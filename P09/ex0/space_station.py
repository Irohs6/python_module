try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError:
    print("Pydantic library is not installed. Please install it using 'pip "
          "install pydantic' and try again.")
    exit(1)

from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main():

    VALID_DATA = {
        "station_id": "LGW125",
        "name": "Titan Mining Outpost",
        "crew_size": 6,
        "power_level": 76.4,
        "oxygen_level": 95.5,
        "last_maintenance": "2023-07-11T00:00:00",
        "is_operational": True,
        "notes": None,
    }

    print("=" * 50)
    print("Space Station Data Validation")
    print("=" * 50)

    try:
        station = SpaceStation(**VALID_DATA)
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(f"Last Maintenance: {station.last_maintenance}")
        print(
            f"Status: "
            f"{'Operational' if station.is_operational else 'Not operational'}"
        )
    except ValidationError as errors:
        for error in errors.errors():
            print(f"{error['loc'][0]}: {error['msg']}")

    print("\n" + "=" * 50)
    print("Expected validation error:")
    print("=" * 50)

    invalid = {
        "station_id": "TOOLONG123456",
        "name": "Test Station",
        "crew_size": 0,
        "power_level": 150.0,
        "oxygen_level": -10.0,
        "last_maintenance": "2024-01-15T10:30:00",
        "is_operational": False,
    }

    try:
        station = SpaceStation(**invalid)
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(
            f"Status: "
            f"{'Operational' if station.is_operational else 'Not operational'}"
        )
    except ValidationError as errors:
        for error in errors.errors():
            print(f"{error['loc'][0]}: {error['msg']}")


if __name__ == "__main__":
    main()
