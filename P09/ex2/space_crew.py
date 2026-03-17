
try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ImportError:
    print("Pydantic library is not installed. Please install it using 'pip "
          "install pydantic' and try again.")
    exit(1)

from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
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
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def custom_mision_id_validator(self):
        if self.mission_id.startswith('M'):
            return self
        raise ValueError(f"mission_id '{self.mission_id}' must start with 'M'")

    @model_validator(mode='after')
    def custom_crew_validator(self):
        for member in self.crew:
            if member.rank in (Rank.captain, Rank.commander):
                return self
        raise ValueError("The crew must include at least one "
                         "captain or commander")

    @model_validator(mode='after')
    def custom_duration_validator(self):
        veterant_member = 0
        if self.duration_days > 365:
            for member in self.crew:
                if member.years_experience >= 5:
                    veterant_member += 1
            if veterant_member >= len(self.crew) / 2:
                return self
            raise ValueError("Missions longer than 1 year require at least "
                             "half of the crew to have 5 or more years of "
                             "experience")

        return self

    @model_validator(mode='after')
    def custom_member_active_validator(self):
        for member in self.crew:
            if member.is_active:
                return self
        raise ValueError("The crew must include at least one active member")


def main():

    print("=" * 50)
    print("Space Mission Crew Validation")
    print("=" * 50)

    VALID__DATA = {
        "mission_id": "M2024_TITAN",
        "mission_name": "Solar Observatory Research Mission",
        "destination": "Solar Observatory",
        "launch_date": "2024-03-30T00:00:00",
        "duration_days": 451,
        "crew": [
            {
                "member_id": "CM001",
                "name": "Sarah Williams",
                "rank": "captain",
                "age": 43,
                "specialization": "Mission Command",
                "years_experience": 19,
                "is_active": True
            },
            {
                "member_id": "CM002",
                "name": "James Hernandez",
                "rank": "captain",
                "age": 43,
                "specialization": "Pilot",
                "years_experience": 30,
                "is_active": True
            },
            {
                "member_id": "CM003",
                "name": "Anna Jones",
                "rank": "cadet",
                "age": 35,
                "specialization": "Communications",
                "years_experience": 15,
                "is_active": True
            },
            {
                "member_id": "CM004",
                "name": "David Smith",
                "rank": "commander",
                "age": 27,
                "specialization": "Security",
                "years_experience": 15,
                "is_active": True
            },
            {
                "member_id": "CM005",
                "name": "Maria Jones",
                "rank": "cadet",
                "age": 55,
                "specialization": "Research",
                "years_experience": 30,
                "is_active": True
            }
        ],
        "mission_status": "planned",
        "budget_millions": 2208.1
    },

    print("Valid mission created:")
    for i, data in enumerate(VALID__DATA):
        try:
            space_mission = SpaceMission(**data)
            print(f"Mission {i+1}: {space_mission.mission_name}")
            print(f"ID:({space_mission.mission_id})")
            print(f"Destination: {space_mission.destination}")
            print(f"Duration: {space_mission.duration_days} days")
            print(f"Budget: ${space_mission.budget_millions}M")
            print(f"Crew size: {len(space_mission.crew)}")
            print("Crew members:")
            for member in space_mission.crew:
                print(f"  - {member.name} ({member.rank.value}) "
                      f"- {member.specialization}")
        except ValidationError as e:
            print(f"[KO] mission {i+1}: {data.get('mission_id', '?')}")
            for err in e.errors():
                print(f"     -> {err}")

    print("\n" + "=" * 50)
    print("Expected validation error:")
    print("=" * 50)
    INVALID__DATA = {
        "mission_id": "M2024_TITAN",
        "mission_name": "Solar Observatory Research Mission",
        "destination": "Solar Observatory",
        "launch_date": "2024-03-30T00:00:00",
        "duration_days": 3600,
        "crew": [
            {
                "member_id": "CM0",
                "name": "Sarah Williams",
                "rank": "cadet",
                "age": 43,
                "specialization": "Mission Command",
                "years_experience": 19,
                "is_active": True
            },
            {
                "member_id": "CM002",
                "name": "James Hernandez",
                "rank": "cadet",
                "age": 43,
                "specialization": "Pilot",
                "years_experience": 30,
                "is_active": False
            },
            {
                "member_id": "CM003",
                "name": "Anna Jones",
                "rank": "commander",
                "age": 35,
                "specialization": "Communications",
                "years_experience": 50,
                "is_active": True
            },
            {
                "member_id": "CM004",
                "name": "Da",
                "rank": "cadet",
                "age": 27,
                "specialization": "Security",
                "years_experience": 15,
                "is_active": False
            },
            {
                "member_id": "CM005",
                "name": "Maria Jones",
                "rank": "cadet",
                "age": 55,
                "specialization": "Research",
                "years_experience": 30,
                "is_active": True
            }
        ],
        "mission_status": "planned",
        "budget_millions": 2208.1
    },
    for i, data in enumerate(INVALID__DATA):
        try:
            space_mission = SpaceMission(**data)
            print(f"Mission {i+1}: {space_mission.mission_name}")
            print(f"ID:({space_mission.mission_id})")
            print(f"Destination: {space_mission.destination}")
            print(f"Duration: {space_mission.duration_days} days")
            print(f"Budget: ${space_mission.budget_millions}M")
            print(f"Crew size: {len(space_mission.crew)}")
            print("Crew members:")
            for member in space_mission.crew:
                print(f"  - {member.name} ({member.rank.value}) "
                      f"- {member.specialization}")
        except ValidationError as errors:
            print(f"[KO] mission {i+1}: {data.get('mission_id', '?')}")
            for error in errors.errors():
                field = error['loc'][0] if error['loc'] else ""
                print(f"     -> {field}: {error['msg']}")
            print()


if __name__ == "__main__":
    main()
