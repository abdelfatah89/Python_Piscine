class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, plant: str = None) -> None:
        self.message = "Plant name cannot be empty!"
        super().__init__(self.message)


class NotValidPlant(GardenError):
    def __init__(self) -> None:
        self.message = "Cannot water None - invalid plant!"
        super().__init__(self.message)


class WaterError(GardenError):
    def __init__(self) -> None:
        self.message = "Not enough water in tank"
        super().__init__(self.message)


class Plant:
    def __init__(self, name: str) -> None:
        """Initializes a new Plant instance."""
        self.name = name


class GardenManager:
    def __init__(self, name: str) -> None:
        self.name = name
        self.plants = []

    """Adds a new plant to the manager with
    validation for empty names."""
    def add_plant(self, name: str) -> None:
        try:
            if name is None:
                raise PlantError
            a = Plant(name)
            self.plants.append(a)
            print(f"Added {name} successfully")
        except PlantError as e:
            print(e)
        except ValueError as e:
            print(f"Error adding plant: {e}")

    """Simulates irrigation while ensuring system
    cleanup via finally block."""
    def water_plants(self) -> None:
        try:
            print("\nOpening watering system")
            for plant in self.plants:
                if plant is None:
                    raise NotValidPlant()
                print(f"Watering {plant.name} - success")
        except NotValidPlant as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    """Validates health metrics and raises
    specific errors for invalid values."""
    def check_plant_health(self, name: str, water: int, sun: int) -> None:
        try:
            if name is None:
                raise ValueError("Plant name cannot be empty!")

            if water > 10:
                raise ValueError(f"Water level {water} is too high (max 10)")

            if sun < 2:
                raise ValueError("Sunlight hours {} is too low (min 2)".format(
                    sun))

            print(f"{name}: healthy (water: {water}, sun: {sun})")
        except ValueError as e:
            print(f"Error checking {name}: {e}")


def test_garden_system() -> None:
    """Demonstrates the full integration of error
    handling in the garden system."""
    print("=== Garden Management System ===")
    Alice = GardenManager("Alice")

    print("\nAdding plants to garden...")
    Alice.add_plant("tomato")
    Alice.add_plant("lettuce")
    Alice.add_plant(None)

    Alice.water_plants()

    print("Checking plant health...")
    Alice.check_plant_health("tomato", 5, 8)
    Alice.check_plant_health("lettuce", 15, 8)

    try:
        print("\nTesting error recovery...")
        tank_fill = False
        if tank_fill is False:
            raise WaterError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")


if __name__ == "__main__":
    test_garden_system()
