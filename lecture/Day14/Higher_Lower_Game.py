# 1. Display art

from art import logo
from art import vs
from game_data import data
import random

# 3. Format the account data into printable format.
def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

### 5-3. Use if statement to check if user is correct.
def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_countinue = True

# 8. Making account at position B become the next account at possition A.
account_b = random.choice(data)


# 7. Make the game repeatable.
while game_should_countinue:

    # 2. Generate a random account from the game data.
    account_a = account_b
    # print(account_a)
    account_b = random.choice(data)
    # print(account_b)

    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # 4. Ask user for a guess.

    # % 참고 % .lower() 내장함수를 사용하여 사용자가 입력한 알파벳이 대/소문자 상관없게 해주자.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # 5-1. Check if user is correct.
    ## 5-2. Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # 5-3 이후
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # 6-1. Give user feedback on their guess.
    # 6-2. Score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_countinue = False
        print(f"Sorry, that's wrong. Final score: {score}")


# 9. Clear the account between rounds.

# 이부분은 vscode에서 실현 안됨.