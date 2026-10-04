"""Let a user get a score, print its result, or show that many stars."""

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
PASSABLE_SCORE = 50
EXCELLENT_SCORE = 90
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Get an initial score and handle the menu until the user quits."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Score {score} is {determine_result(score)}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye.")


def get_valid_score():
    """Get an integer score from 0 to 100 inclusive."""
    score_text = input("Enter score (0-100): ")
    while (not score_text.isdecimal()
           or not MINIMUM_SCORE <= int(score_text) <= MAXIMUM_SCORE):
        print("Invalid score")
        score_text = input("Enter score (0-100): ")
    return int(score_text)


def determine_result(score):
    """Return the result label for a score from 0 to 100."""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    if score >= EXCELLENT_SCORE:
        return "Excellent"
    if score >= PASSABLE_SCORE:
        return "Passable"
    return "Bad"


def print_stars(score):
    """Print as many stars as the integer score."""
    print("*" * score)


main()
