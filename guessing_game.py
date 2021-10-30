# create a guessing game
import random
import time
import sys
import os

def main():
    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")
    print("")
    time.sleep(1)
    print("")

    random_number = random.randint(1, 100)
    guess = 0
    guess_count = 0
    guess_limit = 5
    out_of_guesses = False
    while guess != random_number and not(out_of_guesses):
        if guess_count < guess_limit:
            guess_count += 1
            guess = int(input("Take a guess: "))
            if guess < random_number:
                print("Higher!")
            elif guess > random_number:
                print("Lower!")
            else:
                print("You got it!")
        else:
            out_of_guesses = True
    if out_of_guesses:
        print("You ran out of guesses. The number was", random_number)
    else:
        print("You guessed it in", guess_count, "guesses!")
    print("")
    play_again = input("Do you want to play again? Y/N: ")
    if play_again.lower() != "n":
        main()
    else:
        print("Thanks for playing!")
        sys.exit()

main()