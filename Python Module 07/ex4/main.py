from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...")

    dragon = TournamentCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5,
        armor=2,
        base_rating=1200
    )

    wizard = TournamentCard(
        name="Ice Wizard",
        cost=4,
        rarity="Rare",
        attack=4,
        health=6,
        armor=1,
        base_rating=1150
    )

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    print(f"\n{dragon.name} (ID: {dragon_id}):")
    print("  - Interfaces: ['Card', 'Combatable', 'Rankable']")
    print(f"  - Rating: {dragon.calculate_rating()}")
    rank_info = dragon.get_rank_info()
    print(f"  - Record: {rank_info['record']}")

    print(f"\n{wizard.name} (ID: {wizard_id}):")
    print("  - Interfaces: ['Card', 'Combatable', 'Rankable']")
    print(f"  - Rating: {wizard.calculate_rating()}")
    rank_info = wizard.get_rank_info()
    print(f"  - Record: {rank_info['record']}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for entry in leaderboard:
        print(f"  {entry['position']}. {entry['name']} - "
              f"Rating: {entry['rating']} ({entry['record']})")

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
