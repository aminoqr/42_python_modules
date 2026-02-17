from ex0.CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")
    card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(f"Creature Card: {card.get_card_info()}\n")
    print("Playing Fire Dragon with 6 mana available:")
    is_possible = card.is_playable(6)
    print(f"Playable: {is_possible}")
    result = card.play({})
    print(f"Play result: {result}\n")

    print(f"{card.name} attacks Goblin Warrior:")
    print(f"Attack result: {card.attack_target('Goblin Warrior')}\n")

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {card.is_playable(3)}\n")

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
