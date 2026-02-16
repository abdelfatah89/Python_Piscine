from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Abstract interface for defining
    player behaviors and decision-making logic."""
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Analyze game state to select a card
        to play and determine actions."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the unique identifier
        string for the strategy."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Sort potential targets based
        on the strategy's tactical priorities."""
        pass
