# Eziwork proposal visual system

Use this reference when creating or restyling landscape HTML or PDF proposals. Inspect the relevant PNGs under `assets/reference/pages/` at original detail when exact placement or density matters.

## Default canvas

- 16:9 landscape PDF
- Reference coordinate system: 1920 × 1080 points
- White background with generous negative space
- Default safe margins: 120 points left and right, 70-90 points top, 60 points above the footer
- Keep all pages the same size

For HTML use a 1920 × 1080 CSS-pixel design canvas with screen scaling and print pagination. Do not confuse CSS pixels with PDF points. `assets/layout/executive-landscape.css` contains neutral reusable components. Choose this landscape system for new system-improvement decks; preserve an approved existing design during focused edits.

Use A4 only when the user explicitly requests a document-style proposal. Do not mix A4 and 16:9 pages.

## Brand palette

| Role | Color |
|---|---|
| Primary blue | `#2448E7` |
| Deep blue | `#1728B7` |
| Mid blue | `#6E87EE` |
| Light blue | `#A7B8FF` |
| Blue tint | `#EEF2FF` |
| Purple accent | `#7956D8` |
| Purple tint | `#F3EEFF` |
| Main text | `#272B3A` |
| Secondary text | `#596174` |
| Border | `#D8DEEF` |
| Card background | `#F6F7FA` |

Use blue for the current decision and current implementation scope. Use purple for later expansion or a secondary system group. Use gray for context. Do not add unrelated accent colors without a semantic reason.

## Typography

- Use the bundled Noto Sans KR fonts from `assets/fonts/`.
- Title: Black, generally 44-56 pt
- Section or card title: Bold/Black, generally 22-30 pt
- Body: Regular/Bold, generally 17-21 pt
- Footnote: generally 12-14 pt; never use a size that is unreadable at normal slide view
- Use weight and spacing before adding more color.
- Keep line lengths compact. Break dense explanations into short labels and supporting sentences.

The bundled font copies have unique internal names for reliable ReportLab embedding. Register them instead of relying on system fonts.

## Components

- Use a short blue rule above the main title.
- Prefer rounded information cards with thin gray or blue borders.
- Use pastel fills only to group information, not to decorate empty areas.
- Use solid blue bars for decisions, approval requests, or key scope statements.
- Use compact pills for phase, status, or proposal-target labels.
- Keep non-brand icons consistently duotone: blue outlines with pale blue filled shapes, equal visual weight. Use the icon contract below; do not mix in soft 3D by default.
- Use a visible directional flow for processes. Arrows should express actual movement or feedback.

## Cover and page subtitles

- Use a clear Korean client-and-subject title on the cover. Omit generic English eyebrows such as `SYSTEM IMPROVEMENT`, unless the user explicitly requests one.
- Under each page title, use the question-form subtitle specified in `storyline-and-copy.md`. Keep it readable and visibly connected to the title.
- Check question wrapping at the actual slide scale. Do not shrink the whole page to fit a long subtitle; shorten the question or use an intentional line break.

## Density and hierarchy

- One page carries one conclusion.
- Avoid more than three equal content columns unless the information is extremely short.
- A card should normally contain one headline and no more than four short supporting rows.
- Split a page when body text must be reduced below the minimum size.
- Avoid large decorative areas that do not help the decision, except on cover and closing pages.

## Logos

- Use the Eziwork wordmark from `assets/brand/eziwork-wordmark.png`.
- Find and use the current client's actual logo when available. Prefer a supplied original or an official brand source, and record its provenance. Do not replace an available logo with plain text or a letter badge. Acquire partner logos per project; never reuse a prior client's logo as a default asset.
- Preserve aspect ratio and original colors.
- Crop only empty outer whitespace when necessary; do not crop the artwork.
- Set the authorized brand pair in the order **Eziwork logo × client logo** on the cover and all footers. Keep the separator centered. Balance visible artwork size optically rather than giving logos with different proportions the same height; neither logo should dominate.
- On a new cover, keep the title at the left and the brand pair at the upper right. Reserve separate layout space so a long title cannot overlap the logos. Prefer grid or flex columns over absolute positioning without collision checks.
- Inspect logos at high detail after rendering, including the cover pair, footer order, artwork size, whitespace and alignment.

## Footer and numbering

- Use a thin light-gray divider near the bottom.
- Place **Eziwork logo × client logo** at the lower left when both are authorized, in the same order on every page.
- Place page numbering at the lower right as `NN / TT`.
- Include the cover in numbering when the selected reference style does so.
- For this user's clean executive layout, keep the footer to authorized co-branding and `NN / TT`. Do not add execution IDs, dates, source captions or explanatory prose to it by default. Preserve evidence in a separate register and short material estimate/target labels beside the relevant metric. Follow explicit requests for visible citations without overcrowding the footer.

## Reference-page map

- 01: cover hierarchy and dual-logo balance
- 03: problem cards
- 04-05: Before-After and target visualization
- 06-07: proof and capability pages
- 08: long-term architecture
- 09-12: priority, flow, scope, and deliverables
- 13: roadmap and approval gates
- 14: KPI scorecard
- 15: minimal closing page

## Approved emphasis and visualization patterns

- Use a restrained fluorescent marker treatment behind decisive amounts, remaining capacity, action phrases and Before-After numbers. Typically 1-3 short highlights per page, not whole paragraphs. Preserve dark readable text over the marker.
- At 1920px design width, start around 48-56px for a headline, 27-31px for a key message, 25-30px for body, 18-20px for compact notes. These are HTML dimensions, not PDF point sizes. Give large cost/count metrics 48-72px where space allows.
- Center each comparison on an obvious arrow: official source logo + current state → official destination logo + changed state. Keep the same metric, unit and time window on both sides.
- Remaining capacity: show used and remaining quantities plus a proportional horizontal bar only when the denominator is known. An approximate customer figure produces approximate percentages. Never fill a bar with an invented percentage merely to communicate urgency.
- Repeated retrieval: several recipients → repeated requests for the same content, contrasted with one content retrieval → reuse for recipients. Repeated status writes: same record ID appearing repeatedly → deduplicate → one write. Do not depict repeated writes as duplicate customer sends.
- Workflow optimization: make `current active count → proposed count` the largest element; show course-specific settings feeding common processing. Do not compare all archived workflows against only the new active set.
- Admin examples: operator screen left, employee screen right. Use substantial outer borders (about 4px at 1920px), clear window headers and different allowed actions. Label screens as examples; use non-personal example data.
- Costs: server and DB each get a `현재 요금 → 변경 요금` comparison with logos; the bottom spans the page for combined annual cost and annual savings. Avoid squeezing three pricing catalogs and multiple caveat paragraphs into the same panel.
- Logos: use authentic, aspect-correct assets, transparent when available. Include the relevant platform logos in architecture nodes and a horizontal platform strip on the background page when requested. Distinguish a platform strip from client proof. A textual name plus broken logo is not acceptable QA.
- Architecture includes human inputs and outputs, not only platform boxes: storefront/customer input, content generation, employee review, DB, automation, message provider and recipient as applicable. Arrows represent verified directions.
- Region comparisons may use country flags with city/region labels. Mark current region as unknown if not checked; do not use flags to imply a guaranteed performance multiplier.
- Use graphs only for real comparisons; label structural diagrams and illustrative trends as concepts rather than measured time series.

## Approved duotone icon contract

- The final selected style is **all duotone**, including major pages. Earlier soft-3D, glass, metal and other previews were exploration, not continuing defaults. Produce new variants only when asked; do not apply preview variants without selection.
- Prefer editable inline SVG for these icons, not generated bitmap substitutes or icon-font dependencies. `assets/icons/duotone.svg` supplies reusable geometry. Use a `0 0 48 48` viewBox, cobalt `#2448E7` strokes at about `2.5`, pale fill `#A7B8FF`, light secondary fill `#EEF2FF`, and rounded joins/caps. Brand logos keep their original colors and proportions.
- Supporting symbols are normally 32-42px; a background-page concept illustration can be 180-210px high. Enlarge the same style rather than changing the material. Choose symbols by meaning: storage/growth, shield/heartbeat, people/lock, failure envelope, exposed lock and damaged trust. Icons are optional where a logo or graph already communicates enough; do not blanket-decorate every heading.
- Preserve large-font live HTML labels outside the SVG. Use `aria-hidden="true"` for an icon that duplicates adjacent text; standalone diagrams need an accessible label.

## Alignment and risk emphasis

- In centered workflow cards, the platform logo, **icon-plus-title group**, and explanation share one horizontal center. `text-align:center` alone does not center a flex heading: set `justify-content:center; align-items:center` on that group. Use equal logo slots, consistent title spacing and card padding; keep inter-card arrows vertically centered. Apply the correction to both current and proposed workflows when they use the same component, not to unrelated left-aligned prose.
- For an emphasized risk statement, use about 28px / weight 900 on the 1920px canvas, dark ink and the yellow marker `#FFF08A`. Wrap only the decisive sentence in `<mark>`, with cloned line decoration and a background starting about 35% down the line. Leave body copy unhighlighted and recheck wrapping after enlargement. The neutral CSS provides `.risk-statement`.
- Prominent evidence/decision phrases may use the same marker, but do not turn the whole page yellow. User-requested risk headings can take priority over the ordinary 1-3-highlight guideline.
