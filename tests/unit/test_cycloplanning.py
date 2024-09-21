import ics
from datetime import datetime, timedelta
from cycloplanning import HEADERS, Event, create_ics, parse_html, parse_events


def test_parse_html(cycloplanning_html):
    res = parse_html(cycloplanning_html)
    assert len(res) == 2
    assert all(k in res[0] for k in HEADERS)


def test_parse_events():
    # Given
    expected_event = Event(
        name="Lave-kambouis",
        start_date=datetime(2024, 9, 16, 19),
        duration=timedelta(hours=2),
        location="15 rue Pierre Bonnard",
        attendees=["Kévin", "", "Tur from Ivry", "Leighton"],
        description="Ouvert à tous.tes",
    )
    raw_events = [
        {
            "Jour": "Lundi",
            "Date": "16/09",
            "Quoi": "Lave-kambouis",
            "Adresse": "15 rue Pierre Bonnard",
            "Besoins Humains": "Ouvert à tous.tes",
            "Horaires": "19h - 21h",
            "Bénévole 1": "Kévin",
            "Bénévole 2": "",
            "Bénévole 3": "Tur from Ivry",
            "Bénévole 4": "Leighton",
        }
    ]
    # When
    events = parse_events(raw_events)
    # Then
    assert events[0] == expected_event


def test_create_ics():
    # Given
    events = [
        Event(
            name="Lave-kambouis",
            start_date=datetime(2024, 9, 16, 19),
            duration=timedelta(hours=2),
            location="15 rue Pierre Bonnard",
            attendees=["Kévin", "", "Tur from Ivry", "Leighton"],
            description="Ouvert à tous.tes",
        )
    ]
    # When
    calendar = create_ics(events)
    # Then
    assert isinstance(calendar, ics.Calendar)
    assert len(calendar.events) == len(events)
    assert list(calendar.events)[0].name == events[0].name
