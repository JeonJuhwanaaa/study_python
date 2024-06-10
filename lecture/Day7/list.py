#  일반적인 list 메서드입니다.

# list.append(elem) -- 목록 끝에 단일 요소를 추가합니다. 일반적인 오류: 새 목록을 반환하지 않고 원본만 수정합니다.
# list.insert(index, elem) -- 지정된 색인에 요소를 삽입하여 요소를 오른쪽으로 이동합니다.
# list.extend(list2)는 list2의 요소를 목록 끝에 추가합니다. 목록에서 + 또는 += 를 사용하는 것은 expand()를 사용하는 것과 비슷합니다.
# list.index(elem) -- 목록의 시작 부분부터 지정된 요소를 검색하여 색인을 반환합니다. 요소가 나타나지 않으면 ValueError가 발생합니다 (ValueError 없이 확인하려면 'in'을 사용).
# list.remove(elem) -- 지정된 요소의 첫 번째 인스턴스를 검색하여 삭제합니다 (없는 경우 ValueError 발생).
# list.sort() -- 목록을 제자리에 정렬합니다 (반환하지 않음). 나중에 표시되는 정렬() 함수를 사용하는 것이 좋습니다.
# list.reverse() -- 목록을 역전합니다 (반환하지 않음).
# list.pop(index) -- 지정된 색인에서 요소를 삭제하고 반환합니다. 색인이 생략되면 가장 오른쪽에 있는 요소를 반환합니다 (add()와 거의 반대).

# -----------------------------------------------------------------------------------------------------------------------------------------------

# # Step 1

# word_list = ["ardvark", "baboon", "camel"]

# # todo-1 -> Randomly choose a word from the word_list and assign it to a varibable called chosen_word.
# import random

# chosen_word = random.choice(word_list)

# # 해석 : 랜덤 모듈을 사용해서 list에 있는 문자를 하나 랜덤 선택

# # todo-2 -> Ask the user to guess a letter ad assign their answer to a variable called guess. Make guess lowercase.

# guess = input("Guess a letter: ").lower()

# # 해석 : 유저한테 맞출 알파벳을 물어보는 것 / 유저가 선택한 알파벳 소문자로 변환

# # todo-3 -> Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("wrong")

# # 해석 : 유저가 고른 알파벳이 랜덤으로 선택된 문자에 포함이 되면 right / 아니면 wrong 표시

# -----------------------------------------------------------------------------------------------------------------------------------------------

# # Step 2

# import random

# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #TODO-1: - Create an empty List called display.
# display = []
# word_length = len(chosen_word)

# #For each letter in the chosen_word, add a "_" to 'display'.
# for letter in range(word_length): 
#     display += "_"
# print(display)

# #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

# guess = input("Guess a letter: ").lower()

# #TODO-2: - Loop through each position in the chosen_word;
# #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# for position in range(word_length):
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter

# #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# print(display)

# -----------------------------------------------------------------------------------------------------------------------------------------------

# # Step 3

# import random
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# #TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# end_of_game = False

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     print(display)

#     if "_" not in display:
#         end_of_game = True
#         print("You win")

# -----------------------------------------------------------------------------------------------------------------------------------------------

# Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

# lives = len(stages)
# print(lives)
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")    

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

    print(stages[lives])