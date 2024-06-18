import random
from art import logo

def number_guessing_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        count = 10
    else:
        count = 5

    random_number = int(random.choice(range(101)))
    # print(random_number)
    
    result = False

    while count > 0 and not result:
        guess = int(input("Make a guess: "))

        if guess > random_number:
            print(f"You have {count - 1} attempts remaining to guess the number.")
            print("Too high.\nGuess again.")
            count -= 1
        elif guess < random_number:
            print(f"You have {count - 1} attempts remaining to guess the number.")
            print("Too low.\nGuess again.")
            count -= 1
        elif guess == random_number:
            print("You win.")
            result = True
        elif count == 0:
            print("You lose")
            result = True

    if count == 0 and not result:
        print(f"You lose. The number was {random_number}.")
        


number_guessing_game()