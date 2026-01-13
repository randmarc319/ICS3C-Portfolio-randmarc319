"""
===============================================
Assignment 1 – Python Programming
Student Name: Gavin Randell
Date: 17/09/2025

By typing my name above, I confirm that this is my own work
and I have not plagiarized or copied code from others or AI sources.
===============================================
"""

# =======================================================
# Question 1: Say Hello
# Write a program that asks the user for their name
# and prints: Hello, <name>!
# =======================================================
name = input("What is your name?")

print(f"Hello {name}!")

# =======================================================
# Question 2: Adding Numbers
# Ask the user to enter two numbers. Add them together
# and print the result.
# =======================================================
num_1 = int(input("Enter 1st number:"))

num_2 = int(input("Enter 2nd number:"))

print(f"The sum of {num_1} and {num_2} is {num_1 + num_2}")

# =======================================================
# Question 3: Average of Three Numbers
# Ask the user to enter three numbers. Calculate the
# average and print it.
# =======================================================
total_numbers = 3

n_1 = int(input("Number 1:"))
          
n_2 = int(input("Number 2:"))
          
n_3 = int(input("Number 3:"))

sum_of_all = n_1 + n_2 + n_3

print(f"The average is {sum_of_all / total_numbers:.2f}")


# =======================================================
# Question 4: Pizza Shop – Calculate Tax
# Ask the user to enter the total cost of their order.
# Calculate 13% tax and print the total amount including tax.
# ===============
order_cost = float(input("Enter order total:"))

tax_rate = 0.13

order_cost_tax = order_cost * tax_rate + order_cost

print(f"Total:{order_cost_tax}$")




# =======================================================
# Question 6: Tip Calculator
# Ask the user to enter the total bill amount at a restaurant.
# Ask the user to enter a tip percentage (e.g., 15 for 15%).
# Calculate the tip amount and the total bill including tip.
# Print both values clearly.
# =======================================================

bill_amt = int(input("Enter total bill amount:"))

tip_pct = int(input("Enter tip percentage:"))

tip_dec = tip_pct / 100

tip = tip_dec * bill_amt

print(f"Tip:{tip:.2f}$")

print(f"Total:{tip + bill_amt:.2f}$")


