from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officier = "ofiicier"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=100000.0)

    @model_validator(mode='after')
    def custom_mision_id_validator(self):
        if self.mission_id.startswith('M'):
            return self

    @model_validator(mode='after')
    def custom_crew_validator(self):
        for member in self.crew:
            if member.rank == Rank.captain or Rank.commander:
                return self
        raise ValueError("Has not a valid crew")

    @model_validator(mode='after')
    def custom_duration_validator(self):
        for member in self.crew:
            if member.years_experience > 5 and self.duration_days > 365:
                return self
        raise ValueError("Has not a valid crew")

    def custom_member_active_validator(self):
        for member in self.crew:
            if member.is_active:
                return self
        raise ValueError("Has not a valid crew")


def main():
    import json
    import os

    base_dir = os.path.dirname(os.path.abspath(__file__))

    # --- Test avec les données valides ---
    print("=" * 50)
    print("TEST DONNÉES VALIDES (space_missions.json)")
    print("=" * 50)
    with open(os.path.join(base_dir, "space_missions.json"), "r") as f:
        valid_data = json.load(f)

    for i, data in enumerate(valid_data):
        try:
            space_mission = SpaceMission(**data)
            print(f"[OK] mission {i+1}:({space_mission.mission_id})")
        except ValidationError as e:
            print(f"[KO] mission {i+1}: {data.get('mission_id', '?')}")
            for err in e.errors():
                print(f"     -> {err}")

    # --- Test avec les données invalides ---
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
