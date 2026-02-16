import random
from typing import List
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard


class Deck ():
    """A container class that manages a collection of game cards."""
    def __init__(self):
        """Initialize an empty list to store card objects."""
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a valid card object to the end of the deck."""
        if isinstance(card, Card):
            self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Find and remove a card by its name, returning True if successful."""
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Randomly rearrange the order of cards currently in the deck."""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Remove and return the top card from the deck."""
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        """Calculate and return statistics
        about the deck's composition and costs."""
        if not self.cards:
            return {
                'Status': "Empty Deck"
            }

        total_cost = 0
        for card in self.cards:
            if isinstance(card, SpellCard):
                stats['spells'] += 1
            elif isinstance(card, CreatureCard):
                stats['creatures'] += 1
            elif isinstance(card, ArtifactCard):
                stats['artifacts'] += 1

            total_cost += card.cost
            stats['avg_cost'] = total_cost / len(self.cards)

        stats = {
            'total_cards': len(self.cards),
            'creatures': 0,
            'spells': 0,
            'artifacts': 0,
            'avg_cost': 0.0
        }
        return stats
