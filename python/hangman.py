import random

hangman1 = [
    """
+---+
    |
    |
    |
    ===""","""
+---+
  | |
  o |
    |
    ===""","""
+---+
  | |
  o |
 /| |
    ===""","""

+---+
  | |
  o |
 /|\|
    ===""","""
  +---+
  | |
  o |
 /|\|
  | ===""","""
  /
+---+
  | |
  o |
 /|\|
  | ===""","""
 / \

"""
]

animals = ['tiger', 'giraffe', 'lion', 'zebra', 'dolphin', 'shark', 'elephant', 'rhino']

def play_hangman():
    word = random.choice(animals).lower()
    guessed_correctly = []
    guessed_incorrectly = []
    tries = 6
    hangman_count = 0

    while tries > 0:
        output = ''
        for letter in word:
            if letter in guessed_correctly:
                output += letter
            else:
                output += '_ '
        if output == word:
            break
        print("Guess the word:", output)
        print(tries, "chances left")
        guess = input("Enter your guess: ").lower()

        if guess in guessed_correctly or guess in guessed_incorrectly:
            print("Already guessed", guess)
        elif guess in word:
            print("Awesome job! You guessed a correct letter")
            guessed_correctly.append(guess)
        else:
            print("Sorry, you have guessed a wrong letter")
            hangman_count = hangman_count + 1
            tries = tries - 1
            guessed_incorrectly.append(guess)
            print(hangman1[hangman_count])

    if tries > 0:
        print("You guessed it right and you win!")
    else:
        print("Sorry, you guessed the wrong letter. The word was:", word)
  
play_hangman()




