from tools.card_generator import CardGenerator
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


def main():
    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    generator = CardGenerator()

    creature = generator.get_creature("Fire Dragon")
    if creature is not None:
        creature_obj = CreatureCard(**creature)

    artifact = generator.get_artifact("Mana Crystal")
    if artifact is not None:
        artifact_obj = ArtifactCard(**artifact)

    spell = generator.get_spell("Lightning Bolt")
    if spell is not None:
        spell_obj = SpellCard(**spell)

    deck = Deck()
    deck.add_card(creature_obj)
    deck.add_card(artifact_obj)
    deck.add_card(spell_obj)
    print(f"Deck stats: {deck.get_deck_stats()}\n")

    print("Drawing and playing cards:\n")

    card1 = deck.draw_card()
    card2 = deck.draw_card()
    card3 = deck.draw_card()
    if card1 is not None:
        print(f"Drew: {card1.name} ({card1.card_type})")
        print(f"Play result: {card1.play({})}\n")

    if card2 is not None:
        print(f"Drew: {card2.name} ({card2.card_type})")
        print(f"Play result: {card2.play({})}\n")

    if card3 is not None:
        print(f"Drew: {card3.name} ({card3.card_type})")
        print(f"Play result: {card3.play({})}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
