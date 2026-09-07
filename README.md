# resonance-calendar

A record of the writing that has actually changed how I work as a product manager, kept current so it stays a tool rather than a graveyard of bookmarks.

## The rule

Anything that resonates goes in. No exception. The concept is Ali Abdaal's:

> "anytime I come across anything at all that resonates with me, I drop it into my Resonance Calendar on Notion."

Source: [Using Notion as a Resonance Calendar](https://aliabdaal.com/newsletter/using-notion-as-a-resonance-calendar/)

What I have changed: this is a git repo rather than Notion, entries are categorised by skill area, format and learning stage, and each carries a one-line lesson kept separate from the reason it resonated. An `.ics` feed resurfaces one entry on a cadence, so the calendar cycles back instead of only recording dates.

## Structure

- `entries.yaml`: one entry per resource. Schema in `docs/one-pager.md`.
- `docs/one-pager.md`: what this is for, the scope, and how I will know it worked.
- An index rendered from the entries, grouped by skill area. Not built yet.
- An `.ics` generator. Not built yet.

## Status

v1 in progress. The entries file and this README exist. The index renderer and the `.ics` generator are still to write.
