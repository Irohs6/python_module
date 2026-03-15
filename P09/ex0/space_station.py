import pydantic
from datetime import datetime
from typing import Optional


class SpaceStation(pydantic.BaseModel):
    station_id: str = pydantic.Field(min_length=3, max_length=10)  # 3-10 characters
    name: str = pydantic.Field(min_length=1, max_length=50)
    crew_size: int = pydantic.Field(ge=1, le=20)  # 1-20 people
    power_level: float = pydantic.Field(ge=0.0, le=100.0)  # 0.0-100.0 percent
    oxygen_level: float = pydantic.Field(ge=0.0, le=100.0)  # 0.0-100.0 percent
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = pydantic.Field(default=None, max_length=200)


def main():
    import json
    import os

    base_dir = os.path.dirname(os.path.abspath(__file__))

    # --- Test avec les données valides ---
    print("=" * 50)
    print("TEST DONNÉES VALIDES (space_stations.json)")
    print("=" * 50)
    with open(os.path.join(base_dir, "space_stations.json"), "r") as f:
        valid_data = json.load(f)

    for i, data in enumerate(valid_data):
        try:
            station = SpaceStation(**data)
            print(f"[OK] Station {i+1}: {station.name} ({station.station_id})")
        except pydantic.ValidationError as e:
            print(f"[KO] Station {i+1}: {data.get('name', '?')}")
            for err in e.errors():
                print(f"     -> {err['loc'][0]}: {err['msg']}")

    # --- Test avec les données invalides ---
    print("\n" + "=" * 50)
    print("TEST DONNÉES INVALIDES (invalid_stations.json)")
    print("=" * 50)
    with open(os.path.join(base_dir, "invalid_stations.json"), "r") as f:
        invalid_data = json.load(f)

    for i, data in enumerate(invalid_data):
        try:
            station = SpaceStation(**data)
            print(f"[OK] Station {i+1}: {station.name} — aucune erreur détectée")
        except pydantic.ValidationError as e:
            print(
                f"[KO] Station {i+1}: {data.get('name', '?')} — {e.error_count()} erreur(s)"
            )
            for err in e.errors():
                print(f"     -> {err['loc'][0]}: {err['msg']}")


if __name__ == "__main__":
    main()
