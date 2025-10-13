# a simple guess the number game
import random

# get a random number from 1 to max_number
max_number = 100
secret_number = random.randint(1, max_number)
print(f"I'm thinking of a number from 1 to {max_number}")

# keep track of the number of attempts
attempts = 0

# infinite loop
while True:
    # each iteration represents another attempt
    attempts = attempts + 1
    if attempts >= 10:
        print("Too many guesses!")
        break
    guess = input(f"Attempt #{attempts} Guess the number (type 'q' to quit): ")
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

    # use the abs() function to determine if the guess is +/-10 of the secret number
    #alternative: if (guess_number - secret_number) <= 10 and (secret_number - guess_number) <= 10:
    if abs(guess_number - secret_number) <= 10:
        print("You are getting close")
    
# end of loop
print("game over")
