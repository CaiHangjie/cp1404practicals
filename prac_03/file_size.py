"""Count lines in files until an empty filename is entered."""


def main():
    """Prompt for filenames and report line counts or missing files."""
    filename = input("Enter filename: ")
    while filename != "":
        try:
            number_of_lines = count_lines(filename)
            print(f"{filename} has {number_of_lines} lines.")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")
        filename = input("Enter filename: ")


def count_lines(filename):
    """Return the number of lines in the named file."""
    number_of_lines = 0
    with open(filename) as in_file:
        for line in in_file:
            number_of_lines += 1
    return number_of_lines


main()
