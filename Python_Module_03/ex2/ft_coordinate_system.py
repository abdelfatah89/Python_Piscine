import sys
import math


def calculate_distance(position: tuple) -> None:
    """Calculates and prints the Euclidean distance
    gti from the origin (0,0,0) to a 3D position."""
    x, y, z = position
    float(x), float(y), float(z)
    result = math.sqrt((x-0)**2 + (y-0)**2 + (z-0)**2)
    print(f"Distance between (0, 0, 0) and {position}: {result:.2f}")


def creating(position: tuple) -> None:
    """Formats and displays the initial creation of a 3D position
    and its distance."""
    print(f"\nPosition created: {position}")
    calculate_distance(position)


def unpacking(splitted: str, unpack: bool = False) -> tuple:
    """Demonstrates how to break down a 3D coordinate
    tuple into individual axis values."""
    splitted = splitted.split(",")
    x = int(splitted[0])
    y = int(splitted[1])
    z = int(splitted[2])
    if unpack:
        print("\nUnpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    return (x, y, z)


def parsing(str_position: str) -> None:
    """Outputs the results of converting a raw string
    input into structured numeric data."""
    try:
        position = unpacking(str_position)
        print(f"\nParsing coordinates: \"{str_position}\"")
        print(f"Parsed position: {position}")
        calculate_distance(position)
    except ValueError as e:
        print(f"\nParsing invalid coordinates: \"{str_position}\"")
        print("Error parsing coordinates: ", e)
        print(f"Error details - Type: ValueError, Args: (\"{e}\",)")


def ft_coordinate_system() -> None:
    """Manages the lifecycle of processing 3D coordinates
    from input to mathematical analysis."""
    print("=== Game Coordinate System ===")

    if len(sys.argv) > 1:
        parsing(sys.argv[1])

    creating((10, 20, 5))
    parsing("3,4,0")
    parsing("abc,def,ghi")
    unpacking("3,4,0", True)


if __name__ == "__main__":
    ft_coordinate_system()
