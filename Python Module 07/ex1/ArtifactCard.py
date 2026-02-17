from ex0.Card import Card

class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect_type}"
        }
    
    def activate_ability(self) -> dict:
        if self.durability > 0:
            self.durability -= 1
            success = True
        else:
            success = False
        return {
            "artifact": self.name,
            "ability_activated": success,
            "remaining_durability": self.durability,
            "power_effect": self.effect_type
        }