import random

number = random.randint(0 , 200)
user = -1
guess = 0

while user != number:
    user = int(input("Guess the choosen number (0-200): "))
    guess += 1
    if user > number:
        print("Guess a lower number Please!")
    elif user < number:
        print("Guess a higher number Please!")
    else:
        print(f"Win!!  you Guess the Correct number {number} in your {guess} attempts")


