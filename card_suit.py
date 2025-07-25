from enum import Enum


class CardSuit(Enum):
    """
     המייצג את סוג הקלף (הצורה) בחפיסה
    """

    CLUBS = ("Clubs", 1)
    DIAMONDS = ("Diamonds", 2)
    HEARTS = ("Hearts", 3)
    SPADES = ("Spades", 4)

    @property
    def display_name(self):
        """
        מחזיר את שם הצורה לצורך תצוגה, (לדוגמה: Hearts).
        """
        return self.value[0]

    @property
    def strength(self):
        """
        מחזיר את העוצמה של הצורה.
        עוזר בהשוואה בין קלפים כאשר הדרגות שוות.
        """
        return self.value[1]

    def __str__(self):
        """
        מחרוזת תיאור של הצורה.
        """
        return self.display_name
