from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def __init__(self) -> None:
        self.total_damage_dealt = 0
        self.cards_played = 0

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        actions = {
            "cards_played": [],
            "mana_used": 0,
            "targets_attacked": [],
            "damage_dealt": 0
        }

        sorted_hand = sorted(hand, key=lambda card: card.cost)
        available_mana = 10

        for card in sorted_hand:
            if card.cost <= available_mana:
                actions["cards_played"].append(card.name)
                actions["mana_used"] += card.cost
                available_mana -= card.cost
                self.cards_played += 1

                if hasattr(card, 'attack'):
                    actions["damage_dealt"] += card.attack
                    actions["targets_attacked"].append("Enemy Player")
                    self.total_damage_dealt += card.attack

        return actions

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        prioritized = []

        for target in available_targets:
            if isinstance(target, str):
                if target.lower() in ["player", "enemy player"]:
                    prioritized.append(target)

        remaining = [t for t in available_targets if t not in prioritized]

        def get_health(target):
            if hasattr(target, 'health'):
                return target.health
            return float('inf')

        remaining.sort(key=get_health)
        prioritized.extend(remaining)

        return prioritized
