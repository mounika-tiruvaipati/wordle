def matching_words(word, guess):
    example = []
    for g, w in zip(guess, word):
        if g == w:
            example.append(g)

    return example

word = "Happy"
guess = input("Please enter your guess: ")

while guess != word:
    result = matching_words(word, guess)
    print("Matching letters:", result)
    
    guess = input("Please enter your next guess: ")

print("Congratulations! You've guessed the word.")
