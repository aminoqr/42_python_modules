from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from typing import List, Dict
from random import shuffle

class Deck:
    def __init__(self,) -> None:
        self.cards: List[Card] = []
    
    def add_card(self, card: Card) -> None:
        self.cards.append(card)
    
    def shuffle(self) -> None:
        shuffle(self.cards)
    
    def draw_card(self) -> Card | None:
        if not self.cards:
            return None
        return self.cards.pop()
    
    def get_deck_stats(self) -> Dict:
        cc_count = 0
        ac_count = 0
        sc_count = 0
        total_cost = 0
        for i in self.cards:
            if isinstance(i, CreatureCard):
                cc_count += 1
            elif isinstance(i, ArtifactCard):
                ac_count += 1
            elif isinstance(i, SpellCard):
                sc_count += 1
            total_cost += i.cost
        
        avg = total_cost/len(self.cards) if self.cards else 0.0
        return {
            "total_cards": len(self.cards),
            "creatures": cc_count,
            "spells": sc_count,
            "artifacts": ac_count,
            "avg_cost": avg
        }
    
    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False
            