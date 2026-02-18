from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, armor: int,
                 attack_power: int, health: int, mana_pool: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.mana_pool = mana_pool
        self.armor = armor

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.armor, incoming_damage)
        actual_damage = incoming_damage - blocked

        self.armor -= blocked
        self.health -= actual_damage

        is_alive = self.health > 0
        return {
            "defender": self.name,
            "damage_taken": actual_damage,
            "damage_blocked": blocked,
            "still_alive": is_alive
        }

    def get_combat_stats(self) -> dict:
        return {
            "power": self.attack_power,
            "health": self.health,
            "armor": self.armor
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict | None:
        if self.cost <= self.mana_pool:
            self.mana_pool -= self.cost
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": targets,
                "mana_used": self.cost
            }
        return None

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool
        }

    def get_magic_stats(self) -> dict:
        return {
            "cast_cost": self.cost,
            "mana_pool": self.mana_pool
        }

    def play(self, game_state: dict) -> dict:
        return {
            "event": "card played",
            "card_name": self.name,
            "rarity": self.rarity,
            "combat_stats": self.get_combat_stats(),
            "magic_stats": self.get_magic_stats()
        }
