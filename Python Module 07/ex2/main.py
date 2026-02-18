from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.EliteCard import EliteCard
from ex2.Magical import Magical


def main():
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    card_methods = [method for method in Card.__dict__ if
                    not method.startswith("_")]
    com_methods = [method for method in Combatable.__dict__
                   if not method.startswith("_")]
    magical_methods = [method for method in Magical.__dict__ if
                       not method.startswith("_")]

    print(f"- Card: {card_methods}")
    print(f"- Combatable: {com_methods}")
    print(f"- Magical: {magical_methods}")

    arcane = EliteCard("Arcane Warrior", 4, "Legendary", 3, 5, 10, 8)

    print(f"\nPlaying {arcane.name} (Elite Card):\n")

    print("Combat phase:")
    print(f"Attack result: {arcane.attack('Enemy')}")
    print(f"Defense result: {arcane.defend(5)}\n")

    print("Magic phase:")
    print(f"Spell cast: {arcane.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {arcane.channel_mana(3)}\n")

    print("Multiple interface implementation succesful!")


if __name__ == "__main__":
    main()
