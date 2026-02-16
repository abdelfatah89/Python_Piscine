from pydantic import BaseModel, model_validator, Field, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_alien_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0:
            if not self.message_received:
                raise ValueError(
                    "Strong signals (> 7.0) should include received messages")

        return self


def display_info(contact: AlienContact) -> None:
    print(f"{'=' * 40}\nAlien Contact Log Validation")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witness: {contact.witness_count}")
    print(f"Message: '{contact.message_received}'")


def main():
    try:
        contact1 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
            )
        display_info(contact1)

        contact2 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Gre   etings from Zeta Reticuli",
            is_verified=True
            )
        display_info(contact2)

    except ValidationError as e:
        print(f"\n{'=' * 40}\nExpected validation error:")
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
