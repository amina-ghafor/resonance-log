# resonance-log

My take on [Ali Abdaal](https://aliabdaal.com)'s resonance calendar: a record of the writing that has actually changed how I work as a product manager, kept current so it stays a tool rather than a graveyard of bookmarks.

## The rule

Anything that resonates goes in. No exception. In Abdaal's words:

> "anytime I come across anything at all that resonates with me, I drop it into my Resonance Calendar on Notion."

Source: [Using Notion as a Resonance Calendar](https://aliabdaal.com/newsletter/using-notion-as-a-resonance-calendar/)

What I have changed: this is a git repo rather than Notion, entries are categorised by skill area, format and learning stage, and each carries a one-line lesson kept separate from the reason it resonated. An `.ics` feed resurfaces one entry on a cadence, so I actually go back to them.

## The index

The full reading list, grouped by skill area and by month, is in [`INDEX.md`](INDEX.md). It is generated from `entries.yaml` by `render_index.py`.

## Structure

- `entries.yaml`: one entry per resource. Schema in `docs/one-pager.md`.
- `templates/`: blank templates taken from entries, ready to copy. So far: an opportunity solution tree.
- `docs/one-pager.md`: what this is for, the scope, and how I will know it worked.
- `render_index.py`: reads `entries.yaml` and writes the grouped list into `INDEX.md` between the `INDEX:START` / `INDEX:END` markers.
- `render_ics.py`: reads `entries.yaml` and writes `resonance.ics`, one all-day event a week for each entry marked `revisit: true`.

## Subscribe to the feed

In your calendar app, add a calendar by URL and paste:

```
https://raw.githubusercontent.com/amina-ghafor/resonance-log/main/resonance.ics
```

In Google Calendar that is Other calendars, then From URL. In Apple Calendar it is File, then New Calendar Subscription. Each week one entry comes back with its lesson and link.

## Status

v1 done: the entries file, the rendered index and the `.ics` feed. After adding an entry, run `python render_index.py` and `python render_ics.py`.
