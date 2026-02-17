from ex0.Card import Card
from typing import List
from random import shuffle

class Deck:
    def __init__(self,) -> None:
        self.cards: List[Card] = []
    
    def add_card(self, card: Card) -> None:
        self.cards.append(card)
    
    def shuffle(self) -> None:
        shuffle(self.cards)
    
    def draw