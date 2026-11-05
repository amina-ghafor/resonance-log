# TODO

Done:

- Seed entries in `entries.yaml` with `tldr` and `why`.
- Index renderer (`render_index.py`): reads `entries.yaml`, writes `INDEX.md`
  grouped by skill area and by month. Tests in `test_render_index.py`.
- Published on GitHub with an MIT LICENSE.
- `.ics` generator (`render_ics.py`): one event a week per entry to revisit,
  written to a committed `resonance.ics`. Tests in `test_render_ics.py`.

Deferred to v1.1: a GitHub Action that opens a weekly "review this week's entries" issue.
