# Windows · macOS 설치

이 저장소를 Codex 스킬 폴더의 `eziwork-b2b-ax-proposal`에 놓고 Codex를 다시 연 뒤 `$eziwork-b2b-ax-proposal`을 사용합니다.

## 프로젝트별 설치

~~~shell
git clone https://github.com/eziwork/eziwork-b2b-ax-proposal.git .agents/skills/eziwork-b2b-ax-proposal
~~~

설치 후 다음 파일이 있는지 확인합니다.

```text
프로젝트/.agents/skills/eziwork-b2b-ax-proposal/SKILL.md
```

## 개인 공통 설치

여러 프로젝트에서 사용할 때는 사용자 스킬 폴더에 내려받습니다.

**Windows PowerShell**

~~~powershell
git clone https://github.com/eziwork/eziwork-b2b-ax-proposal.git "$HOME/.agents/skills/eziwork-b2b-ax-proposal"
~~~

**macOS 터미널**

~~~shell
git clone https://github.com/eziwork/eziwork-b2b-ax-proposal.git ~/.agents/skills/eziwork-b2b-ax-proposal
~~~

같은 이름의 폴더가 이미 있다면 기존 파일을 확인한 뒤 업데이트하거나 별도 위치에 보관합니다. 설치 또는 업데이트 후 Codex를 다시 열어 스킬 목록을 갱신합니다.

## 선택 실행 환경

`SKILL.md`와 참고 문서는 별도 설치 없이 사용할 수 있습니다. 포함된 제작·검수 스크립트를 직접 실행하려면 다음 도구가 필요할 수 있습니다.

| 도구 | 사용 목적 |
|---|---|
| Python 3.11 이상 | PDF 검사, 페이지 렌더링, 접촉면 생성 |
| Playwright와 Chromium | HTML을 PDF로 출력할 때 사용하는 선택 렌더러 |
| Poppler | 환경에서 허용되는 경우 PDF 페이지 이미지 렌더링 |

필요한 도구는 수행 작업에 맞춰 설치합니다. 외부 패키지나 브라우저를 설치하기 전 해당 프로젝트의 실행 환경과 보안 정책을 확인합니다.

## 설치 확인

Codex에서 다음과 같이 요청합니다.

~~~text
$eziwork-b2b-ax-proposal
첨부 자료를 바탕으로 제안서의 목차와 필요한 확인 항목을 먼저 정리해줘.
~~~

스킬이 인식되면 근거 상태, 제안 목적, 대상 독자와 출력 형식을 확인한 뒤 작업을 시작합니다.
