"""EX02 One Shot Wordle."""
__author__ = "730607229"

secret: str = "python"
secret_length: int = len(secret)
guess: str = input(f"What is your {secret_length}-letter guess? ")

while len(guess) != len(secret):
    if secret_length == 1:
        guess: str = input(f"That was not {secret_length} letter! Try again: ")
    if secret_length > 1:
        guess: str = input(f"That was not {secret_length} letters! Try again: ")
        # plural form when secret length > 1

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
idx: int = 0
# idx is short for loop indexing variables.
emoji_storage: str = ""
existence: bool = False
alt_idx: int = 0
# alt is the alternate indices of the secret word.

while idx < secret_length:
    if guess[idx] == secret[idx]:
        emoji_storage = emoji_storage + green_box   
    else:
        # Part 2: do not use this one: "if guess[idx] != secret[idx]:" or it will keep saying string out of range
        # Part 3: put while the boolean variable is not true and the index is less than the length of the secret here; putting it above(behind the if) will have errors.
        while existence is False and alt_idx < secret_length:
            if guess[idx] == secret[alt_idx]:
                existence = True
            else:
                alt_idx = alt_idx + 1
        if existence is True:
            emoji_storage = emoji_storage + yellow_box
        else: 
            emoji_storage = emoji_storage + white_box
    idx = idx + 1
    existence = False
    alt_idx = 0
print(f"{emoji_storage}")

if guess != secret:
    print("Not quite. Play again soon!")
if guess == secret:
    print("Woo! You got it!")
