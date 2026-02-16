class GardenError(Exception):
    """Base exception class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-specific health issues."""
    def __init__(self, plant: str) -> None:
        self.message = f"The {plant} plant is wilting!"
        super().__init__(self.message)


class WaterError(GardenError):
    """Exception raised when irrigation system fails."""
    def __init__(self) -> None:
        self.message = "Not enough water in the tank!"
        super().__init__(self.message)


def test_custom_errors() -> None:
    """Demonstrates raising and catching
    custom garden exceptions."""
    print("=== Custom Garden Errors Demo ===\n")

    tank_fill: bool = False
    wilting: bool = False

    try:
        print("Testing PlantError...")
        if wilting is False:
            raise PlantError("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    try:
        print("Testing WaterError...")
        if tank_fill is False:
            raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        if tank_fill is False or wilting is False:
            raise PlantError("tomato")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        if tank_fill is False or wilting is False:
            raise WaterError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
