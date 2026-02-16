from pydantic import BaseModel, ValidationError, Field
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(max_length=200)


def display_info(station: SpaceStation) -> None:
    print(f"{'=' * 40}\nValid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size}")
    print(f"Power: {station.power_level}")
    print(f"Oxygen: {station.oxygen_level}")
    print(f"Status: "
          f"{'Operational' if station.is_operational else 'Not Operational'}")
    if station.notes:
        print(f"Notes: {station.notes}")


def main():
    try:
        station1 = SpaceStation(
            station_id="ADS514",
            name="Abdelfatah Laktaoui",
            crew_size=20,
            power_level=15.7,
            oxygen_level=78.1,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes=""
            )
        display_info(station1)

        station2 = SpaceStation(
            station_id="ADS514",
            name="Abdelfatah Laktaoui",
            crew_size=25,
            power_level=15.7,
            oxygen_level=78.1,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes=""
            )
        display_info(station2)

    except ValidationError as e:
        print(f"\n{'=' * 40}\nExpected validation error:")
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
