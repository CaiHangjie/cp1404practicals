"""Handle invalid integer input and prevent division by zero."""

# 1. ValueError occurs when int() cannot convert an input to an integer.
# 2. ZeroDivisionError occurs when the denominator is zero during division.
# 3. Check for a zero denominator before dividing to prevent ZeroDivisionError.


def main():
    """Get two integers and display their quotient when possible."""
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Cannot divide by zero!")
        else:
            fraction = numerator / denominator
            print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    print("Finished.")


main()
