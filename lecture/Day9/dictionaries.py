# << python Dictionaries >>

# Dictionaries -> 컴퓨터를 위한 프로그램 명령어들의 집합
# ex) {Key: Value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# -----------------------------------------------------------------------------------------------------

# Value 호출
# ex) print(변수명[Key]) -> Value 값 호출 됨.
# *Dictionarie 에서 값을 불러올 때는 키의 철자를 정확히 입력해줄 것!

print(programming_dictionary["Bug"])

# -----------------------------------------------------------------------------------------------------

# Adding new items to dictionary. - 추가
# ex) programming_dictionary[Key] = Value

programming_dictionary["Loop"] = "The action of doing something over and over again."

# -----------------------------------------------------------------------------------------------------

# 코드를 작성할 때 빈 Dictionary를 먼저 선언 후 시작하는 것이 도움이 될 것이다.
empty_dictionary = {}

# -----------------------------------------------------------------------------------------------------

# Wipe an existing dictionary - 초기화
# 빈 dictionary를 선언해주면 초기화 된다. - 이는 게임을 재시갖갷서 점수와 능력을 초기화 할 때와 같이
# 유저의 진행상황을 없애줘야 할 때오 같은 상황에서 매우 유용하다.

programming_dictionary = {}
print(programming_dictionary)

# -----------------------------------------------------------------------------------------------------

# Edit an item in a dictionary - 수정

programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# -----------------------------------------------------------------------------------------------------

# Loop through a dictionary - 반복문으로 값 빼오기

for key in programming_dictionary:
    print(key)
    programming_dictionary[key]

# 반복문을 통해 돌려주면 예상 -> Key / Value 순서대로 출력 될 것으로 예상함.
# 실제 출력 -> Key 만 순서대로 출력 됨.
# Value 값을 출력받고 싶다면 programming_dictionary[Key] 로 print 해줘야 한다.
