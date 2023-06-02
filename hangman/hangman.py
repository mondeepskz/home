import random
from words import words
import string

def get_valid_word(words):

    word = random.choice(words)
     
    while "-" in word or " " in word:
        word = random.choice(words)

    return word    

def hangman():

    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    l = 0

    while len(word_letters) > 0:
        
        chances = 7
        print (f"Used letters: {' '.join(used_letters)}")
        letter_list = [letter if letter in used_letters else '-' for letter in word]
        print(f"Word: {' '.join(letter_list)}")
        user_letter = input("Give letter: ").lower()
        print(' ')
        print(' ')
       
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter not in word_letters:
                l = l + 1
                chances = 7 - l
                print(f"Chances remain: {chances}")
                print(' ')        
            if user_letter in word_letters:
                word_letters.remove(user_letter) 
        elif user_letter in used_letters:
            print(f"You have already used '{user_letter}'")   
        else:
            print("Invalid character")


        if chances == 0:
            print(f'You failed! Your word was: {word.upper()}')          
            break

    if len(word_letters) == 0:
        print(f'You won! Your word is: {word.upper()}')

get_valid_word(words)
hangman()
