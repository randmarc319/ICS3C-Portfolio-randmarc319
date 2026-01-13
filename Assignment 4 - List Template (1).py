"""
Assignment 4 - List
Name:Gavin Randell
Date:08/12/2025
________________________________________________________________________________________________
PART A
________________________________________________________________________________________________
Prompt the user to enter positive numbers repeatedly which represent test scores. 
Continue accepting float inputs until the user enters -1.  
Value -1 will act as a sentinel to stop the input process. 
Store all positive numbers entered by the user in a list.  
After input ends, loop through the list and print each number on a new line. - This needs to be completed for a Level 4  
Bonus: Calculate the average of the test scores – One bonus mark
"""

test_scores = []

score = int(input("Enter test score (positive float, -1 to stop):"))

scores_sum = sum(test_scores)

list_count = len(test_scores)

test_scores.append(score)

while score != -1:
    score = int(input("Enter test score (positive float, -1 to stop):"))
    test_scores.append(score)
    
if score == -1:
    test_scores.pop()
    print("Test scores entered:")
    for test in test_scores:
        print(test)


"""
________________________________________________________________________________________________
PART B
________________________________________________________________________________________________
Prompt the user to enter words repeatedly. 
Continue accepting input until the user enters "quit".  
The word "quit" will act as a stop for the input process. 
Store all words entered by the user in a list. 
After input ends, display all the words in the list. 
Ask the user if they want to check whether a specific word exists in the list: - This needs to be completed for a level 4 Level 4 
If yes, prompt them to enter a word. 
Display whether the word is found in the list.  
You may assume that the names are all lowercase including the word quit – You will lose marks for using upper(), lower() or find() 
"""

word_list = []

user_word = input("Enter a word (type 'quit' to stop):")

word_list.append(user_word)

while user_word != ("quit"):
    user_word = input("Enter a word (type 'quit' to stop):")
    word_list.append(user_word)
    
if score == -1:
    word_list.pop()
    print("Words entered:")
    for word in word_list:
        print(word)

user_check = input("Do you want to check if a word exists in the list? (yes/no):")

if user_check == ("yes"):
    word_search = input("Enter the word to check:")
    if word_search in word_list:
        print(f"{word_search} is in the list!")
    else:
        print(f"{word_search} is not in the list :(")
    

