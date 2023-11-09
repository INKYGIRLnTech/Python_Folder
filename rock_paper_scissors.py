import random

#keeping score
user_score = 0
computer_score = 0

#list with the values in it
options = ["rock", "paper", "scissors"]
#   indices  0      1          2 


#created a while loop giving it a True statement
while True:
    # Just in case they type in lowercase, make the str lower)
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
     # if they press 'q' the game ends
        break

    # if the user input is in the options then its invalid
    # the game will start the loop again until
    # the user input is in the options list
    if user_input not in options:
        continue

    #if they type any value in the options list
    # the game will generate a random number between 0 and 2
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2


    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")


    
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_score += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_score += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_score += 1

    
    #If none of the else if statements are true
    else:
        print("You lost!")
        computer_score += 1

print("User won", user_score, "times!")
print("The computer won", computer_score, "times!")
print("Goodbye!")

