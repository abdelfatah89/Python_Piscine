from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard


def main():
    print("\n=== DataDeck Deck Builder ===")

    deck = Deck()
    spell = SpellCard("Lightning Bolt", 3,
                      "Legendary", "Deal 3 damage to target")
    artifact = ArtifactCard("Mana Crystal", 2,
                            "Legendary", 8, "Permanent: +1 mana per turn")
    creature = CreatureCard("Fire Dragon", 5,
                            "Legendary", 4, 7)

    cards = [spell, artifact, creature]
    for card in cards:
        deck.add_card(card)

    print("\nBuilding deck with different card types...")
    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:")
    deck.shuffle()
    for card in deck.cards:
        print("\nDrew:", card.name)
        print("Play result:", card.play())

    print("\nPolymorphism in action: \
Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
