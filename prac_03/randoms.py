"""Explore random number ranges."""

import random

# 1. Observed values: 13, 16, 19, 5, 9.
# randint(5, 20) can produce integers from 5 to 20, including both endpoints.
# 2. Observed values: 9, 3, 3, 7, 9.
# randrange(3, 10, 2) can produce 3, 5, 7 or 9: minimum 3, maximum 9.
# It cannot produce 4 because the step of 2 selects only odd numbers.
# 3. Observed values: 3.518107602836031, 2.667551408879048, 3.71610934800031,
# 3.6069019798675077 and 4.150509586344409.
# uniform(2.5, 5.5) produces floats between 2.5 and 5.5.
# The upper endpoint may be included due to floating-point rounding.


def main():
    """Display a random integer between 1 and 100 inclusive."""
    print(random.randint(1, 100))


main()
