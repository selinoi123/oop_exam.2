from functools import wraps
from exceptions import DeckCheatingError

"""
בודק האם חפיסה שנוצרה אקראית באמת שונה בכל הרצה.
אם שתי הפעלות של הפונקציה מחזירות אותן חפיסות – תיזרק error DeckCheatingError.
"""


def fair_deck(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        first_deck = func(*args, **kwargs)
        second_deck = func(*args, **kwargs)

        first_cards = list(first_deck.cards)
        second_cards = list(second_deck.cards)

        if first_cards == second_cards:
            raise DeckCheatingError("Deck is not shuffled properly – same order in two calls.")

        return first_deck

    return wrapper
