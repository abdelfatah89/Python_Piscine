from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:
    print("\n=== DataDeck Game Engine ===")
    engine = GameEngine()
    strategy = AggressiveStrategy()
    factory = FantasyCardFactory()

    print("\nConfiguring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    cards_types = {
        'creatures': {s.name for s in engine.raw_deck.get("creatures")},
        'spells': {s.name for s in engine.raw_deck.get("spells")},
        'artifacts': {s.name for s in engine.raw_deck.get("artifacts")}
        }
    print(f"Available types: {cards_types}")

    print("\nSimulating aggressive turn...")
    raw_hand = [c.name for c in engine.player_hand]
    hand = {f"{c} ({raw_hand.count(c)})" for c in raw_hand}
    print(f"Hand: {list(hand)}")

    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {engine.simulate_turn().get("details").get("action")}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
