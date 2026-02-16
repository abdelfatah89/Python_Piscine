from abc import ABC, abstractmethod


class Magical(ABC):
    """Interface defining the essential magical
    capabilities for cards and entities."""
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Execute a specific spell effect on a list of targets."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Modify the internal mana reserves of the magical entity."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Return a dictionary containing current
        mana and magic-related attributes."""
        pass
