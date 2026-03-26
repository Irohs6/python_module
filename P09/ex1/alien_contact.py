try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ImportError:
    print(
        "Pydantic library is not installed. Please install it using 'pip "
        "install pydantic' and try again."
    )
    exit(1)

from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def custom_contact_validation(self):
        if self.contact_id.startswith("AC"):
            return self
        raise ValueError("contact_id must start with 'AC'")

    @model_validator(mode="after")
    def custom_contact_type_validation(self):
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        return self

    @model_validator(mode="after")
    def custom_signal_validator(self):
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) must include a received message"
            )
        return self


def main():
    print("=" * 50)
    print("Alien Contact Log Validation")
    print("=" * 50)

    data = [
        {
            "contact_id": "AC_2024_001",
            "timestamp": "2024-01-20T00:00:00",
            "location": "Atacama Desert, Chile",
            "contact_type": "visual",
            "signal_strength": 9.6,
            "duration_minutes": 99,
            "witness_count": 11,
            "message_received": "Greetings from Zeta Reticuli",
            "is_verified": False,
        },
        {
            "contact_id": "AC_2024_002",
            "timestamp": "2024-08-20T00:00:00",
            "location": "Mauna Kea Observatory, Hawaii",
            "contact_type": "radio",
            "signal_strength": 5.6,
            "duration_minutes": 152,
            "witness_count": 6,
            "message_received": None,
            "is_verified": True,
        },
        {
            "contact_id": "_2024_001",
            "timestamp": "2024-01-20T00:00:00",
            "location": "Atacama Desert, Chile",
            "contact_type": "visual",
            "signal_strength": 9.6,
            "duration_minutes": 0,
            "witness_count": 11,
            "message_received": "Greetings from Zeta Reticuli",
            "is_verified": False,
        },
        {
            "contact_id": "AC_2024_002",
            "timestamp": "2024-08-20T00:00:00",
            "location": "Ma",
            "contact_type": "",
            "signal_strength": 5.6,
            "duration_minutes": 152,
            "witness_count": 0,
            "message_received": None,
            "is_verified": True,
        },
    ]

    print("Valid contact report:")

    for i, alien in enumerate(data):
        try:
            alien = AlienContact(**alien)
            print(f"Alien {i+1} ID:({alien.contact_id})")
            print(f"Type: {alien.contact_type.value}")
            print(f"Location: {alien.location}")
            print(f"Signal Strength: {alien.signal_strength}")
            print(f"Duration: {alien.duration_minutes} minutes")
            print(f"Witness Count: {alien.witness_count}")
            print(f"Message Received: {alien.message_received}\n")
        except ValidationError as errors:
            print("\n" + "=" * 50)
            print("Invalid contact reports:")
            print("=" * 50)
            for error in errors.errors():
                field = error["loc"][0] if error["loc"] else ""
                print(f"[KO] alien {i+1}: {field}: {error['msg']}")
            print()


if __name__ == "__main__":
    main()
