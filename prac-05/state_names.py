"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
Word Occurrences
Estimate: 20 minutes
Actual:   30 minutes
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:<4} is {state_name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
