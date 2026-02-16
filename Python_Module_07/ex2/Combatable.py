from abc import ABC, abstractmethod


class Combatable(ABC):
    """Interface defining mandatory physical combat
    behaviors for game entities."""
    @abstractmethod
    def attack(self, target) -> dict:
        """Calculate and return the results of an
        offensive strike against a target."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Process incoming damage through defensive
        attributes and update health."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Provide a dictionary containing current
        offensive and defensive metrics."""
        pass
