import random
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


class GameEngine():
    """Manages game state, card deck, and turn execution."""
    def __init__(self):
        """Initialize engine with empty collections
        and turn counter."""
        self.factory = FantasyCardFactory()
        self.strategy = None
        self.deck = []
        self.raw_deck = []
        self.player_hand = []
        self.battlefield = []
        self.turn_count = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Setup factory, strategy,
        and draw initial hand of 3 cards."""
        self.factory = factory
        self.strategy = strategy
        self.raw_deck = self.factory.create_themed_deck(30)
        self.deck = (self.raw_deck.get("creatures", [])
                     + self.raw_deck.get("spells", [])
                     + self.raw_deck.get("artifacts", []))
        random.shuffle(self.deck)
        for i in range(3):
            if self.deck:
                card = self.deck.pop(0)
                self.player_hand.append(card)
        self.battlefield = []
        self.turn_count = 0

    def simulate_turn(self) -> dict:
        """Execute a single turn and return action details."""
        if not self.strategy:
            return {"error": "Strategy not configured."}

        self.turn_count += 1
        turn_result = self.strategy.execute_turn(
            self.player_hand, self.battlefield)
        return {
            'turn_number': self.turn_count,
            'details': turn_result
        }

    def get_engine_status(self) -> dict:
        """Return current turn count and component sizes."""
        return {
            'turns_simulated': self.turn_count,
            'strategy_used': self.strategy.get_strategy_name(),
            'hand_size': len(self.player_hand),
            'battlefield_size': len(self.battlefield)
        }
