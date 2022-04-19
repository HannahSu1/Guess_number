#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
print(logo)

import random
target = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose the level you want to play:'easy' or 'hard'\n")

def game(target_num,cnt):
    while cnt:
        n = int(input("Input your guessing number:"))
        if n > target_num:
            print("too high") 
            cnt -=1
        elif n < target_num:
            print("too low")
            cnt -=1
        else:
            print("You win!")
            break            
            
if level == 'easy':
    game(target,cnt=10)    
elif level == 'hard':
    game(target,cnt=5)

