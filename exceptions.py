"""חריגה שאומרת שהתגלתה מניפולציה או חוסר ערבוב בחפיסת הקלפים."""


class DeckCheatingError(Exception):
    """Exception raised when deck appears to be unfairly constructed."""
    pass
