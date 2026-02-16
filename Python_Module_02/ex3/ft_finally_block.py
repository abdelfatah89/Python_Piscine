def water_plants(plant_list) -> None:
    """Simulates watering plants and ensures
    system cleanup using finally."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
    else:
        print("Watering completed successfully!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Tests the watering system with both
    valid and invalid plant lists."""
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])

    print("\nTesting with error...")
    water_plants(["tomato", None])

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
