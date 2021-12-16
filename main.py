from random import randint
from time import sleep
import os


def clear():
    return os.system("clear")


def main():
    f = open("words.txt").read().splitlines()
    f_size = len(f)
    word = f[randint(0, f_size - 1)]
    word_hidden = '*' * len(word)
    guessed_chars = []
    lives = 5

    while True:
        found = False

        clear()
        print("------------HANGMAN------------")
        print("-------------------------------")
        print(f"Guessed chars: {guessed_chars}")
        print(f"Your lives: {lives}")
        print(word_hidden)

        guess = input("Enter your guess: ")[0]

        # If the letter was guessed before we inform the player
        # and move on to the next guess
        if guess in guessed_chars:
            print("You already guessed this letter")
            sleep(1)
            continue

        # We loop through the word and try to find all the matches
        for i in range(len(word)):
            if word[i] == guess:
                found = True
                word_hidden = word_hidden[:i] + guess + word_hidden[i + 1:]

        if not found:
            lives -= 1

        if word == word_hidden:
            print(f"The word is: {word}")
            print("-------------------------------")
            print("YOU WON !!!")
            break
        elif lives == 0:
            print(f"The word is: {word}")
            print("-------------------------------")
            print("YOU LOST !!!")
            break
        
        if guess not in guessed_chars:
            guessed_chars.append(guess)


if __name__ == "__main__":
    main()
