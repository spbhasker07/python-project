import random as ram
words = '''hangman github python r-language php java c c# c++
vscode batman spiderman hulk usa germany uk london'''
words = words.split(" ")
selected_word = ram.choice(words).lower()
if __name__ == '__main__':
    print("Guess the word:")
    # Create a list of underscores
    display_word = ["_"] * len(selected_word)
    print(" ".join(display_word))
    attempts = len(selected_word) + 2
    guessed_letters = []  
    while attempts > 0:
        guess = input("Enter a letter: ").lower()      
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.")
            continue       
        guessed_letters.append(guess)        
        if guess in selected_word:
            print("Good guess!")
            for index, letter in enumerate(selected_word):
                if letter == guess:
                    display_word[index] = guess
        else:
            print("Wrong guess!")
            attempts -= 1
        print(" ".join(display_word))           
        if "_" not in display_word:
            print("Congratulations! You've guessed the word.")
            break     
        print(f"Attempts remaining: {attempts}")  
    if attempts == 0:
        print(f"Game over! The word was '{selected_word}'.")
