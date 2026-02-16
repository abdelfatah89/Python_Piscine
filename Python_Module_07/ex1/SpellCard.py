from ex0.Card import Card


class SpellCard (Card):
    """A card representing a one-time magical
    effect that resolves and expires."""
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        """Initialize spell with its name,
        cost, rarity, and specific effect type."""
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict = None) -> dict:
        """Trigger the spell's play sequence
        and return its activation details."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'type': 'Spell',
            'effect_activated': self.effect_type
        }

    def resolve_effect(self, targets: list) -> dict:
        """Apply the spell's effect to a list
        of valid targets and return a log."""
        results = []
        for target in targets:
            if self.effect_type == "heal":
                if hasattr(target, "health"):
                    target.health += 5
                    results.append(f"{target.name} healed")
            elif self.effect_type == "durable":
                if hasattr(target, "durability"):
                    target.durability += 1
                    results.append(f"{target.name} durability increased")

        return {
            'Spell': self.name,
            'effect': self.effect_type,
            'targets_affected': len(results),
            'log': results
        }
