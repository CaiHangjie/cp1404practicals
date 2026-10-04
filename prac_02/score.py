"""Classify a user score and a randomly generated score."""

import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
PASSABLE_SCORE = 50
EXCELLENT_SCORE = 90


def main():
    """Display the user's result, any prize, and a random result."""
    user_score = float(input("Enter score: "))
    user_result = determine_result(user_score)
    print(f"User score {user_score} is {user_result}")
    if user_result == "Excellent":
        print("You get a prize!")

    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    random_result = determine_result(random_score)
    print(f"Random: {random_score} = {random_result}")


def determine_result(score):
    """Return the result label for a score from 0 to 100."""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    if score >= EXCELLENT_SCORE:
        return "Excellent"
    if score >= PASSABLE_SCORE:
        return "Passable"
    return "Bad"


main()
