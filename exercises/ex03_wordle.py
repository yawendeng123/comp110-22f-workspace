"""EX03 - Structured Wordle."""
__author__ = "730607229"


def contains_char(word: str, single_char: str) -> bool:
    """Given a word and a single character, verifying if the word in the first string contains the single character of the second string."""
    assert len(single_char) == 1
    idx: int = 0
    # idx is short for loop indexing variables.
    while idx < len(word):
        if single_char == word[idx]:
            return True
        else:
            idx += 1
    return False


white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Given a guess and a secret, verify whether the characters in the guess match the characters and positions in the secret, and return a string of colored emoji."""
    # White for letters that don’t exist in the secret; green for letters that match the secret at the same position; yellow for each guessed letter the secret contains_char, but at a different position.
    assert len(guess) == len(secret)
    emoji_storage: str = ""
    alt_idx: int = 0
    # Set up an alternative idx for this funtion.
    while alt_idx < len(secret):
        if guess[alt_idx] == secret[alt_idx]:
            emoji_storage += green_box
            alt_idx += 1
        else:
            if contains_char(secret, guess[alt_idx]):
                emoji_storage += yellow_box
            else:
                emoji_storage += white_box
            alt_idx += 1
    return emoji_storage
    # Remember to quit() or kill the terminal after making changes and then save and re-run.


def input_guess(expected_len: int) -> str:
    """Prompt the user for a guess and continue prompting them until they provide a guess of the expected length."""
    guess: str = ""
    if len(guess) == 0:
        guess += input(f"Enter a {expected_len} character word: ")
    while len(guess) != expected_len:
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    secret: str = "codes"
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return None
        else:
            turn += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
