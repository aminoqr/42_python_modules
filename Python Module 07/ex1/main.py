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
    creature_obj = CreatureCard(**creature)
    spell = generator.get_spell("Lightning Bolt")
    artifact = generator.get_artifact("Mana Crystal")
    deck = Deck()
    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)

if __name__ == "__main__":
    main()