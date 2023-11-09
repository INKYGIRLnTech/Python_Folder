import random

#List of words to choose from
word_list = ['Pikachu', 'Chamander', 'Bulbasaur', 'Squirtle', 'Krabby', 'Ivysaur']


#Randomly select a word from the list
selected_word = random.choice(word_list)

#Convert the selected word to lowercase for case-insenitive comparison
selected_word = selected_word.lower()

#Initialize a variable to keep track of the user's guess count
guess_count = 0

#Game Loop
while True:
    #Get a guess from the user
    user_guess = input('Guess the pokemon: ').lower()

    #Increment the guess count
    guess_count += 1

    #Check if the user's guess is correct
    if user_guess == selected_word:
        print(f"Congratulations! You guessed the Pokemon '{selected_word}' in {guess_count} guesses.")
        break
    else:
        print("Sorry, that's not the correct Pokemon. Try again.")