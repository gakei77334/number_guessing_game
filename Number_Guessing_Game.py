import random

NUMBER = random.randint(0, 100)

difficulty_level = input("Do you want it Easy or Hard?: ").lower()

# This function saves the user's guess
def guess_number():    
    # Allow the player to submit a guess for a number between 1 and 100.
    return int(input("Guess a number between 0 and 100: "))     

def check():
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
    if user_guess > NUMBER:
        print("Too High")
    elif user_guess < NUMBER:
        print("Too Low")
    # If they got the answer correct, show the actual answer to the player.
    else:
        print(f"You guessed it! Answer is {NUMBER}")    
        return True
    
# Track the number of turns remaining.
# This function returns either 5 or 10
def game_level():
    if difficulty_level == 'easy':
        return 10
    else:
        return 5

lives = game_level() # Function call

while lives > 0:
    user_guess = guess_number() # Function call
    # Function call
    if check(): # If check is True ie. if the user guesses the number correctly
        break  # Exit the loop if the user guessed the correct number
    lives -= 1 # While lives > 0 (from while loop line 34)
    print(f"Lives remaining: {lives}")
    
if lives == 0:
    print(f"Lives = 0. Correct answer: {NUMBER}")

