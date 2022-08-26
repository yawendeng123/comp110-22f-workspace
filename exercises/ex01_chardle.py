"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730607229"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()

matching_number: int = 0
print("Searching for " + single_character + " in " + word)

if single_character == word[0]:
    print(single_character + " found at index 0")
    matching_number = matching_number + 1
if single_character == word[1]:
    print(single_character + " found at index 1")
    matching_number = matching_number + 1
if single_character == word[2]:
    print(single_character + " found at index 2")
    matching_number = matching_number + 1
if single_character == word[3]:
    print(single_character + " found at index 3")
    matching_number = matching_number + 1
if single_character == word[4]:
    print(single_character + " found at index 4")
    matching_number = matching_number + 1

if matching_number == 0:
    print("No instances of " + single_character + " found in " + word)
if matching_number == 1:
    print(str(matching_number) + " instance of " + single_character + " found in " + word)
if matching_number > 1:
    print(str(matching_number) + " instances of " + single_character + " found in " + word)
