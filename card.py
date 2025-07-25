from card_suit import CardSuit
from card_rank import CardRank
from card_contract import AbstractCard


class Card(AbstractCard):
    """
    מחלקה המייצגת קלף יחיד בחפיסה.
    כל קלף מורכב מסוג ודירוג .
    """
    def __init__(self, suit: CardSuit, rank: CardRank):
        """
        בונה קלף חדש עם סוג ודירוג מסוימים.
         עם (suit and rank)
        """
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        """
        מחזיר את סוג הקלף.
        מסוג CardSuit.
        """
        return self._suit

    @property
    def rank(self):
        """
        מחזיר את דירוג הקלף.
        מסוג CardRank.
        """
        return self._rank

    def get_display_name(self):
        """
        מחזיר שם תצוגה של הקלף, לדוגמה: "Queen of Hearts".
        """
        return f"{self.rank.display_name} of {self.suit.display_name}"

    def __eq__(self, other):
        """
        בדיקת שוויון בין שני קלפים.
אז יחזיר True אם הסוג והדירוג זהים.
        """
        return isinstance(other, Card) and self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        """
        השוואה לפי עוצמת דירוג קודם, ואם שווה אז לפי עוצמת סוג.
        : יחזיר True אם הקלף הנוכחי קטן מהשני.
        """
        if self.rank.strength < other.rank.strength:
            return True
        elif self.rank.strength == other.rank.strength:
            return self.suit.strength < other.suit.strength
        return False

    def __gt__(self, other):
        """
        השוואה לפי עוצמת דירוג קודם, ואם שווה אז לפי עוצמת סוג.
        :אז יחזיר: True אם הקלף הנוכחי גדול מהשני.
        """
        if self.rank.strength > other.rank.strength:
            return True
        elif self.rank.strength == other.rank.strength:
            return self.suit.strength > other.suit.strength
        return False

    def __hash__(self):
        """
        מחזיר hash לקלף, מבוסס על סוג ודירוג.
        """
        return hash((self.suit, self.rank))

    def __str__(self):
        """
        מחזיר מחרוזת תיאור של הקלף (לתצוגה).
        """
        return self.get_display_name()

    def __repr__(self):
        """
        מחזיר ייצוג טכני של הקלף, לשימוש במפתחים.
        """
        return f"Card({self.suit}, {self.rank})"