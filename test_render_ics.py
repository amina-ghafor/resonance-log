"""Tests for render_ics.py. Run: python -m pytest

Each test checks one promise the generator makes.
"""

from datetime import date

import render_ics as r


SAMPLE = [
    {"title": "First piece", "url": "https://example.com/a", "source": "Source A",
     "date_found": date(2026, 8, 1), "skill_area": "ai-tools", "tldr": "Lesson A.",
     "revisit": True},
    {"title": "Skipped piece", "url": "https://example.com/b", "source": "Source B",
     "date_found": date(2026, 9, 5), "skill_area": "ai-tools", "tldr": "Lesson B.",
     "revisit": False},
    {"title": "Second piece, with a comma", "url": "https://example.com/c", "source": "Source C",
     "date_found": date(2026, 9, 20), "skill_area": "design-ux", "tldr": "Lesson C.",
     "revisit": True},
]

START = date(2026, 11, 9)


def test_one_event_per_entry_to_revisit():
    """Entries marked revisit: false get no event."""
    output = r.render_ics(SAMPLE, START)
    assert output.count("BEGIN:VEVENT") == 2
    assert "Skipped piece" not in output


def test_events_are_a_week_apart():
    """The first event is on the start date, the next one seven days later."""
    days = [day for day, _ in r.schedule(SAMPLE, START)]
    assert days == [date(2026, 11, 9), date(2026, 11, 16)]


def test_event_is_titled_and_links_back():
    """Each event carries the resource title and its URL."""
    output = r.render_ics(SAMPLE, START)
    assert "SUMMARY:Revisit: First piece" in output
    assert "URL:https://example.com/a" in output


def test_special_characters_are_escaped():
    """A comma in a title is escaped, or calendar apps misread the line."""
    output = r.render_ics(SAMPLE, START)
    assert "Second piece\\, with a comma" in output


def test_no_line_is_longer_than_75_bytes():
    """Long lines are folded, as the calendar format requires."""
    long_entry = dict(SAMPLE[0], tldr="A very long lesson. " * 20)
    output = r.render_ics([long_entry], START)
    for line in output.split("\r\n"):
        assert len(line.encode("utf-8")) <= 75


def test_same_entries_give_the_same_file():
    """Running twice gives identical output, so the file only changes with the entries."""
    assert r.render_ics(SAMPLE, START) == r.render_ics(SAMPLE, START)
