# Executive system-improvement playbook

Use for an existing-service redesign proposal. This encodes the approved editorial and comparison patterns, not a fixed client, stack, duration, fee, page count or numerical result.

## 1. Evidence before a proposal

If the user is still planning, collect data before creating the deck:

1. Map actual systems, workflow triggers, storage, staff input, content generation/review, message delivery, hosting and return/status paths.
2. Identify duplicated work, data/API ceilings, missing role separation, costs, reliability and maintenance burden.
3. Quantify only what the evidence supports. Then agree on the outline and implementation scope.

Prefer bounded read-only diagnostics. Do not add production load by crawling all customer records merely to decorate a usage bar when an account usage view or existing count is sufficient. API keys never belong in proposal files, logs, chat or screenshot examples.

## 2. Page sequence and non-overlap

| Page family | Main question | Preferred treatment |
|---|---|---|
| Cover | Who is proposing what to whom? | Co-branded concise title, real logos |
| Background | What concerns does the owner have? | 3 short professional headings with meaningful visuals, a single proposal-purpose line |
| Current workflow | How does the service actually work? | Logos + human roles + directional architecture |
| Optional divider | What is wrong with the current system? | One plain Korean question, no competing detail |
| Numbered problems | Why change now? | Evidence → cause/structure → operational impact |
| Improvement divider | What changes and what improves? | `개선 방향 및 개선 효과` |
| Matched solutions | How does this problem change? | Small exact issue title; large `문제 → 해결 방식`; visual Before-After and useful metric |
| Costs | What happens to recurring spend? | Component current→changed prices; bottom combined annual total and reduction |
| Support, if applicable | How do we offset initial fees? | Place immediately after costs, approval-dependent credit value + application steps |
| Development plan | How do we migrate a live service safely? | Step-by-step roadmap, acceptance/cutover/rollback gates |
| Scope and fee | What is included and what decision is needed? | Agreed scope, duration, amount, VAT and installment terms |

Do not add a generic future-expansion or AI-vision chapter when it weakens the decision flow. Follow a user's removal of divider and detail pages exactly. Avoid blaming a former vendor's competence; describe specific design constraints and risks.

## 3. Problem-to-effect examples

These headings are patterns, not mandatory diagnoses:

- `서비스 확장에 따른 데이터·통신 부하` → `레코드·통신 제약 → 데이터 구조 전환`
- `워크플로우의 비효율적 설계` → `콘텐츠 중복 조회 → 워크플로우 최적화`
- `운영자·직원 전용 페이지 부재` → `전용 업무 화면 부재 → 관리자·직원 페이지 구축`
- `데이터 증가에 따른 시스템 운영비 증가` → `운영비 증가 부담 → 구성별 비용 최적화`
- `발송 상태·이력 관리 로직의 신뢰성 부족` → `발송 실패·누락 위험 → 발송 성공률 개선 및 실패 건 자동 재전송` when bounded automatic retry is included; otherwise describe status/history improvements without promising retry.

Use a general-course explanation when the inefficiency occurs across courses. A named course from one sample may remain in the evidence record but should not make a systemic issue sound exclusive to that course. One sample is still not a global average.

## 4. Quantified Before-After patterns

- Show both percentage and absolute change: count A→B, task duration A→B, yearly price A→B. Use the exact same scope on both sides.
- Display large workflow counts and smaller active/archive definitions. A consolidation target is a target until implementation and regression tests pass.
- Show remaining records as a used/remaining bar, known base limit, source/date and approximate status. Do not fabricate measured traffic or assume row count equals storage size.
- If current platform/server regions are verified, show country flag + region → target flag + region. Explain reduced travel distance, but distinguish user→server from server→database latency and measure instead of inventing milliseconds.
- For duplicated status updates, show record identity through the flow. For dispatch reliability, separate queued, accepted, delivered, failed and retry states; do not imply successful workflow execution means customer delivery.
- For admin separation, show operator approval/assignment/overview vs staff assigned-content editing/review requests. Include authorization at the server/DB level, not only hidden UI buttons.

### Dispatch retry boundary

Explain the proposed flow as `결과 확인 → 메시지별 상태 저장·중복 통제 → 재시도 가능한 실패 건 자동 재전송`. Only confirmed retryable failures enter bounded retry, with a limit and interval appropriate to the provider. Unknown results, permanent failures and exhausted retries remain visible for investigation rather than being resent blindly. Separate provider acceptance from final delivery, retain useful history, and never present a saved-status reduction as a delivery-success percentage. Describing this in a proposal does not authorize live message sending or production workflow edits.

### Split dense pages by decision

Storage capacity and communication/performance deserve separate pages when their Before-After explanations compete. Server/DB plan comparison and total annual savings can likewise split, with identical cost scope and assumptions. Place support applications immediately after related costs; place these after region placement when that is the accepted storyline. Avoid duplicating the same diagnostic prose in each improvement page. Keep user-deleted expansion, AI-vision or extra handover pages deleted; preserve essential operational safeguards in the remaining development pages.

## 5. Cost-page contract

Use `서버 요금제 검토` (or `호스팅 비용`) and `DB 요금제 검토`. Do not turn the DB heading into a presumption that Free is sufficient.

Each component panel:

`현재 로고 + 현재 요금·구성 → 변경 로고 + 변경 요금·구성 → 연간 차이`

Across the bottom:

`현재 연간 (호스팅 + DB) → 변경 연간 (호스팅 + DB) → 총 연간 절감액`

Use KRW on executive pages. Store the original currency and current official source, FX source/date, seat count, billing interval, included storage/IP, taxes and excluded usage in the evidence record. Retain a short meaningful exclusion line if the figure is not total service cost.

Calculate on unrounded source values, round only displayed amounts:

```
monthly_component = source_currency_amount × FX
annual_total = 12 × sum(comparable_monthly_components)
annual_savings = annual_current - annual_changed
reduction_percent = annual_savings / annual_current × 100
```

If annual billing, commitment discounts or varying hours are involved, use the actual annual basis instead of assuming a month × 12 is the invoice. For VM estimates include stated disk/IP/hours, burst or sustained CPU behavior, operations/backup needs. Same vCPU/RAM labels do not establish equal workload performance.

When current price is unknown, show `확인 필요` and distinguish the assumed scenario prominently. Replace it with a user-confirmed price when supplied, including the total and all active comparison pages. A known single shared account is not several paid seats.

For Free DB: compare projected migrated DB+index size, log retention/growth, file storage, monthly egress, burst concurrency, backup/restore and idle-pause behavior. Prefer `무료 조건 충족 시` plus paid fallback until validated. Do not claim unlimited records, transfers and performance merely because the API request count is unlimited.

For subsidies: show currency-converted **usage-credit** value, not cash; actual award/expiry/eligible services and owner approval matter. Application steps: eligibility → documents → submission/review → approved-credit usage/budget. Explain Eziwork's assistance without claiming it controls approval. Do not double-count temporary credits in recurring annual savings.

## 6. Development and delivery

For a live service, staged preparation and validation is usually appropriate, but uncontrolled dual writes can create divergence. A useful pattern is schema/mapping → migration rehearsal and reconciliation → automation/admin implementation → non-sending shadow comparison → limited pilot with one authoritative writer → cutover/rollback window → handover. Adapt dependencies and gates to the actual system; do not promise that every project takes the same number of weeks.

Make service continuity concrete with a side-by-side view: **existing DB/server/automation remain operating**; **a separate new server/automation/DB environment is developed and verified**; approved cutover happens after validation. Use the current project's actual platform logos, retain original data/environment for recovery, and minimize operational impact without promising zero risk. An isolated build does not by itself change an already agreed schedule; retain the current duration unless the user explicitly changes it.

Explain fees and VAT separately; note installments only when authorized and leave unsupplied installment details for agreement. Keep scope exclusions meaningful, not a page of defensive language.

Final HTML sharing means an actual self-contained attachment, not a local path link or an unapproved website deployment. Use the packaging and QA rules in `production-and-qa.md`.
