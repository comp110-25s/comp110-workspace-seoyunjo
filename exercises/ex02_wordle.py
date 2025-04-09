__author__: str = "730760820"


def contains_char(word: str, character: str) -> bool:
    """True when word is found of the first string and False otherwise."""
    assert len(character) == 1, f"len('{character}) is not 1"
    idx: int = 0
    while idx < len(word):
        if word[idx] == character:
            return True
        idx += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Guess and secret are matching at the correct position"""
    result: str = ""
    idx = 0
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        idx += 1
    return result
    assert len(guess) == len(secret), "Guess must be same length as secret"


def input_guess(expected_length: int) -> str:
    """guess until provide a guess of the expected length"""
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    turns = 1
    max = 6
    won = False
    while turns <= max and won is False:
        print(f"===Turn {turns}/{max}===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            won = True
        else:
            turns += 1
    if won:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6- Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
