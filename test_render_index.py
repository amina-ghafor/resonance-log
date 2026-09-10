"""Tests for render_index.py. Run: python -m pytest

Each test checks one promise the renderer makes.
"""

from datetime import date

import pytest

import render_index as r


# A small hand-made set of entries to test the grouping and rendering with,
# so the tests do not depend on what is currently in entries.yaml.
SAMPLE = [
    {"title": "Older ai-tools piece", "url": "https://example.com/a", "source": "Source A",
     "date_found": date(2026, 8, 1), "skill_area": "ai-tools", "tldr": "Lesson A."},
    {"title": "Newer ai-tools piece", "url": "https://example.com/b", "source": "Source B",
     "date_found": date(2026, 9, 5), "skill_area": "ai-tools", "tldr": "Lesson B."},
    {"title": "Design piece", "url": "https://example.com/c", "source": "Source C",
     "date_found": date(2026, 9, 20), "skill_area": "design-ux", "tldr": "Lesson C."},
]


def test_real_entries_file_loads_and_is_complete():
    """The actual entries.yaml parses and every entry has the required fields."""
    entries = r.load_entries()
    assert len(entries) > 0
    for entry in entries:
        for field in r.REQUIRED_FIELDS:
            assert field in entry


def test_missing_field_is_reported_by_name(tmp_path):
    """An entry missing a required field stops load_entries with a clear message."""
    bad_file = tmp_path / "entries.yaml"
    bad_file.write_text(
        "- title: No lesson here\n"
        "  url: https://example.com\n"
        "  source: Somewhere\n"
        "  date_found: 2026-09-01\n"
        "  skill_area: ai-tools\n"
    )
    with pytest.raises(ValueError) as caught:
        r.load_entries(bad_file)
    assert "tldr" in str(caught.value)
    assert "No lesson here" in str(caught.value)


def test_group_by_puts_entries_in_the_right_bucket():
    """group_by buckets entries under the value the key function returns."""
    groups = r.group_by(SAMPLE, lambda e: e["skill_area"])
    assert len(groups["ai-tools"]) == 2
    assert len(groups["design-ux"]) == 1


def test_render_index_contains_both_views():
    """The rendered page has a by-skill-area section and a by-month section."""
    output = r.render_index(SAMPLE)
    assert "## By skill area" in output
    assert "## By month" in output


def test_month_view_lists_newest_month_first():
    """In the by-month view, 2026-09 appears before 2026-08."""
    output = r.render_index(SAMPLE)
    assert output.index("### 2026-09") < output.index("### 2026-08")


def test_write_between_markers_leaves_the_rest_of_the_file_alone(tmp_path):
    """Only the text between the markers is replaced."""
    target = tmp_path / "INDEX.md"
    target.write_text(
        f"# Keep this heading\n\n{r.START_MARKER}\nold content\n{r.END_MARKER}\nkeep this footer\n"
    )
    r.write_between_markers("new content", path=target)
    result = target.read_text()
    assert "# Keep this heading" in result
    assert "keep this footer" in result
    assert "new content" in result
    assert "old content" not in result
