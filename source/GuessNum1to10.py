## Exercise 1: Working with a while loop
# Printing the game rules
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Importing random and writing a while loop
import random

# Set initial values for the Number Guessing Game
number = random.randint(1,10)
isGuessRight = False
totalChances = 5
print("You've {} chances to guess the correct number. Good Luck!".format(totalChances))

# Define Number Guessing Game function
def GuessGame(setGuessRight, setNumber, guessNumber, chance):
    if guessNumber == setNumber:
        print("You guessed {}. That is correct! You win!".format(guessNumber))
        setGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guessNumber))
        print("{} guesses remaining".format(chance))
        setGuessRight = False
    return setGuessRight # Returns True if guess is right

# Run GuessGame() function upto preset chances to play
while isGuessRight != True:
    if totalChances > 0:
        guess = input("Guess a number between 1 and 10: ")
        if guess.isdigit():
            if int(guess) >= 1 and int(guess) <= 10:
                totalChances -= 1
                isGuessRight = GuessGame(isGuessRight, number, int(guess), totalChances)
            else:
                print("The {} isn't a number between 1 and 10. Try again".format(guess))
        else:
            print("The {} isn't a number between 1 and 10. Try again".format(guess))
    else:
        break

if int(guess) != number:
    print("\n")
    print("The number is {}".format(number))
    print("*****Game Over*****")
else:
    print("\n")
    print("***Thank you for playing***")
