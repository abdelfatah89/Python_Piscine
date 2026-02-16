def garden_operations(error: str) -> None:
    """Triggers specific built-in Python exceptions
    for demonstration."""
    if error == "value":
        int("abc")
    elif error == "div":
        1 / 0
    elif error == "file":
        open("missing.txt")
    elif error == "key":
        dict_test = {"id_0": 1}
        print(dict_test["missing_plant"])


def test_error_types() -> None:
    """Tests and catches various garden-related
    error types gracefully."""
    print("=== Garden Error Types Demo ===\n")

    # Testing ValueError
    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    # Testing ZeroDivisionError
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("div")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    # Testing FileNotFoundError
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    # Testing KeyError
    print("\nTesting KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    # Testing Multiple Errors
    print("\nTesting multiple errors together...")
    try:
        garden_operations("value")
        garden_operations("div")
        garden_operations("file")
        garden_operations("key")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
