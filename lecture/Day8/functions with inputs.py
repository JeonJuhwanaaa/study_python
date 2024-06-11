# << def / 나만의 함수만들기 >>

# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")

# greet()

# ---------------------------------------------------------------------------

# << Parameter(매개변수)를 가진 함수 >>

# Functions with Inputs

# def my_function(something):
    #Do this with something
    #Then do this
    #Finally do this

# ex) something = 123
# Parameter(something) / 123(Argument) 라고 부름 

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name("Juhwan")

# ---------------------------------------------------------------------------

# << 1개 이상의 매개변수 갖는 함수 >>

# Functions with more than 1 input

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# # Positional Argument / Parameter(매개변수) 위치와 같은 Argument(인자) 위치에 따라 값을 대입
# greet_with("Jack Bauer", "Nowhere")

# ---------------------------------------------------------------------------

# << 매개변수와 인자 순서가 달라도 순서에 관계 없이 값 넣어주기 >>

# Keyword Argument

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# greet_with(location="London", name="Juhwan")

# ---------------------------------------------------------------------------

# << 페인트 면적 계산기 >>

# import math

# def paint_calc(height, width, cover):
#   # math.ceil => round up 내장함수 즉, 정수를 올림해주는 내장함수
#   number_of_cans = math.ceil((height * width) / cover)
#   print(f"You'll need {number_of_cans} cans of paint.")
  
# # Write your code above this line 👆

# # Define a function called paint_calc() so the code below works.   

# # 🚨 Don't change the code below 👇

# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# ---------------------------------------------------------------------------

# << Prime Number >> -> 자기 자신 또는 1 외의 다른 숫자로는 나눌 수 없는 숫자

# Write your code below this line 👇

def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)

# ---------------------------------------------------------------------------
