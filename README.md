The Hangman game is a simple text-based implementation with the following features:

    Word Selection:
        The game selects a random word from a list stored in a 'words.txt' file in the same directory.

    User Interaction:
        Players input guesses by entering a single alphabetical character.
        The game checks the validity of the input and handles repeated guesses.

    Display:
        The current state of the word is displayed, with underscores representing unguessed letters.
        Guessed letters are displayed in their correct positions.

    Attempts:
        Players have a limited number of attempts (6 by default) to guess the word.
        The remaining attempts are shown.

    Game Outcome:
        If the player correctly guesses all the letters in the word, they win.
        If the player runs out of attempts without guessing the word, they lose.

    File Handling:
        The game reads words from a 'words.txt' file, providing flexibility for users to modify the word list easily.

    Error Handling:
        The game handles file not found errors and notifies the user.

    Case Insensitivity:
        Both user input and word comparison are case-insensitive.

    Clean Code Structure:
        The code is organized into functions, making it modular and easy to understand.

    Graceful Exit:
        If the word list file is not found, the program prints an error message and exits gracefully.

These features provide a basic framework for a Hangman game.
