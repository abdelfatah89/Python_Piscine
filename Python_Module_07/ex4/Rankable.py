from abc import ABC, abstractmethod


class Rankable(ABC):
    """Simple ranking interface for tracking tournament performance."""
    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return the current rating of the card."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Increment the win count."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Increment the loss count."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Return a dictionary with ranking details."""
        pass
