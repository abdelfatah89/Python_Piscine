import sys


def command_quest() -> None:
    """Processes and displays command-line arguments
    while handling empty inputs safely."""
    argv_len: int = len(sys.argv)
    print("=== Command Quest ===")
    try:
        if argv_len == 1:
            raise ValueError("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        i = 1
        print(f"Arguments received: {argv_len - 1}")
        while i < argv_len:
            print("Argument {}: {}".format(i, sys.argv[i]))
            i += 1

    except ValueError as e:
        print(e)
        print(f"Program name: {sys.argv[0]}")
    finally:
        print(f"Total arguments: {argv_len}")


if __name__ == "__main__":
    command_quest()
