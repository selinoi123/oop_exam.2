import random
from card import Card
from card_suit import CardSuit
from card_rank import CardRank
from deck_contract import AbstractDeck


class Deck(AbstractDeck):
    """
    מחלקה המייצגת חפיסת קלפים .
    מאפשרת יצירה, ערבוב, שליפה, והוספה, ממש כמו משחק אמיתי .
    """

    def __init__(self, shuffle=True):
        """
        יוצר את החפיסה עם כל הקלפים האפשריים שיצרנו.
        , ומערבב את החפיסה מיד לאחר היצירה.
        """

        self._cards = [Card(suit, rank) for suit in CardSuit for rank in CardRank]
        if shuffle:
            self.shuffle()

    def shuffle(self):
        """
        מערבב את הקלפים בחפיסה בצורה אקראית.
         """
        random.shuffle(self._cards)

    def draw(self):
        """
        שולף את הקלף הראשון מהחפיסה.
         """
        return self._cards.pop(0) if self._cards else None

    def add_card(self, card):
        """
         מוסיף קלף לחפיסה.
          אם הפרמטר אינו קלף יופיע error.
        """
        if isinstance(card, Card):
            self._cards.append(card)
        else:
            raise TypeError("Only Card objects can be added.")

    @property
    def cards(self):
        """
         מחזיר את כל הקלפים בחפיסה כטופל.
          """
        return tuple(self._cards)

    def __len__(self):
        """
         מחזיר את מספר הקלפים הנוכחי בחפיסה.
           """
        return len(self._cards)

    def __getitem__(self, index):
        """
        מאפשר גישה לקלפים לפי אינדקס.
        """
        return self._cards[index]

    def __iter__(self):
        """
        מאפשר איטרציה על כל הקלפים בחפיסה.
        """
        return iter(self._cards)
