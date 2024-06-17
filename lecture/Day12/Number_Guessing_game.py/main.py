import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        count = 10
        random_number = int(random.choice(range(100)))
        # print(random_number)
        guess = int(input("Make a guess: "))
        is_win = False

        while not is_win: 
            if guess > random_number:
                print(f"You have {count} attempts remaining to guess the number.")
                print("Too high.\nGuess again.")
                return count - 1
            elif guess < random_number:
                print(f"You have {count} attempts remaining to guess the number.")
                print("Too low.\nGuess again.")
                return count - 1
            else:
                print("You win.")
                is_win = True
    else:
        count = 5
        random_number = int(random.choice(range(100)))
        # print(random_number)
        guess = int(input("Make a guess: "))
        is_win = False

        while not is_win:
            if guess > random_number:
                print(f"You have {count} attempts remaining to guess the number.")
                print("Too high.\nGuess again.")
                return count - 1
            elif guess < random_number:
                print(f"You have {count} attempts remaining to guess the number.")
                print("Too low.\nGuess again.")
                return count - 1
            else:
                print("You win.")
                is_win = True

    




number_guessing_game()