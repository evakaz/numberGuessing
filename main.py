# Make a program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range.
# Then give users a hint to guess the number. Every time the user guesses wrong, he gets another clue, and his score gets reduced.
# The clue can be multiples, divisible, greater or smaller, or a combination of all.
#You will also need functions to compare the inputted number with the guessed number, to compute the difference between the two, and to check whether an actual number was inputted or not in this python project.
import random

def EvenOrOdd():
    if (randomNumber % 2) == 0:
        return "The number is even"
    else:
        return "The number is odd"


def SmalllerOrBigger():
    if (userGuess > randomNumber):
        return f"The number is smaller than {userGuess}"
    else:
        return f"The number is bigger than {userGuess}"


def GiveHint():
    print("hello wrold")



randomNumber = random.randint(1, 10)
try:
    print("Your current score is 10")
    userGuess = int(input("Guess the number: "))
except ValueError:
    print("That's not a number!")

score = 10
while(userGuess != randomNumber):
    try:
        score =- 1
        userGuess = int(input("Guess the number: "))
        print("The number is incorrect. your current score is " + str(score))
        GiveHint()
    except ValueError:
        print("That's not a number!")

if userGuess == randomNumber:
    print("hoooraah you guessed the right number is " + str(randomNumber))


