# ---------------------------------------------------------
# Academic Integrity Declaration
# I, Gavin Randell, confirm that this work is my
# own. I have not used AI tools or received external help.
# ---------------------------------------------------------
# =========================================================
# TASK 1: Vending Machine Program
# ---------------------------------------------------------
# Requirements:
# - Simulate a vending machine with 3 items:
#     1. Chips – $2.00
#     2. Chocolate – $2.50
#     3. Soda – $3.00
# - Ask user to choose an item (1–3)
# - Ask user to insert money
# - If money < cost → print "Not enough money. Transaction cancelled."
# - If money == cost → print "Enjoy your item!"
# - If money > cost → print "Enjoy your item! Your change is $X."
#
# Pseudocode:
# - Print all choices
# - Get choice from user
# - Print total cost
# - Get pay from user
# - Calculate change if necessary and print
#   "Enjoy your item!"
# 
# Flowchart:
# (Write your flowchart description here as comments, or attach separately)
#
# Python Code:
# =========================================================
soda = 3

chocolate = 2.50

chips = 2

print("Chips - $2")

print("Chocolate - $2.50")

print("Soda - $3")

choice = input("Select Item:")

if choice == ("soda"):
    print("Total: $3.00")
    pay_1 = float(input("Insert cash:"))
    
elif choice == ("chocolate"):
    print("Total: $2.50")
    pay_1 = float(input("Insert cash:"))
    
elif choice == ("chips"):
    print("Total: $2.00")
    pay_1 = float(input("Insert cash:"))
    
else:
    print("Invalid input")

if pay_1 == soda and choice == ("soda"):
    print("Enjoy your item!")
    
elif pay_1 > soda and choice == ("soda"):
    print(f"Enjoy your item! your change is ${pay_1 - soda:.2f}")
    
elif pay_1 < soda and choice == ("soda"):
    print("Transaction cancelled, not enough funds.")
    
elif pay_1 == chocolate and choice == ("chocolate"):
    print("Enjoy your item!")
    
elif pay_1 > chocolate and choice == ("chocolate"):
    print(f"Enjoy your item! your change is ${pay_1 - chocolate:.2f}")
    
elif pay_1 < chocolate and choice == ("chocolate"):
    print("Transaction cancelled, not enough funds.")
    
elif pay_1 == chips and choice == ("chips"):
    print("Enjoy your item!")
    
elif pay_1 > chips and choice == ("chips"):
    print(f"Enjoy your item! your change is ${pay_1 - chips:.2f}")
    
elif pay_1 < chips and choice == ("chips"):
    print("Transaction cancelled, not enough funds.")
    
else:
    print("Transaction failed")





# =========================================================
# TASK 2: Movie Ticket Price Calculator
# ---------------------------------------------------------
# Requirements:
# - Ask user for age
# - Ask if user is a student (Yes/No)
# - Ticket prices:
#     Under 12 → $8
#     12–17 → $10
#     18–64 → $12
#     65+ → $6
# - If student AND over 12 → $2 discount
# - Output final ticket price
#
# Pseudocode:
# - Get age from user
# - Check if user is student
# - Calculate discount if necessary and print total
#
# Flowchart:
# (Write your flowchart description here as comments, or attach separately)
#
# Python Code:
# =========================================================
children = 8

teens = 10

adults = 12

seniors = 6

print("Under 12 - $8")

print("12-17 - $10")

print("18-64 - $12")

print("65+ - $6")

age = int(input("Enter age:"))

is_student = input("Are you a student?(yes/no):")

if age in range (0, 12) and is_student == ("yes"):
    print(f"Total: ${children - 2}")

elif age in range (0, 12) and is_student == ("no"):
    print(f"Total: ${children}")
    
elif age in range (12, 17) and is_student == ("yes"):
    print(f"Total: ${teens - 2}")

elif age in range (12, 17) and is_student == ("no"):
    print(f"Total: ${teens}")
    
elif age in range (18, 64) and is_student == ("yes"):
    print(f"Total: ${adults - 2}")

elif age in range (18, 64) and is_student == ("no"):
    print(f"Total: ${adults}")

elif age >= 65 and is_student == ("yes"):
    print(f"Total: ${seniors - 2}")

elif age >= 65 and is_student == ("no"):
    print(f"Total: ${seniors}")
    
else:
    print("Invalid entry.")
