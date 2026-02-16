from pydantic import BaseModel, model_validator, Field, ValidationError
from datetime import datetime
from enum import Enum


class CrewRole(str, Enum):
    COMMANDER = "commander"
    CAPTAIN = "captain"
    LIEUTENANT = "lieutenant"
    OFFICER = "officer"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRole
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = False


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember]
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_mission(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        leaders = any(member.rank in [CrewRole.COMMANDER, CrewRole.CAPTAIN]
                      for member in self.crew)
        if not leaders:
            raise ValueError(
                "Mission must have at least one Commander or Captain")

        if self.duration_days > 365:
            exp_count = sum(1 for m in self.crew if m.years_experience >= 5)
            if exp_count < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) need 50% \
experienced crew (5+ years)")

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def display_info(valid_mission: SpaceMission):
    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    for m in valid_mission.crew:
        print(f" - {m.name} ({m.rank.value}) - {m.specialization}")


def main():
    print("Space Mission Crew Validation")
    print("=" * 41)

    try:
        crew1 = CrewMember(
            member_id="CMD01", name="Sarah Connor",
            rank=CrewRole.COMMANDER, age=45,
            specialization="Mission Command", years_experience=15,
            is_active=True
            )

        crew2 = CrewMember(
            member_id="NAV02", name="John Smith",
            rank=CrewRole.LIEUTENANT, age=32,
            specialization="Navigation", years_experience=8,
            is_active=True
            )

        crew3 = CrewMember(
            member_id="ENG03", name="Alice Johnson",
            rank=CrewRole.OFFICER, age=28,
            specialization="Engineering", years_experience=6,
            is_active=True
            )

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars", launch_date=datetime.now(),
            duration_days=900, budget_millions=2500.0,
            crew=[crew1, crew2, crew3]
        )

        display_info(mission)

    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err['msg'])

    try:
        print("\n", "=" * 41)

        crew4 = CrewMember(
            member_id="OFF01", name="Casual Bob",
            rank=CrewRole.OFFICER, age=25,
            specialization="Cleaning", years_experience=1,
            is_active=True
            )

        invalid_mission = SpaceMission(
            mission_id="M2024_BAD", mission_name="Unauthorized Mission",
            destination="Moon", launch_date=datetime.now(),
            duration_days=100, budget_millions=500.0,
            crew=[crew4]
        )
        display_info(invalid_mission)
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
