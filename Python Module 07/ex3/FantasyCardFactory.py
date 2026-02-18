from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "Dragon":
            return CreatureCard("Red Dragon", 7, "Legendary", 8, 10)
        elif name_or_power == "Gobliin":
            return CreatureCard("Goblin", 2, "Common", 2, 2)
        else:
            return CreatureCard("Beast", 1, "Common", 1, 1)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "Meteor":
            return SpellCard("Meteor", 8, "Legendary", "damage")
        elif name_or_power == "Ice Shard":
            return SpellCard("Ice Shard", 2, "Common", "damage")
        else:
            return SpellCard("Shield Spell", 1, "Common", "buff")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "Crown of Kings":
            return ArtifactCard("Crown of Kings", 7, "Legendary", 8,
                                "Permanent: +1 cost reduction to all cards")
        elif name_or_power == "Cloak of Shadows":
            return ArtifactCard("Cloak of Shadows", 3, "Uncommon", 3,
                                "Permanent: Creatures have stealth")
        else:
            return ArtifactCard("Mana Crystal", 2, "Common", 5,
                                "Permanent: +1 mana per turn")

    def create_themed_deck(self, size: int) -> dict:
        card_list = []
        for i in range(size):
            if i % 3 == 0:
                card_list.append(self.create_creature())
            elif i % 3 == 1:
                card_list.append(self.create_artifact())
            else:
                card_list.append(self.create_spell())

        return {
            "theme": "Fantasy",
            "size": len(card_list),
            "cards": card_list
        }

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["Dragon", "Gobliin", "Beast"],
            "spells": ["Meteor", "Ice Shard", "Shield Spell"],
            "artifacts": ["Crown of Kings", "Cloak of Shadows", "Mana Crystal"]
        }
