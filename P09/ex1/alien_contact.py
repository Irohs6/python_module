from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContactModel(BaseModel):
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
        raise ValueError(f"{self.contact_id} must start with 'AC'")

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
    import json
    import os

    base_dir = os.path.dirname(os.path.abspath(__file__))

    # --- Test avec les données valides ---
    print("=" * 50)
    print("TEST DONNÉES VALIDES (alien_contacts.json)")
    print("=" * 50)
    with open(os.path.join(base_dir, "alien_contacts.json"), "r") as f:
        valid_data = json.load(f)

    for i, data in enumerate(valid_data):
        try:
            alien = AlienContactModel(**data)
            print(f"[OK] alien {i+1}:({alien.contact_id})")
        except ValidationError as e:
            print(f"[KO] alien {i+1}: {data.get('contatc_id', '?')}")
            for err in e.errors():
                print(f"     -> {err}")

    # --- Test avec les données invalides ---
    print("\n" + "=" * 50)
    print("TEST DONNÉES INVALIDES (invalid_contacts.json)")
    print("=" * 50)
    with open(os.path.join(base_dir, "invalid_contacts.json"), "r") as f:
        invalid_data = json.load(f)

    for i, data in enumerate(invalid_data):
        try:
            alien = AlienContactModel(**data)
            print(
                f"[OK] alien {i+1}: {alien.contact_id} — aucune erreur détectée"
            )
        except ValidationError as e:
            print(
                f"[KO] alien {i+1}: {data.get('contact_id', '?')} — {e.error_count()} erreur(s)"
            )
            for err in e.errors():
                loc = err["loc"][0] if err["loc"] else "model"
                print(f"     -> {loc}: {err['msg']}")


if __name__ == "__main__":
    main()
