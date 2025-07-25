from abc import ABC, abstractmethod
from card import Card


class AbstractDeck(ABC):
    """
    מחלקת בסיס אבסטרקטית לחפיסת קלפים.
    כל מחלקה שמממשת אותה צריכה לממש את כל הפונקציות והמאפיינים המוגדרים כאן.
    כל מה שיש פה צריך לממש במחלקה יורשת.
    """

    @abstractmethod
    def shuffle(self):
        """
        ערבוב הקלפים בחפיסה באופן אקראי.
        """
        pass

    @abstractmethod
    def draw(self):
        """
        שליפת קלף מהחפיסה מראש הרשימה.
        """
        pass

    @abstractmethod
    def add_card(self, card: Card):
        """
        הוספת קלף לחפיסה.
        קלף מסוג Card להוספה.
        """
        pass

    @property
    @abstractmethod
    def cards(self):
        """
        מחזיר את רשימת הקלפים הנוכחית כטופל לצורך קריאה בלבד.
        """
        pass

    @abstractmethod
    def __len__(self):
        """
        מחזיר את מספר הקלפים הנוכחיים בחפיסה.
        """
        pass

    @abstractmethod
    def __getitem__(self, index):
        """
        מאפשר גישה לקלפים לפי אינדקס (כמו ברשימה).
        """
        pass

    @abstractmethod
    def __iter__(self):
        """
        מאפשר איטרציה על החפיסה בעזרת לולאות.
        """
        pass
