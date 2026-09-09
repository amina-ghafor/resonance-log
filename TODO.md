# TODO

Next three, in order:

1. Fill `tldr` and `why` for the six seed entries in `entries.yaml`. Check the
   `skill_area` / `format` / `stage` tags while doing it and adjust any that are wrong.
2. Write the index renderer: read `entries.yaml`, group by `skill_area`, write a
   Markdown index (to the README or a separate `INDEX.md`). Python, stdlib plus PyYAML.
3. Write the `.ics` generator: one VEVENT per entry on a weekly cadence, output a
   committed `resonance.ics` anyone can subscribe to by raw URL. No calendar API.

Deferred to v1.1: a GitHub Action that opens a weekly "review this week's entries" issue.

Open decision: whether to publish the repo on GitHub now or after the renderer works.
Add a LICENSE when publishing (MIT, matching opportunity-tree).
