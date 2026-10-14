# Intake and evidence

Use this reference before drafting a new proposal or materially changing claims, targets, scope, or proof.

## Required intake

Capture the following. Infer only when the supplied evidence makes the answer clear.

- Client name, industry, audience, and recipient role
- Business decision requested from the reader
- Current workflow and the operational or commercial problem
- Desired future workflow and expected users
- Long-term system concept and the current phase boundary
- Project duration, deliverables, client approvals, and dependencies
- Success measures, baseline availability, observation windows, and owners
- Eziwork experience relevant to this client
- Client and partner logos, brand rules, and output path
- Source documents, URLs, interviews, and unresolved choices

Use `assets/project-brief-template.json` as a working structure when a project contains many sources or revisions.

## Fact register

Maintain a compact fact register before writing proposal copy.

| Field | Meaning | Allowed use |
|---|---|---|
| Provided fact | Explicitly supplied by the user or an authorized source | May be stated directly with a source note when useful |
| Externally verified | Confirmed through an official primary source | State with a readable citation |
| Eziwork provided | Internal experience that cannot be independently verified | Append `Eziwork 제공 정보 기준` |
| Proposal target | A measurable value proposed for the project | Use `제안 목표`; never phrase as a guaranteed result |
| Hypothesis | A value or relationship to test | Use `PoC 검증 전 가설값` |
| To be confirmed | Depends on access, policy, country, channel, or kickoff decisions | Assign the most precise decision-stage label below |

`Provided fact` and `Externally verified` are internal fact-register statuses; they do not require a badge on every proposal sentence. Use the following visible Korean labels only when they materially prevent misunderstanding:

- `Eziwork 제공 정보 기준`: non-public Eziwork experience or internally supplied evidence
- `제안 목표`: a measurable target proposed for agreement, not a guarantee
- `PoC 검증 전 가설값`: an effect or relationship that must be tested
- `착수 전 확정`: access, security, roles, approval authority, scope exclusions, or other prerequisites
- `1주차 확정`: baselines, final target values, and measurement thresholds that require live data
- `후속 단계 검토`: explicitly out-of-scope capability that may be considered later

Use the older umbrella label `착수 후 확정` only when the exact decision point genuinely cannot be assigned yet.

## Evidence precedence

1. The user's current explicit request
2. Confirmed project decisions in the current conversation
3. Current client-provided materials
4. Official primary sources
5. Prior proposals used only as examples

If sources conflict, do not silently choose. Preserve the user's explicit priority rule when one exists; otherwise flag the conflict and use the least assumptive statement that keeps the proposal moving.

## Numerical claims

- Do not turn a directional benefit into a percentage.
- If the user requests target values, label them as proposal targets and state how week-one baselines will confirm them.
- Every KPI needs: definition, formula, source, measurement cycle, baseline, target, and owner.
- Confirm data availability, measurement feasibility, access rights, and KPI ownership before kickoff. Confirm baseline and final target values during week one when live data is required.
- Use observation windows only when the platform, access rights, and data collection method support them.
- Separate business outcomes from system outputs. A generated draft is an output; increased revenue is an outcome that usually needs a longer validation window.

## Logos and external facts

- Prefer official client websites, official press materials, or user-provided originals.
- Preserve logo aspect ratio and colors. Do not redraw a logo.
- If a transparent original is unavailable, use the best official asset and place it on a suitable neutral background.
- Cite time-sensitive company or product facts from current official sources.

## Sensitive reuse boundary

The retained HIRONIC proposal contains client-specific content. Use it only to understand page hierarchy, density, component styling, and executive narrative. Never reuse its facts, target values, company names, system names, or logos as defaults.

Before opening the retained reference, record the current client name and add at least `HIRONIC` and `하이로닉` to the final PDF's forbidden-token check unless HIRONIC is the current client.

## Operating-cost and system-limit register

For systems redesign, record the actual account/seat count, current plan and billing cycle, compute specification, region, storage, and any unverified invoice components. Distinguish a customer's confirmed bill, a configured service's public list price, and a potential upgrade scenario. Never label the upgrade scenario `현재 요금`.

For every reduction record the scope, before/after units, formula and status. Distinguish returned rows from HTTP calls, duplicate updates from duplicate sends, one execution from a daily total, task duration from customer delivery time, active workflows from inactive/archived definitions, and counts in one base from counts summed across bases.

Record capacity as per-base limit and actual/approximate remaining usage. For example calculate used = limit - remaining and used% = used / limit; retain the source's approximation. Do not infer a deadline to exhaustion without a measured growth rate.

Recheck time-sensitive official prices and quotas when drafting a new proposal. A free database tier can still have storage, transfer, CPU, connection, backup and inactivity constraints. `Unlimited API requests` does not mean unlimited throughput or storage. Treat credit applications as eligibility-dependent fee offsets, not cash, guaranteed support or perpetual recurring savings.

Use structural risk language when only configuration and customer-reported instability are known. Do not attribute all gateway/timeouts to rate-limit responses without correlated logs. Urgency may be expressed as an internal assessment of inadequate headroom, with supporting facts separated from inferred cause.
