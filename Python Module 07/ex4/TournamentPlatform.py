import random
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self) -> None:
        self._cards: dict[str, TournamentCard] = {}
        self._matches_played: int = 0
        self._match_history: list[dict] = []
        self._card_counter: int = 0

    def register_card(self, card: TournamentCard) -> str:
        self._card_counter += 1
        card_type = card.name.lower().replace(" ", "_")
        card_id = f"{card_type}_{self._card_counter:03d}"

        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self._cards:
            raise ValueError(f"Card {card1_id} not registered")
        if card2_id not in self._cards:
            raise ValueError(f"Card {card2_id} not registered")

        card1 = self._cards[card1_id]
        card2 = self._cards[card2_id]

        card1.reset_for_match()
        card2.reset_for_match()

        card1_power = (card1.attack_power + card1.health +
                       random.randint(0, 10))
        card2_power = (card2.attack_power + card2.health +
                       random.randint(0, 10))

        if card1_power >= card2_power:
            winner_id, loser_id = card1_id, card2_id
            winner, loser = card1, card2
        else:
            winner_id, loser_id = card2_id, card1_id
            winner, loser = card2, card1

        winner.update_wins(1)
        loser.update_losses(1)

        self._matches_played += 1

        match_result = {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

        self._match_history.append(match_result)
        return match_result

    def get_leaderboard(self) -> list:
        leaderboard = []

        for card_id, card in self._cards.items():
            rank_info = card.get_rank_info()
            leaderboard.append({
                "id": card_id,
                "name": card.name,
                "rating": rank_info["rating"],
                "record": rank_info["record"]
            })

        leaderboard.sort(key=lambda x: x["rating"], reverse=True)

        for i, entry in enumerate(leaderboard, 1):
            entry["position"] = i

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self._cards)
        total_ratings = sum(card.calculate_rating()
                            for card in self._cards.values())
        avg_rating = total_ratings / total_cards if total_cards > 0 else 0

        return {
            "total_cards": total_cards,
            "matches_played": self._matches_played,
            "avg_rating": round(avg_rating, 2),
            "platform_status": "active" if total_cards > 0 else "inactive"
        }

    def get_card(self, card_id: str) -> TournamentCard | None:
        return self._cards.get(card_id)
