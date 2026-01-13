"""
===============================================
Assignment Mini Activity 7
Student Name: Gavin Randell
Date: 19/09/2025

By typing my name above, I confirm that this is my own work
and I have not plagiarized or copied code from others or AI sources.
===============================================
"""
age = int(input("Enter your age:"))

parent_prm = input("do you have parent permission?(yes/no)")

if age >= 18:
    print("You can watch the movie")

elif age < 18 and parent_prm == ("yes"):
    print("You can watch the movie")

else:
    print("You cannot watch the movie")
    
