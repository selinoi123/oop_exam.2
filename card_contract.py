from abc import ABC, abstractmethod


class AbstractCard(ABC):
    """
    מחלקת אבסטרקטית (מופשטת) שמגדירה את הממשק הבסיסי לקלף.
    כל מחלקה שמממשת אותה צריכה לממש את כל הפונקציות והמאפיינים המוגדרים כאן.
    כל מה שיש פה צריך לממש במחלקה יורשת.
    """

    @property
    @abstractmethod
    def suit(self):
        """
        מחזיר את סוג הקלף.Suit.
        """
        pass

    @property
    @abstractmethod
    def rank(self):
        """
        מחזיר את דירוג הקלף Rank.
        """
        pass

    @abstractmethod
    def get_display_name(self):
        """
        מחזיר מחרוזת ייצוג של הקלף .
        """
        pass

    @abstractmethod
    def __eq__(self, other):
        """
        השוואה בין שני קלפים לפי שוויון.
        """
        pass

    @abstractmethod
    def __lt__(self, other):
        """
        השוואה בין שני קלפים - קטן מ.
        """
        pass

    @abstractmethod
    def __gt__(self, other):
        """
        השוואה בין שני קלפים - גדול מ.
        """
        pass

    @abstractmethod
    def __str__(self):
        """
        מחרוזת תיאורית של הקלף .
        """
        pass

    @abstractmethod
    def __repr__(self):
        """
        ייצוג טכני של הקלף.
        """
        pass

    @abstractmethod
    def __hash__(self):
        """
        ייחוד הקלף לצורך שימוש במבנים (set או dict).
        """
        pass

