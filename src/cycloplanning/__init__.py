import pytz
from dataclasses import dataclass
from datetime import datetime, timedelta
from collections.abc import Iterable
from bs4 import BeautifulSoup
import requests
import ics
import logging

LOGGER = logging.getLogger(__name__)

# Define column headers
HEADERS = [
    "Jour",
    "Date",
    "Quoi",
    "Adresse",
    "Besoins Humains",
    "Horaires",
    "Bénévole 1",
    "Bénévole 2",
    "Bénévole 3",
    "Bénévole 4",
]


@dataclass
class Event:
    name: str
    start_date: datetime
    duration: timedelta
    location: str
    description: str
    attendees: list[str]


def get_html(url: str) -> str:
    response = requests.get(url)
    return response.content


def parse_html(html: str) -> Iterable[dict]:
    soup = BeautifulSoup(html, "html.parser")

    # Find the header row to start processing
    header_row = soup.find("td", string=lambda x: x and "Date" in x)
    if header_row:
        # Iterate over each subsequent <tr> for data extraction
        for row in header_row.parent.find_next_siblings("tr"):
            # Get all <td> elements in the row
            columns = row.find_all("td")

            # Create a dictionary for the row using headers as keys
            row_dict = {
                HEADERS[i]: col.get_text(strip=True)
                for i, col in enumerate(columns[: len(HEADERS)])
            }

            # Skip header rows
            if row_dict["Jour"] == "Date":
                continue

            yield row_dict


def parse_events(raw_events: Iterable[dict]) -> Iterable[Event]:
    for raw_event in raw_events:
        try:
            start_date = datetime.strptime(raw_event["Date"], "%d/%m")
        except ValueError:
            LOGGER.exception(f"Could not parse date for event {raw_event}, skipping.")
            continue
        start_date = start_date.replace(year=datetime.today().year)
        start_date = start_date.replace(tzinfo=pytz.timezone("Europe/Paris"))
        try:
            hour_begin = int(raw_event["Horaires"].split("-")[0].split("h")[0])
            hour_end = int(raw_event["Horaires"].split("-")[1].split("h")[0])
            duration = timedelta(hours=(hour_end - hour_begin))
        except (ValueError, IndexError):
            LOGGER.exception(
                f"Could not parse hour for event {raw_event}, setting default."
            )
            hour_begin = 0
            duration = 24
        finally:
            start_date = start_date.replace(hour=hour_begin)
        attendees = [
            raw_event["Bénévole 1"],
            raw_event["Bénévole 2"],
            raw_event["Bénévole 3"],
            raw_event["Bénévole 4"],
        ]

        event = Event(
            name=raw_event["Quoi"],
            description=raw_event["Besoins Humains"],
            start_date=start_date,
            duration=duration,
            location=raw_event["Adresse"],
            attendees=attendees,
        )
        yield event


def create_ics(raw_events: list[Event]) -> ics.Calendar:
    calendar = ics.Calendar()
    for raw_event in raw_events:
        event = ics.Event(
            name=raw_event.name,
            description=raw_event.description,
            begin=raw_event.start_date,
            duration=raw_event.duration,
            location=raw_event.location,
            attendees=raw_event.attendees,
        )
        calendar.events.add(event)
    return calendar


def write_ics(calendar: ics.Calendar, output="/dev/stdout"):
    with open(output, "w") as f:
        f.writelines(calendar.serialize_iter())
