import random

print("Welcome to number guess game!")

range = int(input("Please enter the maximum value of the range:"))
number_to_guess = random.randint(1, range)
count = 1
guess = int(input("Enter your guess:"))

while guess != number_to_guess:
    if guess < number_to_guess:
        print("Your guess is smaller.")
    else:
        print("Your guess is larger.")
    guess = int(input("Please guess again: "))
    count += 1

if guess == number_to_guess:
    print("Well done, you won!")
    print("You took", count, "goes to complete the game.")

print("success")
