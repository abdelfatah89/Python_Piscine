from ex0.Card import Card


class ArtifactCard (Card):
    """A card representing a persistent artifact
    with limited durability."""
    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int, effect: str):
        """Initialize artifact with specific
        durability and persistent effect."""
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("Durability must be a positive integer")

        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict = None) -> dict:
        """Deploy the artifact to the field and return
        its deployment status."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'type': 'Artifact',
            'status': 'Deployed',
            'durability': self.durability
        }

    def activate_ability(self) -> dict:
        """Trigger the artifact's effect
        and decrease its remaining durability."""
        if self.durability > 0:
            self.durability -= 1
            return {
                'artifact': self.name,
                'action': 'Ability activated',
                'remaining_durability': self.durability,
                'effect_triggered': self.effect
            }
        else:
            return {
                'artifact': self.name,
                'action': 'Failed',
                'reason': 'Artifact is broken (0 durability)'
            }
