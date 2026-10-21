---
version: alpha
name: BMW-Motorrad-design-analysis
description: A private design system for the BMW Motorrad model catalogue and filter experience — engineered, photographic, confident, and built around the motorcycle as the object of desire.
privateUse: true
source: "https://www.bmw-motorrad.de/de/home.html#/filter-alle"
sourceNote: "Original analysis for private use. This is not an official BMW Motorrad design-system document."

colors:
  canvas: "#000000"
  canvas-soft: "#111111"
  surface: "#1A1A1A"
  surface-elevated: "#262626"
  surface-soft: "#0D0D0D"
  surface-light: "#F5F5F5"
  ink: "#FFFFFF"
  ink-dark: "#1A1A1A"
  body: "#C7C7C7"
  muted: "#898989"
  hairline: "#3C3C3C"
  primary: "#1C69D4"
  primary-active: "#0653B6"
  m-blue-light: "#0066B1"
  bmw-blue: "#0066B1"
  m-blue: "#1C69D4"
  m-red: "#E22718"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  on-light: "#1A1A1A"
  success: "#22C55E"
  warning: "#F59E0B"
  danger: "#DC2626"

typography:
  display-xl:
    fontFamily: "'BMW Type Next Latin', system-ui, sans-serif"
    fontSize: 80px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0"
  display-lg:
    fontFamily: "'BMW Type Next Latin', system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "0"
  display-md:
    fontFamily: "'BMW Type Next Latin', system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "0"
  title-lg:
    fontFamily: "'BMW Type Next Latin', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0"
  title-md:
    fontFamily: "'BMW Type Next Latin', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0"
  body-md:
    fontFamily: "'BMW Type Next Latin Light', 'BMW Type Next Latin', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: "0"
  body-sm:
    fontFamily: "'BMW Type Next Latin Light', 'BMW Type Next Latin', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: "0"
  caption:
    fontFamily: "'BMW Type Next Latin', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0.05em"
  label-uppercase:
    fontFamily: "'BMW Type Next Latin', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.12em"
    textTransform: uppercase
  button:
    fontFamily: "'BMW Type Next Latin', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.08em"
  nav-link:
    fontFamily: "'BMW Type Next Latin', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0.03em"

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 40px
  2xl: 64px
  3xl: 96px

components:
  top-navigation:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.xl}"
  primary-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: "16px 32px"
    minHeight: 48px
  primary-button-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  secondary-button:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: "15px 31px"
    minHeight: 48px
  dark-button:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: "16px 24px"
  model-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  model-card-media:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
    objectFit: contain
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.label-uppercase}"
    padding: "{spacing.md} 0"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    padding: "{spacing.md} 0"
    borderBottomColor: "{colors.ink}"
  filter-control:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  selected-filter:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  spec-cell:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  dark-photo-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.3xl}"
  m-stripe:
    backgroundColor: transparent
    height: 4px
    colors: "{colors.m-blue-light} → {colors.m-blue} → {colors.m-red}"
  carousel-control:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 48px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.2xl} {spacing.xl}"
---

# BMW Motorrad model catalogue

## Brand reading

BMW Motorrad presents motorcycles as engineered objects with a strong emotional charge. The page
should feel precise and physical: a dark stage, controlled typography, large motorcycle imagery,
clear model families, and direct routes into configuration or product detail.

This system is intended for a private implementation or case-study reconstruction of the German
BMW Motorrad catalogue experience. Keep the product content and assets honest; do not imply that a
private project is an official BMW Motorrad website.

## Design idea

On this page, the motorcycle range becomes a dark showroom: each model is given enough space to
read as an object, while filters act like the showroom's navigation system.

Use this idea throughout:

- Give each motorcycle a clean stage rather than a decorative card treatment.
- Let model family, silhouette, and photographic crop carry hierarchy.
- Treat filtering as a primary browsing action, not a buried utility.
- Use the BMW blue for action and navigation; reserve the M blue/red stripe for authentic M-related
  branding or a clearly labelled motorsport context.
- Keep the black field confident and quiet so the motorcycle remains the loudest element.

## Brand principles

1. **Object first.** Product photography and silhouette are more important than ornament.
2. **Engineered confidence.** Copy is short, factual, and assured. Avoid hype stacked on hype.
3. **One decision per view.** A model card asks the visitor to explore that model; a filter asks
   which family or use case they want.
4. **Performance is specific.** Use real specifications with units and context; never invent range,
   power, price, or availability.
5. **Premium through control.** Use scale, crop, contrast, and spacing instead of shadows, gradients,
   floating glass, or excessive corner rounding.
6. **Motion serves the machine.** Transitions may reveal a motorcycle or move between catalogue
   states, but must not turn the interface into a spectacle.

## Catalogue information architecture

### Home / hero

The opening viewport is a full-bleed motorcycle image or product-led visual with a short headline,
model or campaign name, and one primary action. Keep navigation visible and functional. The title
must identify what the visitor is seeing; do not use an abstract slogan alone.

### Model range

The `filter-alle` experience is a catalogue, not a generic marketing grid. Model families should be
available as explicit filters or tabs:

- Adventure
- Roadster
- Sport
- Touring
- Heritage
- Urban Mobility
- Electric, where current product data supports it

Only show categories that exist in the supplied catalogue data. A selected filter must be reflected
in text, focus state, and the visible result set.

### Model card

Each model card should contain:

- A real motorcycle image or approved product render.
- The model name and family.
- One useful differentiator, such as riding position or intended terrain.
- A direct link such as “Discover” or “Configure.”
- Price or availability only when the source data is current and region-specific.

Do not add a row of decorative feature icons. Do not use generic grey bars as loading content;
provide a labelled loading state and preserve the card geometry.

### Detail and configuration

The product detail route should move from desire to evidence:

1. Large motorcycle view.
2. Model name and concise positioning.
3. Key specifications with units.
4. Equipment, colour, or trim choices.
5. Price or dealer route, when available.
6. Clear action to configure, request information, or find a dealer.

The action label must describe its destination. Avoid “Get started” when “Configure the R 1300
GS” is possible.

## Filter behavior

- Filters are visible before the first result and remain understandable when the result count is
  zero.
- “All” is a real selected state, not an unlabelled reset icon.
- Multiple active filters show their names and can be removed independently.
- Results update without losing keyboard focus or scroll position unexpectedly.
- A no-results state explains how to broaden the selection.
- On mobile, open filters in a full-width sheet or panel with a persistent apply/close action.
- Filter controls use square geometry and clear selected contrast, not pill-chip decoration.
- URL state should be shareable when the implementation supports routing.

## Composition

Use the tagged direction **The well-kept board** (`dense-tiles`, seed `125985394`) only as a layout
reference, not as a literal visual copy:

- Keep its dense, filled composition and varied tile sizes.
- Replace generic tiles with product stages, model imagery, category controls, and specifications.
- Use a dark photo-led opening rather than the direction's stone palette.
- Let model cards align in a disciplined catalogue grid, with enough negative space around each
  motorcycle to preserve silhouette.
- Use a full-width photographic or black section to reset the eye between catalogue groups.
- On mobile, keep the selected category and first model visible before secondary navigation.

Recommended page order:

1. Persistent navigation.
2. Hero motorcycle or model campaign.
3. Category tabs and filter controls.
4. Model catalogue.
5. Feature or technology image band.
6. Comparison/specification view.
7. Dealer/configuration action.
8. Footer and legal links.

## Imagery

Photography is the primary material. Prefer:

- Full-bleed motorcycle product photography.
- Three-quarter views that preserve the complete silhouette.
- Detail crops of engine, wheel, cockpit, lighting, or material.
- Riders and landscape only when they clarify the motorcycle's intended use.
- Consistent background treatment across a model family.

Never present stock motorcycle imagery as a specific BMW Motorrad model. If official product assets
are unavailable, use clearly labelled placeholders or a code-drawn interface study rather than
misrepresenting another motorcycle.

Image treatment:

- Square corners by default.
- Dark or neutral fields behind cut-out motorcycles.
- No colour overlays that obscure paint or material.
- `object-fit: contain` for product renders; `object-fit: cover` for environmental photography.
- Alt text identifies the model and view, for example: “BMW R 1300 GS in three-quarter front view.”

## Content and copy

- Use sentence case for explanatory copy and restrained uppercase only for short navigation labels.
- Keep headings short enough for two lines at desktop and mobile.
- Prefer “Explore the models” to “Begin your journey.”
- Prefer “Compare specifications” to “See what sets it apart.”
- Use German copy when the target experience is German; do not mix English CTA labels into a German
  page without an explicit localization decision.
- Preserve official model names, capitalization, units, and legal qualifiers.
- Never fabricate reviews, awards, customer counts, test results, finance rates, or inventory.

## Interaction states

- `default`: white or light-grey type on the dark field.
- `hover`: a controlled image crop shift, underline, or blue action state; never a floating card.
- `focus-visible`: a high-contrast outline that is visible against both black and white surfaces.
- `selected`: active category/filter uses strong contrast and a text label.
- `disabled`: reduced contrast with an explanation where the action is unavailable.
- `loading`: preserve the product-card layout and announce loading status.
- `error`: name the failed operation and provide a retry path.
- `no-results`: explain the active filters and offer a clear reset.

## Responsive behavior

- Desktop uses a 12-column grid with 24–32px gutters and equal outer margins.
- Tablet reduces the catalogue to two columns without shrinking product imagery below legibility.
- Mobile uses one model per row and keeps the product name, family, and primary action in the first
  view of each card.
- The filter control becomes a full-width action near the catalogue heading.
- Navigation may collapse, but the BMW Motorrad identity and the current catalogue context remain
  visible.
- Touch targets are at least 44px. Body text remains at least 16px.

## Motion

- Use one controlled reveal for the hero motorcycle: clip or shutter the image into view, then
  settle the crop.
- Model cards may fade or translate a small distance when the filter result changes.
- Do not animate every tile independently or use parallax that changes the motorcycle silhouette.
- Respect `prefers-reduced-motion`; the complete image and result state must remain immediately
  available.

## Accessibility

- Use one `h1` for the current page or campaign.
- Use real buttons for filter toggles and real links for model routes.
- Announce result-count changes to assistive technology without stealing focus.
- Expose selected filter state with `aria-pressed` or an equivalent semantic pattern.
- Do not encode model family, availability, or status by colour alone.
- Provide keyboard access to every carousel control and a non-carousel fallback for product media.
- Ensure white text, BMW blue, and muted copy meet contrast requirements on their actual surfaces.

## Implementation constraints

- Use the YAML tokens above as the source of truth.
- Keep the visual system to black, white, greys, BMW blue, and the restrained M stripe.
- Do not introduce gradients, glow effects, glass panels, or soft “app” cards.
- Use BMW Type Next only when the project has the right to load it; otherwise use a documented
  fallback such as Arial or a comparable neutral grotesk.
- Keep official logos and product photography as supplied assets. Do not redraw or modify protected
  marks.
- Include a small source/asset credit area where required by the asset licence.

## Content to confirm before publication

- The exact market and language: this source is the German BMW Motorrad site.
- Current model families and model names.
- Whether pricing and finance information may be displayed.
- The approved BMW Motorrad logo, BMW roundel, and any M branding assets.
- Product image rights and crop permissions.
- The real target for “Configure,” “Find a dealer,” and information-request actions.
- Whether the page is a private case-study reconstruction, internal prototype, or public-facing work.
