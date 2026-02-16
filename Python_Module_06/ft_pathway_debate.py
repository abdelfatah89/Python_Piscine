import alchemy
from alchemy.transmutation import lead_to_gold
from alchemy.transmutation import stone_to_gem
from alchemy.transmutation import philosophers_stone
from alchemy.transmutation import elixir_of_life


def main():
    print("\n=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")

    print("\nTesting Package Access:")
    print("alchemy.transmutation.lead_to_gold(): {}".format(
        alchemy.transmutation.lead_to_gold()))
    print("alchemy.transmutation.philosophers_stone(): {}".format(
        alchemy.transmutation.philosophers_stone()))

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
