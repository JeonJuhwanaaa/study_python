# Dictionary Comprehension

# EX) 기존 딕셔너리르 새로운 딕셔너리로 만드는 법.
# new_dict = {new_key:new_value for (key,value) in dict.items()}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >= 68}
print(passed_students)

# ----------------------------------------------------------------------------------

# You are going to use Dictionary Comprehension to create a dictionary called
# result that takes each word in the given sentence and calculates
# the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words.

# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

sentence = input()
# input 값 -> What is name?
# split() 함수는 문자열을 분할하는 매서드이며 원한다면 구분자를 명시가능.
# 매개변수가 빈 상태일 때는 공백을 기준으로 분할.
# sentence_split = sentence.split()

result = {word:len(word) for word in sentence.split()}
print(result)

# ----------------------------------------------------------------------------------

# 섭씨 온도만 화씨 온도로 value 값 변경해서 딕셔너리 만들기.

# You are going to use Dictionary Comprehension to create a dictionary
# called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f use this formula: (temp_c * 9/5) + 32 = temp_f

# input 값 -> {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# 딕셔너리 형태로 input 값을 받을 것이므로 eval() 함수 사용해주기.
weather_c = eval(input())

weather_f = {day:temp * 9/5 + 35 for (day, temp) in weather_c.items()}
print(weather_f)

# ----------------------------------------------------------------------------------

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

import pandas

student_dict_frame = pandas.DataFrame(student_dict)
print(student_dict_frame)

# Loop through a data frame
for (key, value) in student_dict_frame.items():
    print(key)
    print(value)

# Loop through rows of a data frame
# index -> 그냥 인덱스 번호만 출력
# row -> 각각의 데이터 행을 따로 나열해서 출력 / 각각의 행들은 판다스 시리즈의 객체
for (index, row) in student_dict_frame.iterrows():
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)