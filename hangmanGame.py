import random

# Improved word list (you can expand this list as needed)
word_list = [
    "python", "java", "kotlin", "javascript", "hangman", "programming", "development",
    "computer", "algorithm", "function", "variable", "syntax", "compile", "interpreter"
]

# ASCII Art for the hangman stages
hangman_stages = [
    """
      -----
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]

def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = len(hangman_stages) - 1
    used_hints = False

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(hangman_stages[len(hangman_stages) - 1 - attempts])
        print(f"\nYou have {attempts} attempts remaining.")
        print(f"Current word: {display_word(word, guessed_letters)}")
        
        guess = input("Guess a letter or type 'hint' for a hint: ").lower()

        if guess == "hint":
            if not used_hints:
                hint_letter = random.choice([letter for letter in word if letter not in guessed_letters])
                print(f"Hint: Try the letter '{hint_letter}'")
                used_hints = True
            else:
                print("You have already used your hint.")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print("Incorrect guess.")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(hangman_stages[-1])
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
