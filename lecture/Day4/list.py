# Data structures

# Lists
# 파이썬의 리스트는 모든 데이터 형식을 저장할 수 있습니다 또한 혼합된 데이터 형식을 저장할 수도 있습니다
# 문자열과 숫자나 불리언 집합을 함께 저장할 수 있습니다. / 데이터 형식은 중요하지 않습니다.
# 중요한 것은 구문입니다.

# 인덱스 [0] - 정방향 순서 / [-1] 끝에서부터 역방향 순서

# state_of_america = ["Delaware", "Pennsylvania"]

# list 안에 하나의 데이터 추가 - append() 사용
# 여러 데이터를 추가 - extend([]) 사용

# state_of_america.append("Hawaii")
# state_of_america.extend(["Angelaland","Jack Bauer Land"])

# print(state_of_america)

# ---------------------------------------------

# 입력받은 이름 중 랜덤으로 계산하기 

# names_string = input()
# names = names_string.split(", ")

# import random

# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]

# print(person_who_will_pay + " is going to buy the meal today!")

# ---------------------------------------------

# index out of range 오류 - 인덱스 없는 수를 출력할 때 발생

# 중첩 리스트 만들기

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

# --------------------------------------------

# 보물 찾기

# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]

# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?

# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# letter = position[0].lower()
# abc = ["a", "b", "c"]

# letter_index = abc.index(letter)
# number_index = int(position[1]) -1
# map[number_index][letter_index] = "X"

# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")

# --------------------------------------------

# random 가위 바위 보

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")