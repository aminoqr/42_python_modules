from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self) -> None:
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._hand: list = []
        self._battlefield: list = []
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self._factory = factory
        self._strategy = strategy
        self._hand = []
        self._hand.append(self._factory.create_creature("Dragon"))
        self._hand.append(self._factory.create_creature("Gobliin"))
        self._hand.append(self._factory.create_spell("Meteor"))
        self._cards_created = 3

    def simulate_turn(self) -> dict:
        if self._factory is None or self._strategy is None:
            raise ValueError("Engine not configured.")

        turn_result = self._strategy.execute_turn(
            self._hand, self._battlefield)

        self._turns_simulated += 1
        self._total_damage += turn_result.get("damage_dealt", 0)

        return {
            "strategy": self._strategy.get_strategy_name(),
            "actions": turn_result,
            "turn_number": self._turns_simulated
        }

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self._turns_simulated,
            "strategy_used": (self._strategy.get_strategy_name()
                              if self._strategy else None),
            "total_damage": self._total_damage,
            "cards_created": self._cards_created,
            "factory_configured": self._factory is not None,
            "strategy_configured": self._strategy is not None
        }

    def get_hand(self) -> list:
        return self._hand

    def add_card_to_hand(self, card) -> None:
        self._hand.append(card)
        self._cards_created += 1
