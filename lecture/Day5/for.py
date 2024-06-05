# 파이썬 리스트로 for 반복문 만들기

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)
# -----------------------------------------------

# << 평균 키 구하기 >>

# Input a Python list of student heights
student_heights = input().split()

# range(a) -> 0부터 a-1 까지의 정수를 반환  // range(a,b) -> a부터 b-1 까지 반환 // range(a,b,c) -> a부터 c숫자만큼의 간격으로 b-1 까지의 정수를 반환
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

total_height = 0
for total in student_heights:
  total_height += total
# print(total_height)

number_of_students = 0
for count in student_heights:
  number_of_students += 1
# print(number_of_students)
  
average = round(total_height / number_of_students)

print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average}")
# -----------------------------------------------

# << 리스트 중 가장 높은 숫자 뽑기 >>

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
# print(highest_score)
print(f"The highest score in the class is: {highest_score}")
# -----------------------------------------------

# << Range 함수 >>

# range(a) = 0 ~ a-1 까지 정수 반환 / range(a, b) = a ~ b-1 까지 정수 반환 / range(a,b,c) = a ~ b-1 까지 c의 간격으로 정수 반환  
for number in range(1, 10):
    print(number)

# 1 ~ 100 까지 정수 모두 더하기

total = 0
for number in range(1, 101):
    total += number
print(total)
# -----------------------------------------------

# << 1 ~ 100 까지 짝수만 더하기 >>

# 내가 해본 것

total = 0
for number in range(1, 101):
    if number % 2 == 0:
        # print(number)
        total += number
print(total)

# 수정)

target = int(input())
even_sum = 0
for number in range(2, target+1, 2):
    even_sum += number
print(even_sum)

# or

alternative_sum = 0
for number in range(1, target+1):
    if number % 2 == 0:
        alternative_sum += number
print(alternative_sum)
# -----------------------------------------------

# << FizzBuzz Game >> - 3배수는 "Fizz" / 5배수는 "Buzz" / 3과 5 모두 배수는 "FizzBuzz"

# 순서가 중요하다
# 조건문은 위에서부터 실행되고 elif 문은 첫 번째 조건문이 거짓일 때 실행됩니다.

target = 100

for number in range(1, target+1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
# -----------------------------------------------

# << 비밀번호 자동 생성기 >>
# << Password Generator Project >>

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# << Eazy Level >> - Order not randomised: / 순서대로 적용
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for char in range(1, nr_letters + 1): # 마지막에 +1 해준 이유 : range(1,5) 1 ~ 4 를 반환 해주기때문
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(numbers)

for char in range(1, nr_numbers + 1):
    password += random.choice(symbols)

print(password)

# << Hard Level >> - Order of characters randomised: / 랜덤으로 적용
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(symbols))

print(password_list)

random.shuffle(password_list)
print(password_list)

# 문자열로 변환

password = ""

for char in password_list:
    password += char

print(f"Your password is : {password}")