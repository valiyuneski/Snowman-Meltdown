import random
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    print("\n" + "="*40)
    # Display the snowman stage for the current number of mistakes.
    print(ascii_art.STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print(f"Word: {display_word}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Mistakes: {mistakes}/{len(ascii_art.STAGES)-1}")
    print("="*40 + "\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(ascii_art.STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check for win
        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 Congratulations! You saved the snowman!\n")
            break

        # Check for loss
        if mistakes >= max_mistakes:
            print(f"💧 Oh no! The snowman melted. The word was: {secret_word}\n")
            break

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❗ Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("⚠️  You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            mistakes += 1
            print("❌ Incorrect!")

def main():
    while True:
        play_game()
        again = input("Would you like to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing Snowman Meltdown!")
            break

if __name__ == "__main__":
    main()

