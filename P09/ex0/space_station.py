import pydantic
from datetime import datetime
from typing import Optional


class SpaceStation(pydantic.BaseModel):
    station_id: str = pydantic.Field(min_length=3, max_length=10)
    name: str = pydantic.Field(min_length=1, max_length=50)
    crew_size: int = pydantic.Field(ge=1, le=20)
    power_level: float = pydantic.Field(ge=0.0, le=100.0)
    oxygen_level: float = pydantic.Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = pydantic.Field(default=None, max_length=200)


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

    # --- Test avec les données valides ---
    print("=" * 50)
    print("TEST DONNÉES VALIDES")
    print("=" * 50)

    try:
        station = SpaceStation(**VALID_DATA)
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(
            f"Status: "
            f"{'Operational' if station.is_operational else 'Not operational'}"
        )
    except pydantic.ValidationError as e:
        print(f"[KO] Station : {VALID_DATA.get('name', '?')}")
        for err in e.errors():
            print(f"     -> {err['loc'][0]}: {err['msg']}")

    # --- Test avec les données invalides ---
    print("\n" + "=" * 50)
    print("TEST DONNÉES INVALIDES")
    print("=" * 50)

    invalid = {
        "station_id": "TOOLONG123456",
        "name": "Test Station",
        "crew_size": 25,
        "power_level": 85.0,
        "oxygen_level": 92.0,
        "last_maintenance": "2024-01-15T10:30:00",
        "is_operational": True,
    }

    try:
        station = SpaceStation(**invalid)
        print(f"[OK] Station {1}: {station.name} — aucune erreur détectée")
    except pydantic.ValidationError as errors:
        print(f"{errors.errors()[0]['input']}: {errors.errors()[0]['msg']}")


if __name__ == "__main__":
    main()
