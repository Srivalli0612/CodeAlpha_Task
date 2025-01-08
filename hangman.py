import random

hangman_stages = [
    '''
     ------
     |    |
          |
          |
          |
          |
    =========
    ''',
    '''
     ------
     |    |
     O    |
          |
          |
          |
    =========
    ''',
    '''
     ------
     |    |
     O    |
     |    |
          |
          |
    =========
    ''',
    '''
     ------
     |    |
     O    |
    /|    |
          |
          |
    =========
    ''',
    '''
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    =========
    ''',
    '''
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    =========
    ''',
    '''
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    =========
    '''
]


file_path = "C:/Users/rhssr/OneDrive/Desktop/code_alpha/1k_words_with_actual_hints.txt"

with open(file_path, "r") as file:
    word_list = [line.strip().split(":", 1) for line in file if ":" in line]

word, hint = random.choice(word_list)
word = word.lower()
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []


print("Hint:", hint)


while attempts > 0:
    print("\nWord:", " ".join(guessed_word))
    print(f"Guessed Letters: {', '.join(guessed_letters)}")
    print(f"Remaining Attempts: {attempts}")
    
 
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    

    guessed_letters.append(guess)
    

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Incorrect guess!")
        attempts -= 1
        
        if attempts > 0:
            print(hangman_stages[6 - attempts])

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
        break

if attempts == 0:
    print("\nYou ran out of attempts. The word was:", word)
    print(hangman_stages[6])  
