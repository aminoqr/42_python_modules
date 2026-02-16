from CreatureCard import CreatureCard

def main():
    print("\n=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Desgin:\n")
    card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(f"Deck stats: {card.get_card_info()}\n")
    print(f"Playing Fire Dragon with 6 mana available:")
    is_possible = card.is_playable(6)
    print(f"Playable: {is_possible}")
    result = card.play({})
    print(f"Play result: {result}\n")
    
    print("Playing Fire attacks Goblin Warrior:")
    print(f"{card.attack_target("Goblin Warrior")}\n")

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {card.is_playable(6)}\n")

    print("Abstract pattern successfully demonstrated!")

if __name__ == "__main__":
    main()