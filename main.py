import random
from five_letter_word import WORDS
from wordle_logic import matching_letter, matching_letter_wrong_placement 

word = random.choice(WORDS)

attempts = 1  
already_guessed_letters = []  

while attempts <= 6:
    guess = input("Please enter your guess (or type 'stop' to quit): ")
    
    if guess.lower() == "stop":
        print("Game ended by user.")
        break  
    
    if guess.lower() == word.lower():
        print("Congratulations! You've guessed the word.")
        break  

    if len(guess) != 5:
        print("Please only guess a 5 letter word!")
        continue

    example, misc = matching_letter(word, guess)
    wrong_placement, already_guessed_letters = matching_letter_wrong_placement(word, guess, already_guessed_letters)  

    print("Matching letters with correct placement:", example)
    print("Correct letters but wrong placement:", wrong_placement)
    print("Already guessed letters:", already_guessed_letters)
    print("Attempt #:", attempts)
    
    attempts += 1

    if attempts == 6:
        print("Sorry, you've reached the maximum number of attempts. The correct answer is:", word)
