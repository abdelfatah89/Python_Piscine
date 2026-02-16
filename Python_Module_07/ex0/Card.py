from abc import ABC, abstractmethod


class Card(ABC):
    """
    Abstract base class representing the template for all game cards.
    """
    def __init__(self, name: str, cost: int, rarity: str):
        """
        Initialize card with its name, mana cost, and rarity level.
        """
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """
        Execute the card's specific gameplay logic based on current state.
        """
        pass

    def get_card_info(self) -> dict:
        """Return a dictionary containing the card's primary attributes."""
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """Check if the provided mana is sufficient to play this card."""
        return available_mana >= self.cost
