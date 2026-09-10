"""Generate INDEX.md from entries.yaml.

Run: python render_index.py

Reads every entry in entries.yaml, builds a Markdown reading list, and writes it
into INDEX.md between the INDEX:START / INDEX:END markers. Nothing else in
INDEX.md is touched.
"""

from pathlib import Path

import yaml

ENTRIES_FILE = Path("entries.yaml")
INDEX_FILE = Path("INDEX.md")
START_MARKER = "<!-- INDEX:START -->"
END_MARKER = "<!-- INDEX:END -->"

# Fields every entry must have for the renderer to work.
REQUIRED_FIELDS = ("title", "url", "source", "date_found", "skill_area", "tldr")


def load_entries(path=ENTRIES_FILE):
    """Parse the YAML file into a list of entry dicts and check each one has the
    fields the renderer needs.

    A dict may also carry: format, stage, why, quotes (list), revisit (bool).
    """
    with open(path) as f:
        entries = yaml.safe_load(f)

    for position, entry in enumerate(entries, start=1):
        missing = [field for field in REQUIRED_FIELDS if field not in entry]
        if missing:
            name = entry.get("title", "untitled")
            raise ValueError(
                f"entry {position} ({name}) is missing: {', '.join(missing)}"
            )

    return entries


def group_by(entries, key):
    """Bucket entries into {group_value: [entries]}.

    `key` is a function that takes one entry dict and returns the string to
    group it under. setdefault creates the list the first time a value is seen.
    """
    groups = {}
    for entry in entries:
        groups.setdefault(key(entry), []).append(entry)
    return groups


def entry_line(entry):
    """One Markdown list item: linked title, source in italics, the lesson."""
    return f"- [{entry['title']}]({entry['url']}). *{entry['source']}.* {entry['tldr']}"


def render_section(heading, groups, newest_first=False):
    """Render one view: a `##` heading, then a `###` sub-heading per group key
    with that group's entries listed under it.

    Keys are sorted so runs are stable. `newest_first` reverses that order, for
    the by-month view where the latest month should come first.
    """
    lines = [f"## {heading}", ""]
    for key in sorted(groups, reverse=newest_first):
        lines.append(f"### {key}")
        lines.append("")
        for entry in groups[key]:
            lines.append(entry_line(entry))
        lines.append("")
    return "\n".join(lines).strip()


def render_index(entries):
    """Turn the list of entry dicts into the Markdown that goes in INDEX.md.

    Two views of the same entries: one grouped by skill area, one grouped by
    the month each entry was found.
    """
    by_skill = group_by(entries, lambda e: e["skill_area"])
    skill_view = render_section("By skill area", by_skill)

    # Sort entries newest-first before grouping, so within each month the latest
    # entry comes first. PyYAML parses `date_found: 2026-09-05` as a date object,
    # so format it back to a "YYYY-MM" string rather than slicing.
    newest_first = sorted(entries, key=lambda e: e["date_found"], reverse=True)
    by_month = group_by(newest_first, lambda e: e["date_found"].strftime("%Y-%m"))
    month_view = render_section("By month", by_month, newest_first=True)

    return skill_view + "\n\n" + month_view


def write_between_markers(generated, path=INDEX_FILE, start=START_MARKER, end=END_MARKER):
    """Replace the text between the two marker lines in `path` with `generated`.

    Everything before and including the start marker, and everything from the
    end marker onward, is kept as-is.
    """
    text = path.read_text()
    if start not in text or end not in text:
        raise ValueError(f"{path} is missing the {start} / {end} markers")

    before = text.split(start)[0]
    after = text.split(end)[1]
    path.write_text(f"{before}{start}\n{generated}\n{end}{after}")


def main():
    entries = load_entries()
    generated = render_index(entries)
    write_between_markers(generated)
    print(f"Wrote {len(entries)} entries to {INDEX_FILE}")


if __name__ == "__main__":
    main()
