# TODO

Done:

- Seed entries in `entries.yaml` with `tldr` and `why`.
- Index renderer (`render_index.py`): reads `entries.yaml`, writes `INDEX.md`
  grouped by skill area and by month. Tests in `test_render_index.py`.
- Published on GitHub with an MIT LICENSE.

Next:

1. Write the `.ics` generator: one calendar event per entry on a weekly cadence,
   output a committed `resonance.ics` anyone can subscribe to by raw URL. No
   calendar API.

Deferred to v1.1: a GitHub Action that opens a weekly "review this week's entries" issue.
