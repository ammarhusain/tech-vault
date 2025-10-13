# a simple guess the number game
import random

# get a random number from 1 to max_number
max_number = 100
secret_number = random.randint(1, max_number)
print(f"I'm thinking of a number from 1 to {max_number}")

# infinite loop
while True:
    guess = input("Guess the number (type 'q' to quit): ")
    if guess == 'q':
        break
    guess_number = int(guess)
    if guess_number == secret_number:
        print("Correct! That's the right number.")
        break
    elif guess_number < secret_number:
        print("Your guess is too low")
    elif guess_number > secret_number:
        print("Your guess is too high")

# end of loop
print("game over")
