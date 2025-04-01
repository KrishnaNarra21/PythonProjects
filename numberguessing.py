import random

# Get the top range number
top_range = input("Enter your top range number: ")

# Validate the input
if not top_range.isdigit() or int(top_range) <= 0:
    print("Please type a number larger than zero next time.")
    quit()

top_range = int(top_range)

# Generate a random number
random_number = random.randint(0, top_range)
n_times = 0

while True:
    n_times += 1
    user_guess = input("Guess the number: ")

    # Check if input is a number
    if user_guess.lstrip('-').isdigit():  # Allows negative numbers if needed
        user_guess = int(user_guess)
    else:
        print("Invalid input. Please enter a valid number.")
        continue

    # Check the guess
    if user_guess == random_number:
        print("You got it! Excellent work!")
        break
    elif user_guess > random_number:
        print("You're too high! Try again.")
    else:
        print("You're too low! Try again.")

# Feedback based on attempts
if n_times == 1:
    print("Amazing! You got it on the first try! 🎉")
else:
    print(f"Great job! You guessed it in {n_times} attempts. 🎯")





"""
This is a simple number guessing game where the player tries to guess a randomly generated number within a specified range. 
The game continues indefinitely until the user guesses the correct number.
"""



