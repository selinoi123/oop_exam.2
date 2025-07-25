from decorators import fair_deck
from deck import Deck
from exceptions import DeckCheatingError


@fair_deck
def create_shuffled_deck():
    """
    יוצר חפיסת קלפים מעורבבת באופן הוגן בעזרת (fair_deck).

    """
    return Deck(shuffle=True)


def main():
    """
    הפונקציה הראשית של התוכנית.
    יוצרת חפיסת קלפים, מדפיסה קלפים לפי אינדקס, מדפיסה את כל הקלפים,
    ומציגה את הקלף החזק ביותר והחלש ביותר בחפיסה.
    אם מתגלה מניפולציה (cheating), נתפסת חריגה מסוג (DeckCheatingError).
    """
    try:
        deck = create_shuffled_deck()
        print("Deck created and shuffled fairly.")

        print("Accessing cards directly by index:")
        for i in range(5):
            print(f"Card at index {i}: {deck[i]}")

        print("Iterating through all cards in the deck:")
        for card in deck:
            print(card)

        print(f"Max card in deck: {max(deck)}")
        print(f"Min card in deck: {min(deck)}")

    except DeckCheatingError as e:
        print(f"Cheating detected: {e}")


if __name__ == "__main__":
    main()

