"""Embed a local static proposal's assets; reject unsupported dependencies, never fetch URLs.

python pack_html.py source.html share.html [--asset-root DIRECTORY]
python pack_html.py --check share.html
Input/output must differ. Source hyperlinks remain hyperlinks. Complex dynamic sites are out of scope.
"""
import argparse
import base64
import mimetypes
import re
import sys
from pathlib import Path
from html import unescape
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET

URL = re.compile(r'url\(\s*([\'"]?)(.*?)\1\s*\)', re.I | re.S)
ATTR = re.compile(r'(\b(?:src|poster|href|xlink:href)\s*=\s*)([\'"])(.*?)\2', re.I | re.S)
MIME = {'.ttf':'font/ttf','.otf':'font/otf','.woff':'font/woff','.woff2':'font/woff2','.svg':'image/svg+xml'}

def is_embedded(value):
    return value.startswith(('data:', '#'))

def check_svg(data, depth=0):
    if depth > 8:
        raise ValueError('Nested SVG asset depth exceeds supported static scope')
    root = ET.fromstring(data)
    for node in root.iter():
        tag = node.tag.rsplit('}',1)[-1].lower()
        if tag in ('script','foreignobject'):
            raise ValueError('SVG scripting/foreignObject needs manual portability review')
        for key,value in node.attrib.items():
            name = key.rsplit('}',1)[-1].lower()
            if name in ('href','src') and tag != 'a':
                audit_reference(value, depth+1)
            if name == 'style': audit_css(value, depth+1)
        if tag == 'style': audit_css(node.text or '',depth+1)

def audit_reference(value, depth=0):
    if not is_embedded(value):
        raise ValueError('Found a non-embedded runtime asset')
    if value.startswith('data:image/svg+xml'):
        header,body = value.split(',',1)
        check_svg(base64.b64decode(body) if ';base64' in header else unquote(body),depth)

def audit_css(css,depth=0):
    if re.search(r'@import\b|image-set\s*\(',css,re.I):
        raise ValueError('Flatten CSS imports/image-set before packaging')
    for match in URL.finditer(css): audit_reference(match[2],depth)

class Audit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.images=0; self.styles=False; self.scripts=False; self.ids=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        for name in ('src','poster'):
            if name in a: audit_reference(a[name] or '')
        if a.get('srcset'): raise ValueError('Flatten srcset before packaging')
        if tag in ('iframe','object','embed'): raise ValueError('Embedded documents need manual review')
        if tag in ('image','use'): audit_reference(a.get('href',a.get('xlink:href','#')))
        if tag == 'link' and a.get('href'): audit_reference(a['href'])
        if 'style' in a: audit_css(a['style'])
        if tag == 'img': self.images+=1
        if tag == 'style': self.styles=True
        if tag == 'script': self.scripts=True
    def handle_endtag(self,tag):
        if tag=='style': self.styles=False
        if tag=='script': self.scripts=False
    def handle_data(self,text):
        if self.styles: audit_css(text)
        if self.scripts and re.search(r'\bfetch\s*\(|XMLHttpRequest|WebSocket|import\s*\(|import\s+.+?\s+from\s+[\'"]',text):
            raise ValueError('Dynamic networking/imports require manual portability review')

def audit(html):
    parser=Audit();parser.feed(html);parser.close()
    if len(set(parser.ids)) != len(parser.ids): raise ValueError('Duplicate HTML IDs')
    # Nested SVG resources also need inspection, not just top-level image tags.
    for svg in re.findall(r'<svg\b[\s\S]*?</svg>',html,re.I):
        check_svg(svg)
    return parser.images

def package(source, output, asset_root=None):
    source=Path(source).resolve(); output=Path(output).resolve()
    if source==output: raise ValueError('Use a distinct output; preserve the source')
    if output.exists(): raise ValueError('Output already exists; choose a new output filename')
    allowed=Path(asset_root).resolve() if asset_root else source.parent
    cache={}; count=0
    def local(value,base):
        parts=urlsplit(unescape(value))
        if parts.scheme or parts.netloc: raise ValueError('Remote or file-scheme assets are not fetched')
        p=(base/unquote(parts.path)).resolve()
        if not p.is_relative_to(allowed) or not p.is_file():
            raise ValueError('Asset missing or outside the declared asset root')
        return p
    def embed(value,base):
        nonlocal count
        if is_embedded(value): return value
        p=local(value,base)
        if p not in cache:
            data=p.read_bytes(); mime=MIME.get(p.suffix.lower(),mimetypes.guess_type(p.name)[0] or 'application/octet-stream')
            if mime=='image/svg+xml': check_svg(data)
            cache[p]='data:'+mime+';base64,'+base64.b64encode(data).decode('ascii');count+=1
        suffix=urlsplit(value).fragment
        return cache[p]+('#'+suffix if suffix else '')
    def css(text,base):
        if re.search(r'@import\b|image-set\s*\(',text,re.I): raise ValueError('Flatten CSS imports/image-set first')
        return URL.sub(lambda m:'url("'+embed(m[2],base)+'")',text)
    def attrs(text):
        parser=HTMLParser(convert_charrefs=True)
        result={}
        parser.handle_starttag=lambda tag,a:result.update(dict(a))
        parser.feed(text);return result
    html=source.read_text(encoding='utf-8-sig')
    def link(m):
        a=attrs(m[0]); rel=a.get('rel','').lower(); href=a.get('href','')
        if 'stylesheet' in rel:
            p=local(href,source.parent);text=css(p.read_text(encoding='utf-8-sig'),p.parent)
            if re.search(r'</style',text,re.I):raise ValueError('Unsafe CSS closing tag')
            media=a.get('media');media_attr=' media="'+media.replace('"','&quot;')+'"' if media else ''
            return '<style'+media_attr+'>'+text+'</style>'
        if 'icon' in rel:
            return ATTR.sub(lambda n:n[1]+n[2]+embed(n[3],source.parent)+n[2],m[0])
        raise ValueError('Remove or inline non-stylesheet/non-icon link resources')
    html=re.sub(r'<link\b[^>]*>',link,html,flags=re.I)
    def script(m):
        a=attrs(m[1]);src=a.get('src')
        if not src:return m[0]
        p=local(src,source.parent);text=p.read_text(encoding='utf-8-sig')
        if re.search(r'</script',text,re.I):raise ValueError('Unsafe JS closing tag')
        # Static proposal scripts only; retain module type, reject unsupported loading semantics.
        if any(x in a for x in ('async','defer','integrity')):raise ValueError('Consolidate asynchronous/external script semantics first')
        kind=' type="module"' if a.get('type')=='module' else ''
        return '<script'+kind+'>'+text+'</script>'
    html=re.sub(r'(<script\b[^>]*>)([\s\S]*?)</script>',script,html,flags=re.I)
    html=re.sub(r'(<style\b[^>]*>)([\s\S]*?)(</style>)',lambda m:m[1]+css(m[2],source.parent)+m[3],html,flags=re.I)
    def tag(m):
        text=m[0]; name=re.match(r'<([\w:-]+)',text)[1].lower()
        if name in ('script','style'):return text
        def attribute(n):
            attr=n[1].split('=')[0].strip().lower()
            if attr in ('href','xlink:href') and name not in ('image','use','link'):return n[0]
            return n[1]+n[2]+embed(unescape(n[3]),source.parent)+n[2]
        text=ATTR.sub(attribute,text)
        return re.sub(r'(\bstyle\s*=\s*)([\'"])(.*?)\2',lambda n:n[1]+n[2]+css(unescape(n[3]),source.parent).replace(n[2],'&quot;' if n[2]=='"' else '&#39;')+n[2],text,flags=re.I|re.S)
    html=re.sub(r'<[a-zA-Z][^>]*>',tag,html)
    images=audit(html)
    output.parent.mkdir(parents=True,exist_ok=True);output.write_text(html,encoding='utf-8')
    return {'embedded_local_assets':count,'images':images,'bytes':output.stat().st_size,'external_runtime_assets':0,'visual_qa':'not performed'}

def main():
    import json
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('input',nargs='?');ap.add_argument('output',nargs='?');ap.add_argument('--asset-root');ap.add_argument('--check')
    args=ap.parse_args()
    try:
        if args.check:
            p=Path(args.check);result={'images':audit(p.read_text(encoding='utf-8-sig')),'bytes':p.stat().st_size,'external_runtime_assets':0,'visual_qa':'not performed'}
        else:
            if not args.input or not args.output:ap.error('input and output required')
            result=package(args.input,args.output,args.asset_root)
        print(json.dumps(result))
    except (ValueError,OSError,ET.ParseError) as ex:
        print('Packaging refused: '+str(ex),file=sys.stderr);sys.exit(1)

if __name__=='__main__':main()
