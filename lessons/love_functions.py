"""Some tender, loving loving functions."""

heart: str = "\U0001F499\U0001F49B"
def love(subject: str) -> str:
    """Given a subject as a parameter, returns a loving string."""
    return f"I love you {subject}! My one and only{heart}"

print(love("Suguru"))

def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note: str = ""
    counter: int = 0
    while counter < n:
        love_note += love(to) + "\n"
        counter += 1
    return love_note

print(spread_love("Suguru", 5))