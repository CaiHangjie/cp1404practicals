"""Write a name and read text files using different techniques."""


def main():
    """Run the four separate file exercises."""
    # 1. Write the entered name using open and close.
    name = input("Name: ")
    out_file = open("name.txt", "w")
    print(name, file=out_file)
    out_file.close()

    # 2. Read the stored name using open and close.
    in_file = open("name.txt")
    name = in_file.read().strip()
    in_file.close()
    print(f"Hi {name}!")

    # 3. Read only the first two numbers.
    with open("numbers.txt") as in_file:
        first_number = int(in_file.readline())
        second_number = int(in_file.readline())
    print(first_number + second_number)

    # 4. Total all numbers, regardless of the number of lines.
    total = 0
    with open("numbers.txt") as in_file:
        for line in in_file:
            total += int(line)
    print(total)


main()
