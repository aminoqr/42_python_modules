from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import List
from datetime import datetime


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field("planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation_rules(self) -> 'SpaceMission':
        # Rule 1: Mission ID check
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        # Rule 2: Leadership check
        # We look for ANY member who is a Captain or Commander
        has_leader = any(member.rank in [Rank.CAPTAIN, Rank.COMMANDER]
                         for member in self.crew)
        if not has_leader:
            raise ValueError("Mission must have at least one Commander or "
                             "Captain")

        # Rule 3: Experience check for long missions
        if self.duration_days > 365:
            experienced_count = sum(1 for member in self.crew if
                                    member.years_experience >= 5)
            if experienced_count < len(self.crew) / 2:
                raise ValueError("Long missions (> 365 days) need 50%"
                                 "experienced crew (5+ years)")

        # Rule 4: Active status check
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("========================================")

    # 1. Prepare valid crew data
    # We ensure at least one Commander/Captain and all are active
    crew_list = [
        CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=40,
            specialization="Mission Command",
            years_experience=15
        ),
        CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=32,
            specialization="Navigation",
            years_experience=8
        ),
        CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=28,
            specialization="Engineering",
            years_experience=6
        )
    ]

    try:
        # 2. Create a valid mission
        mission_data = {
            "mission_id": "M2024_MARS",
            "mission_name": "Mars Colony Establishment",
            "destination": "Mars",
            "launch_date": "2024-12-01T10:00:00",
            "duration_days": 900,
            "crew": crew_list,
            "budget_millions": 2500.0
        }
        mission = SpaceMission(**mission_data)

        # 3. Display the valid mission info
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value}) "
                  "- {member.specialization}")

        print("\n========================================")
        print("Expected validation error:")

        # 4. Trigger the Leadership Error
        # Creating a mission with NO Captain or Commander
        invalid_crew = [
            CrewMember(
                member_id="CM004",
                name="James Holden",
                rank=Rank.OFFICER,
                age=30,
                specialization="Pilot",
                years_experience=4
            )
        ]
        mission_data["crew"] = invalid_crew
        SpaceMission(**mission_data)

    except ValidationError as e:
        # Extract the specific message to match the required output style
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
