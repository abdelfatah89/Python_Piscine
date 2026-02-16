from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """focusing on creature deployment and direct hero damage."""
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Play a creature if possible,
        otherwise any card, and attack."""
        if not hand:
            return {
                'strategy': self.get_strategy_name(),
                'status': 'No cards to play'
            }

        card_played = None
        for i, card in enumerate(hand):
            if hasattr(card, 'attack'):
                card_played = hand.pop(i)
                break
        if not card_played:
            card_played = hand.pop(0)
        battlefield.append(card_played)

        available_targets = ["Enemy 1", "Enemy Hero", "Enemy 2"]
        targets = self.prioritize_targets(available_targets)
        if hasattr(card_played, 'attack'):
            action = card_played.attack_target(targets[0])
        else:
            action = card_played.play()

        return {
            'strategy': self.get_strategy_name(),
            'card_played': card_played.name,
            'action': action
        }

    def get_strategy_name(self) -> str:
        """Return the strategy identity string."""
        return "Aggressive Strategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """Move 'Enemy Hero' to the top of the priority list."""
        if "Enemy Hero" in available_targets:
            available_targets.remove("Enemy Hero")
            available_targets.insert(0, "Enemy Hero")
            return available_targets
        return available_targets
