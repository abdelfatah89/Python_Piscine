def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """Validates plant metrics and raises ValueError
    for invalid data."""
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(" Sunlight hours {} is too low (min 2)".format(
            sunlight_hours))

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Demonstrates error raising and handling
    for various health scenarios."""
    print("=== Garden Plant Health Checker ===")
    try:
        print("\nTesting good values...")
        print(check_plant_health("tomato", 5, 7))
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("\nTesting empty plant name...")
        print(check_plant_health("", 5, 7))
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("\nTesting bad water level...")
        print(check_plant_health("tomato", 15, 4))
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("\nTesting bad sunlight hours...")
        print(check_plant_health("tomato", 5, 0))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
