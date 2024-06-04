# Data Types

# String - 문자열
# Subscript - 특정 문자열 추출하기
# print("Hello"[4])

# Integer - 정수
# 숫자 단위 끊어서 적을 때 ,(쉼표)를 _(밑줄)로 바꿔서 사용 가능한데 컴퓨터는 밑줄을 무시한다, 사용자는 편하게 인식한다
# print(123+456)

#Float - 소수점

#Boolean - True / False

#Type - Data Type을 알려줌

#str() - 문자열로 형변환

# num_char = len("Hello")

# print(num_char)

# print("Your name has" + num_char + "characters.") - 문자열안에 정수타입 넣어서 오류
# new_num_char = str(num_char) - 정수타입을 문자열로 변환
# print("Your name has " + new_num_char + " characters.")

# a = str(123)
# print(type(a))

# two_digit_number = input()
# print(int(two_digit_number[0])+int(two_digit_number[1]))



# << 연산 >>
# print(6/3) - 나누기하면 부동소수(type을 Float 으로 인식) 로 출력
# ** - 거듭제곱
# print(2**3) - 2*2*2 = 8
# 연산 순서 = () -> ** -> * / -> + -
# 예) 3 * 3 + 3 / 3 - 3 = 7.0
# print(3*3+3/3-3)
# 예) 3 * (3 + 3) / 3 - 3 = 3.0
# print(3*(3+3)/3-3)

# f-String - 위 코드 중 print("your age has " + age + " characters") 가 오류 뜨는건
# age 이 타입이 맞지않아서 오류가 발생해서 str(age) 해서 형변환 해줘야했다면
# f-String은 문자열 앞에 f를 써주고 {} 중괄호를 사용해서 형변환 없이 알아서 변환해준다. 
# score = 0
# height = 1.8
# isWinning = True
# print(f"your score is {score}, your hegith is {height}, you are winning is {isWinning}")

# -----------------------------------------------------------
# << f-String 과제 >>

# Life in weeks
# age = input()
# years = 90 - int(age)
# weeks = years * 52  -- 1년에 52주가 있으므로

# -----------------------------------------------------------
# << 팁 계산기 >>

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $")) - 데이터 형식이 String 이니깐 형변환 해주기
# print(type(bill))
# tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))
# bill_with_tip = tip / 100 * bill + bill
# tip_calcualator = round(bill_with_tip / people, 2) - 소수점 두번째 자리까지 반올림
# print(f"Each person should pay ${tip_calcualator}")
# -----------------------------------------------------------

# << if / else 조건 연산 or 비교 연산자(> < >= <= == !=) >>

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# # 들여쓰기 중요!!
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
# -----------------------------------------------------------

# << Nested if / elif / else 조건 연산 (중첩 조건 연산)

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))

#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.") 
#     else:
#         print("Please pay $12." )   
# else:
#     print("Sorry, you have to grow taller before you can ride.")
    
# -----------------------------------------------------------

# BMI 2.0 측정하기

# height = float(input())
# weight = int(input())

# bmi = weight / height**2
# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")
# -----------------------------------------------------------

# 윤년 계산 확인

# year = int(input())

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")
# -----------------------------------------------------------

# 롤러코스터 사진 받을 시 추가 요금 발생

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")

#     age = int(input("What is your age? "))

#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.") 
#     else:
#         bill = 12
#         print("Adult tickets are $12." )   

#     wants_photo = input("Do you went a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         #Add $3 to their bill
#         bill += 3

#     print(f"Youre final bill is {bill}")

# else:
#     print("Sorry, you have to grow taller before you can ride.")

# -----------------------------------------------------------

# 피자 주문

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N

# bill = 0

# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3

# if extra_cheese == "Y":
#   bill += 1
  
# print(f"Your final bill is: ${bill}. ")
# -----------------------------------------------------------

# 사랑 계산기

# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?

# combined_names = name1 + name2
# lover_names = combined_names.lower()
# t = lover_names.count("t")
# r = lover_names.count("r")
# u = lover_names.count("u")
# e = lover_names.count("e")
# first_digit = t + r + u + e

# l = lover_names.count("l")
# o = lover_names.count("o")
# v = lover_names.count("v")
# e = lover_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))

# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")
# -----------------------------------------------------------
