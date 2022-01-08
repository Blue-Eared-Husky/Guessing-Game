import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rightNumber = random.choice(numbers)
chances = 5

print("Welcome to the number guessing game!")

while chances <= 5:
    print("Chances remaining: " + str(chances))
    guess = int(input("Please enter your guess (from 1 to 9): "))
    if guess == rightNumber:
        print("Congratulations! You won!")
        break
    else:
        if guess < rightNumber:
            print("That was too low! Please try again.")
            chances = chances - 1
        if guess > rightNumber:
            print("That was too high! Please try again.")
            chances = chances - 1

if chances == 0:
    print("Oh no! You ran out of chances! The number was " + str(rightNumber))
