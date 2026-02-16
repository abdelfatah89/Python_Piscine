def check_temperature(temp_str: str) -> None:
    try:
        temp = int(temp_str)
        if 0 <= temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    temp_str = input("Testing temperature: ")
    check_temperature(temp_str)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
