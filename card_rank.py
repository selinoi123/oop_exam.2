from enum import Enum


class CardRank(Enum):
    """
    Enum שמייצג את דרגות הקלפים בחפיסה,
    """

    TWO = ("2", 2)
    THREE = ("3", 3)
    FOUR = ("4", 4)
    FIVE = ("5", 5)
    SIX = ("6", 6)
    SEVEN = ("7", 7)
    EIGHT = ("8", 8)
    NINE = ("9", 9)
    TEN = ("10", 10)
    JACK = ("Jack", 11)
    QUEEN = ("Queen", 12)
    KING = ("King", 13)
    ACE = ("Ace", 14)

    @property
    def display_name(self):
        """
        מחזיר את שם התצוגה של הדרגה .
        """
        return self.value[0]

    @property
    def strength(self):
        """
        מחזיר את הערך המספרי של הדרגה , המשמש להשוואות.
        """
        return self.value[1]

    def __str__(self):
        """
        מחרוזת תיאור של דרגת הקלף.
        """
        return self.display_name