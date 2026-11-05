"""Generate resonance.ics from entries.yaml.

Run: python render_ics.py

Turns every entry marked `revisit: true` into an all-day calendar event, one a
week, in the order the entries appear in entries.yaml. Subscribe to the raw URL
of resonance.ics in any calendar app to get one entry back each week.
"""

import hashlib
from datetime import date, timedelta
from pathlib import Path

from render_index import load_entries

ICS_FILE = Path("resonance.ics")

# The first event lands on this date, then one a week after it. Kept fixed, not
# "today", so re-running the script gives the same dates and the file only
# changes when entries change.
START_DATE = date(2026, 11, 9)


def escape(text):
    """Escape the characters the calendar format treats as special.

    Backslash first, so the backslashes added for the others are not doubled.
    """
    return (
        str(text)
        .replace("\\", "\\\\")
        .replace(";", "\\;")
        .replace(",", "\\,")
        .replace("\n", "\\n")
    )


def fold(line):
    """Split a long line into 75-byte pieces, as the calendar format requires.

    Each continuation piece starts with a space, which is how calendar apps know
    to join it back on. Splits on whole characters so an accented letter is
    never cut in half.
    """
    pieces = []
    current = ""
    limit = 75
    for char in line:
        if len((current + char).encode("utf-8")) > limit:
            pieces.append(current)
            current = " "
            limit = 75
        current += char
    pieces.append(current)
    return "\r\n".join(pieces)


def event_uid(entry):
    """A stable ID per entry, built from its URL.

    Calendar apps use the ID to recognise an event they already have, so an
    edited entry updates in place rather than appearing twice.
    """
    digest = hashlib.sha1(entry["url"].encode("utf-8")).hexdigest()[:16]
    return f"{digest}@resonance-log"


def schedule(entries, start=START_DATE):
    """Pair each entry to revisit with its date: start, then a week apart.

    Entries with `revisit: false` are skipped. An entry with no revisit field
    counts as true.
    """
    to_revisit = [e for e in entries if e.get("revisit", True)]
    return [(start + timedelta(weeks=i), e) for i, e in enumerate(to_revisit)]


def render_event(entry, day):
    """The lines for one all-day event: title, lesson and link."""
    description = f"{entry['tldr']}\n\nWhy it resonated: {entry.get('why', '')}\n\n{entry['url']}"
    lines = [
        "BEGIN:VEVENT",
        f"UID:{event_uid(entry)}",
        f"DTSTAMP:{entry['date_found'].strftime('%Y%m%d')}T000000Z",
        f"DTSTART;VALUE=DATE:{day.strftime('%Y%m%d')}",
        f"DTEND;VALUE=DATE:{(day + timedelta(days=1)).strftime('%Y%m%d')}",
        f"SUMMARY:{escape('Revisit: ' + entry['title'])}",
        f"DESCRIPTION:{escape(description)}",
        f"URL:{entry['url']}",
        "TRANSP:TRANSPARENT",
        "END:VEVENT",
    ]
    return lines


def render_ics(entries, start=START_DATE):
    """Turn the entries into the full text of the .ics file."""
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//amina-ghafor//resonance-log//EN",
        "CALSCALE:GREGORIAN",
        "X-WR-CALNAME:Resonance log",
    ]
    for day, entry in schedule(entries, start):
        lines.extend(render_event(entry, day))
    lines.append("END:VCALENDAR")
    # The format wants Windows-style line endings, including after the last line.
    return "\r\n".join(fold(line) for line in lines) + "\r\n"


def main():
    entries = load_entries()
    text = render_ics(entries)
    # newline="" stops Python changing the \r\n line endings on write.
    with open(ICS_FILE, "w", newline="") as f:
        f.write(text)
    print(f"Wrote {len(schedule(entries))} events to {ICS_FILE}")


if __name__ == "__main__":
    main()
