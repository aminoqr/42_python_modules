from Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("Cost must be more than 0!!!")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be more than 0!!!")
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be more than 0!!!")
        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"]= self.health
        return info
    
    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt" : self.attack,
            "combat_resolved": True
        }