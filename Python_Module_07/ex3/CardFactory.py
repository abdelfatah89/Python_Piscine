from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract interface for producing themed card sets and decks."""
    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create and return a new creature card instance."""
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create and return a new spell card instance."""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create and return a new artifact card instance."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Generate a dictionary containing a balanced set of themed cards."""
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Return metadata about the card types this factory can produce."""
        pass
