"""Get a sufficiently long password and print one star per character."""

MINIMUM_PASSWORD_LENGTH = 6


def main():
    """Get a valid password and display its length as stars."""
    password = get_password()
    print_stars(password)


def get_password():
    """Get a password that meets the minimum length."""
    password = input("Enter your password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print(f"Password must contain at least "
              f"{MINIMUM_PASSWORD_LENGTH} characters")
        password = input("Enter your password: ")
    return password


def print_stars(password):
    """Print one star for each character in the password."""
    print("*" * len(password))


main()
