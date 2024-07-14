import random

def get_random_word():
    words = ["python", "hangman", "challenge", "programming", "random", "words", "guessing", "game", "pillow", "earPhones", "laptop", "keyboard", "diary"]
    return random.choice(words)

def display_current_state(word, guessed_letters):
    display = [letter if letter in guessed_letters else "_" for letter in word]
    return " ".join(display)

def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 10

    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\n" + display_current_state(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            if set(word).issubset(guessed_letters):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! The letter '{guess}' is not in the word.")
    
    if incorrect_guesses == max_incorrect_guesses:
        print(f"Sorry, you lost! The word was: {word}")

if __name__ == "__main__":
    play_hangman()
