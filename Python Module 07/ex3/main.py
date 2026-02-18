from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("=== DataDeck Game Engine ===\n")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game...")
    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")

    available_types = factory.get_supported_types()
    print(f"Available types: {available_types}\n")

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Simulating aggressive turn...")
    hand = engine.get_hand()
    hand_display = ", ".join([f"{card.name} ({card.cost})" for card in hand])
    print(f"Hand: [{hand_display}]")

    print("\nTurn execution:")
    turn_result = engine.simulate_turn()
    print(f"Strategy: {turn_result['strategy']}")
    print(f"Actions: {turn_result['actions']}")

    print("\nGame Report:")
    status = engine.get_engine_status()
    report = {
        'turns_simulated': status['turns_simulated'],
        'strategy_used': status['strategy_used'],
        'total_damage': status['total_damage'],
        'cards_created': status['cards_created']
    }
    print(report)

    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility!")


if __name__ == "__main__":
    main()
