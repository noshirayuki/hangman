import random

def read_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file.readlines()]
        return words
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def choose_word():
    words = read_words_from_file('words.txt')
    if not words:
        print("No words available. Exiting.")
        exit()

    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter.lower() in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    while True:
        print("\nAttempts left:", max_attempts - attempts)
        print(display_word(word_to_guess, guessed_letters))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess not in word_to_guess.lower():
            attempts += 1
            print("Incorrect guess!")

        if set(guessed_letters) >= set(letter.lower() for letter in word_to_guess):
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break

        if attempts == max_attempts:
            print("\nSorry, you ran out of attempts. The word was:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()
