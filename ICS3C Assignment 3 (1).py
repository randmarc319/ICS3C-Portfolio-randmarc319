"""
===============================================
Assignment – 3
Student Name: Gavin Randell
Date: 03/11/2025

By typing my name above, I confirm that this is my own work
and I have not plagiarized or copied code from others or AI sources.
===============================================
"""

# =======================================================
# Task 1: Blast Off!
# 
# Write a program that asks the user for a number to count up to,
# and also asks how much to count by each time (the step size).
# The program should use a for loop to display the count on
# separate lines and end by printing "Blast off!".
#
# Program Requirements:
#   1. Ask the user for a number to count up to.
#   2. Ask the user for a step amount.
#   3. Use a for loop to count up by that step amount
#      until you reach that number or above.
#   4. Display each number on a new line.
#   5. When the count is finished, print "Blast off!".
#
# Example Output:
#   Enter a number to count up to: 20
#   Enter a step amount: 5
#   0
#   5
#   10
#   15
#   20
#   Blast off!
# =======================================================

goal_num = int(input("Enter a number to count up to:"))

step_num = int(input("Enter a step amount:"))

first_num = 0

for i in range (first_num, goal_num + 1, step_num):
    print(f"{i}")

print("Blast off!")
    

# =======================================================
# Task 2: Number Guessing Game
#
# Write a program that asks the user to guess a secret number
# between 1 and 10. You can hardcode the secret number
# (e.g., secret_number = 7).
#
# Program Requirements:
#   1. Use a while loop to let the user keep guessing until
#      they get it right.
#   2. If the guess is too low, display "Too low! Try again."
#      If the guess is too high, display "Too high! Try again."
#   3. When they guess correctly, display a congratulations message.
#
# Example Output:
#   I'm thinking of a number between 1 and 10.
#   Enter your guess: 5
#   Too low! Try again.
#   Enter your guess: 9
#   Too high! Try again.
#   Enter your guess: 7
#   You got it! The secret number was 7.
# =======================================================

secret_num = 6

print("Im thinking of a number between 1 and 10.")

user_guess = int(input("Enter your guess:"))

while user_guess > 6:
    print("Too high! Try again.")
    user_guess = int(input("Enter your guess:"))

while user_guess < 6:
    print("Too low! Try again.")
    user_guess = int(input("Enter your guess:"))

while user_guess > 6:
    print("Too high! Try again.")
    user_guess = int(input("Enter your guess:"))

while user_guess < 6:
    print("Too low! Try again.")
    user_guess = int(input("Enter your guess:"))

while user_guess != 6:
    user_guess = int(input("Enter your guess:"))
    
if user_guess == 6:
    print("You got it! The secret number was 6.")









