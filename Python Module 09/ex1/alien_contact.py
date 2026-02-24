from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = Field(False)

    @model_validator(mode='after')
    def check_business_rues(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.TELEPATHIC and \
                self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 "
                             "witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include "
                             "received messages")

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("========================================")

    valid_data = {
        "contact_id": "AC_2024_001",
        "timestamp": "2024-06-15T14:30:00",
        "location": "Area 51, Nevada",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": False
    }

    try:
        contact = AlienContact(**valid_data)
        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")

        print("\n========================================")

        print("Expected validation error:")
        invalid_data = valid_data.copy()
        invalid_data.update({
            "contact_id": "AC_2024_002",
            "contact_type": "telepathic",
            "witness_count": 1
        })

        AlienContact(**invalid_data)

    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
