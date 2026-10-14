# PDF production and visual QA

Use this reference for every created or edited proposal PDF.

## Working layout

Keep generated files organized under the current project, for example:

```text
tmp/pdfs/<project>/
├─ assets/
├─ build/
├─ renders-v01/
├─ renders-v02/
└─ qa/
```

Write the stable final PDF to the user-requested output directory. Do not overwrite source documents or user-owned reference files.

## Build discipline

- Separate content data, layout helpers, and page functions.
- Keep a single source of truth for total pages, colors, fonts, system names, and scope status.
- Use explicit output paths rather than the current directory.
- Preserve unrelated user files and existing changes.
- Use official or provided logo assets. Do not redraw logos.

## Render loop

1. Generate the PDF.
2. Run `scripts/validate_pdf.py` for structural checks.
3. Run `scripts/render_pdf.py` at 72 DPI into a new versioned directory.
4. Run `scripts/make_contact_sheet.py` and inspect every page at once.
5. Open pages with density, alignment, logo, chart, or text concerns at original detail.
6. Revise the source and repeat with a new render version.
7. Before delivery, render the latest PDF again and inspect the changed pages plus the complete contact sheets.

Do not treat successful text extraction as visual proof.

## Vision review scorecard

Evaluate every page on these dimensions:

| Dimension | Pass condition |
|---|---|
| Sentence naturalness | No awkward translation, broken particles, or ambiguous subjects |
| Expression fit | Executive language; technical terms explained or replaced |
| Readability | Clear title, adequate font size, sufficient contrast, logical scan path |
| Visualization | Diagrams and comparisons communicate a relationship, not decoration |
| Design quality | Consistent spacing, alignment, cards, icons, colors, and logos |
| Factual integrity | Claims, targets, sources, and status labels are correct |

A page fails when any critical item is present, even if its average score is high.

## Critical visual defects

- Cropped, overlapping, or off-page text
- Broken Korean glyphs or missing font characters
- Blurry, distorted, recolored, or disproportionate logos
- Tables or cards that overflow their containers
- Arrows that imply the wrong order or feedback direction
- Current scope and future scope using indistinguishable styling
- Footnotes or target-status labels unreadable at normal viewing size
- Page number or total-page inconsistency

## Structural checks

- Expected page count or an explicitly approved change
- Consistent page dimensions
- Unencrypted final PDF
- Embedded Noto Sans KR font resources
- No unresolved placeholders or tool tokens
- No prior-client names or system defaults in visible text, PDF metadata, bookmarks, attachments, or generator defaults
- Required system names and status labels present
- Forbidden obsolete copy absent
- Every page uses the intended footer behavior and the authorized brand pair remains Eziwork × client
- Generic English cover eyebrows removed; title, navigation and metadata use the current project naming
- Cover and content-page subtitles are specific Korean questions ending in `~할까요?` (question-only dividers need no duplicate)
- Final file reopens successfully after writing

## Content checks

- Titles alone tell the complete decision story. Each question-form subtitle names what its page explains, and the visual or body supplies the supported answer.
- Korean titles, diagram labels, messages and notes contain no awkward translation-like wording; exact technical identifiers remain intact where required.
- Before-After pages show actual work changes and measurement logic.
- Capability proof links experience to client relevance.
- Architecture, current scope, user functions, roadmap, and KPI pages do not contradict one another.
- The final decision request is explicit and proportionate to the proposal.
- Proposal targets are not presented as guaranteed outcomes.
- Access rights, security, role ownership, and measurement feasibility are resolved before kickoff; live-data baselines and target thresholds may be finalized in week one.

## Stopping rule

Stop iterating only when the latest renders contain zero critical defect and no remaining issue would materially affect executive comprehension, factual trust, or brand credibility.

## Landscape HTML, revisions and sharing

1. Start from the latest approved master, not an older builder whose run would restore deleted material. Keep content, layout and evidence separated; do not accumulate a permanent v1→v2→... patch chain for new projects.
2. When deleting/merging/reordering, regenerate `NN / TT`, page IDs, `aria-labelledby`, navigation options and internal links from the same ordered page list. A deleted page's unrelated following pages stay unless the user includes them.
3. Keep source and output distinct. Reuse the previous client deck only as authorized visual reference; never import its operational figures, platform choices or client logos automatically.
4. Source hyperlinks may remain online, but a sharing HTML must not need local sibling folders or live asset servers. Embed images/logos, all used font weights, CSS and JS. Check CSS `url()`, nested styles, `src`/`srcset`, icon links and SVG image references; `file:` paths and relative font files are dependencies too.
5. For supported local assets run `python scripts/pack_html.py input.html output.html`. The script refuses unsupported remote assets/complex dependencies instead of claiming a fully portable file. Consolidate dynamic imports, CSS imports and complex srcsets first. It reads only inside the input's asset root, does not download anything, and preserves ordinary citation links. Run `--check output.html` for a dependency audit.
6. Reopen the packaged artifact and inspect the changed pages plus a full contact sheet using available permitted rendering tools. Check loaded font weights, nonzero image dimensions, SVG parsing, content/footers staying in bounds, responsive reading view and print page breaks. XML and static checks alone are not visual QA.
7. Include an HTML print stylesheet: one landscape design canvas per printed page, hidden navigation, no clipped overflow, background colors/markers retained. For a requested PDF, load the PDF skill and export/render/inspect the actual result. A browser connection or permission failure is not success and must not be bypassed with an unauthorized alternative route.
8. Explain sharing accurately: send the actual standalone HTML attachment; a `C:/...` link only works on the owner's computer. Report file size if material. Fonts/images should work offline, but citation clicks need internet. Embedded assets improve consistency, not a guarantee that all browser engines render identically.
9. Package once; do not repeatedly embed the same fonts. Prefer optimized official vectors and tested WOFF2/subsetting when available and permitted. Never change font glyph coverage or destroy logos merely to hit a file-size target.

## Final review prompts

### Focused revision regression checks

- Select the latest approved artifact before editing. For a CSS-only correction, assert that the page-body markup is unchanged. For an icon replacement, compare visible text, actual brand-image tags and footers before/after; preserve numbering, navigation and existing typography unless the request includes them.
- After an all-duotone conversion, check that no superseded 3D image instances remain in the final HTML, every SVG parses, and icon styles are consistent. Do not delete the user's earlier preview assets simply because they are no longer embedded.
- Inspect centered architecture cards at normal slide size: logo, icon-title group and description centers, arrow centers and equal spacing. A parent `text-align:center` is insufficient for a flex heading. Check current and future structures plus responsive/print styles.
- Inspect the cover at normal slide size: title at the left, authorized Eziwork × client logos at the upper right, separate space for both, and no collision. Inspect footer logo order, visible artwork balance and separator alignment on every page.
- Recheck question-form subtitles, long titles and enlarged risk statements for wrapping/overflow, including the actual embedded heavy font. Preserve compact estimate/target labels even when removing dense footer explanations; keep their full calculations separately.
- Inline selected SVG symbols/geometry: do not leave `<use href="icons.svg#...">` or sibling paths in a shareable HTML. Verify fragment IDs resolve if using inline symbols. Existing raster assets must be real embedded images; requested transparency must be actual alpha rather than painted checkerboard pixels.
- Static content, XML, font/dependency checks and source-level alignment fixes do not establish visual success. Use permitted rendering in the current environment when available; if blocked, identify the outstanding screen check, do not bypass the restriction, and do not advertise a generated PDF that was not created.

### Executive review

- Can the executive read title → question-form subtitle → visualization and see the page's answer without reconstructing missing meaning?
- Does every numbered issue link to an actual solution, and are redundant diagnostics merged?
- Are counts/time/money labeled as observed, proposed or conditional without dense footnotes?
- Do component totals use the same scope/FX/tax/billing basis, with compute vs DB and credits separated?
- Is a free-plan option conditional on measured capacity/traffic/backup needs rather than chosen only for a zero-price claim?
- Are deleted notes and optional expansion pages still absent? Are the costs and copied labels current everywhere?
- Are all images/fonts embedded in the delivered HTML, and is PDF export actually complete if requested?

If final visual verification is blocked, deliver only as an explicitly unverified revision when useful, identify the unresolved check and request user review. Do not encode a prior environment's browser outage as a permanent property of the skill.
