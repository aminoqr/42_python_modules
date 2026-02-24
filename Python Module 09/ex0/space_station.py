from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(True)
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    try:
        print("\nSpace Station Data Validation")
        print("========================================")
        print("Valid station created:")
        valid_data = {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 6,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": "2024-01-01T12:00:00"
        }
        station = SpaceStation(**valid_data)
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print("Status: ", end="")
        print("Operational\n") if station.is_operational else \
            print("Not Operational\n")
        print("========================================")
        invalid_data = {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 25,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": "2024-01-01T12:00:00"
        }
        print("Expected validation error:")
        station2 = SpaceStation(**invalid_data)
        print(f"ID: {station2.station_id}")
        print(f"Name: {station2.name}")
        print(f"Crew: {station2.crew_size} people")
        print(f"Power: {station2.power_level}%")
        print(f"Oxygen: {station2.oxygen_level}%")
        print("Status: ", end="")
        print("Operational\n") if station2.is_operational else \
            print("Not Operational\n")

    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
