# resonance-calendar - one-pager

Size: S. One weekend for v1, no users but me at first.

## Outcome

A working record of the writing that has actually changed how I work as a PM, kept current so it stays a tool rather than a graveyard of bookmarks.

## Problem

- Resources that shifted my thinking get saved once and never seen again. The saving feels like learning. It isn't.
- Useful references are scattered across browser bookmarks, Slack saved items, and memory. There is no single place to look.
- A flat list gives no sense of when something is worth returning to, or where it sits in a learning path.
- Nothing prompts a revisit. Insight I don't reuse decays.

## Hypothesis

Building a categorised, dated log with a scheduled resurfacing feed will increase how often I re-read and apply the resources that mattered, rather than saving and forgetting them.

## Features

- A structured entry per resource: title, URL, source, date found, skill-area / format / stage tags, TL;DR learning, why it resonated, revisit flag.
- A categorised index rendered from the entries, grouped by skill area.
- An `.ics` feed that resurfaces one entry on a cadence, subscribable in any calendar.
- A capture rule in the README: anything that resonates goes in, no exception.
- Credit to Ali Abdaal for the concept, with a short direct quote and a link.

## Metrics

Number of logged entries I re-read and act on per month, recorded as a dated note on the entry (e.g. `reused: 2026-10`). The outcome is reuse, not entry count.

## Non-goals (cut to keep v1 small)

- No Streamlit or interactive front end. The README index is the interface.
- No Google Calendar API sync. A committed `.ics` file people subscribe to does the same job without auth.
- No automated import from bookmarks or Pocket. Adding entries by hand is part of the filter.
- No full note or summary per resource. The TL;DR line is the point. Longer notes live elsewhere.
- No public submissions or multi-user support.

## Scope

- **In:** the entries file, the rendered index, the `.ics` generator, the README with capture rule and attribution.
- **Out:** hosting, a database, search.
- **Cut for v1** (reasonable to include, deferred to v1.1): an automated Friday review, a GitHub Action that opens a "review this week's entries" issue. The manual habit covers it until then.

## Measure and limit

- **Single outcome metric:** entries re-read and acted on per month, counted from the `reused:` notes.
- **v1 boundary:** done means the entries file with the current resources, a rendered index committed, a working `.ics` anyone can subscribe to, and the README with capture rule and Abdaal credit. Deferred: the Friday review automation and any front end beyond the index.

## Entry schema

Each entry in `entries.yaml`:

| Field | Notes |
|---|---|
| `title` | the resource title |
| `url` | canonical link |
| `source` | publication or author |
| `date_found` | when it came in, `YYYY-MM-DD` |
| `skill_area` | e.g. ai-tools, ai-evals, product-strategy, design-ux, role-of-pm |
| `format` | essay, newsletter, reference, forum-thread, talk, book, podcast |
| `stage` | foundational, mid-build, reference |
| `tldr` | one line, the lesson I took and can apply |
| `why` | why it pulled me in, the context I was in when I found it |
| `revisit` | true / false |
| `reused` | optional, a `YYYY-MM` note each time I re-read and act on it |

`tldr` and `why` stay separate. One is the lesson, the other is the context.
