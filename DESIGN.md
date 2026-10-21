# Workflow automation design system

This project uses a focused operations-console language for service teams. It should feel reliable,
clear, and adaptable to different organizations and request types rather than tied to one industry.

## Visual direction

- Use a dark canvas (`#0B0D0F`) with charcoal surfaces and white primary text.
- Use one cool blue accent (`#4EA1FF`) for the primary action and the main data series.
- Use green, amber, and red only for meaningful status or urgency.
- Prefer flat surfaces, square or lightly rounded geometry, and clear spacing.
- Avoid gradients, decorative icons, fake metrics, excessive shadows, and product-specific marks.

## Typography

- Use Barlow when available, with a system sans-serif fallback.
- Use large, short page titles and compact section headings.
- Keep body copy between 14px and 18px with comfortable line height.
- Use sentence case for explanatory text and restrained uppercase for short labels.

## Dashboard structure

1. Identify the workflow and current scope in the header.
2. State the screen question and the most important finding.
3. Show computed operational metrics without decorative cards.
4. Put the main category and routing signals beside one another.
5. Keep recent cases dense, readable, and aligned.
6. Provide complete operational details behind an expandable section.

## Content and data

- Use generic concepts such as organization, requester, asset, request, category, priority, and route.
- Keep example data clearly fictional and replaceable.
- Compute totals from the displayed records.
- Distinguish a real zero from missing data.
- Never invent customer counts, performance claims, or service outcomes.

## Interaction and accessibility

- Use real buttons, links, inputs, and tables.
- Preserve keyboard focus and provide visible focus states.
- Do not use color alone to communicate priority or status.
- Keep the first action and the current scope visible on smaller screens.
- Provide useful empty, loading, and error states.

## Reuse

The same intake contract can support internal help desks, IT operations, facilities, logistics,
customer support, or other service workflows. Domain-specific vocabulary belongs in configuration
or request content, not in the core data model or visual identity.
