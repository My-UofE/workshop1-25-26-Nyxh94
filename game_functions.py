import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    choice = int(round(len(poss_values)/2))
    x = poss_values[choice]
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if user_input == "h":
        if next_val > current_val:
            return True
        else:
            return False
    elif user_input == "l":
        if next_val < current_val:
            return True
        else: 
            return False
    else:
        print("Please input 'h' or 'l'")




# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    if letter in word:
        word_list = list(word)
        for i in range(0, len(word_list)):
            if word_list[i] == letter:
                board[i] = letter
        return True
    else:
        return False

