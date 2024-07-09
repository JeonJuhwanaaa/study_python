# List Comprehension 을 통해 리스트 생성하기.

# << 기초로 배웠던 리스트 코드 >>

numbers = [1, 2, 3]
new_numbers = []

for n in numbers:
    new_numbers.append(n+1)
print(new_numbers)

# -----------------------------------------
# << List Comprehension >>
# 위 코드를 간결하게 한줄로 만드는 것.

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Angela"
letter_list = [letter for letter in name]
print(letter_list)

double_list = [ num * 2 for num in range(1, 5)]
print(double_list)

# -----------------------------------------
# << 조건이 포함된 List Comprehension >>

# ex) new_list = [new_item for item in list if test]
# 덧붙여진 if test는 이 코드를 실행해서 만약 조건문을 통과하면 new_item에 추가될 수 있음.

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# 길이가 4글자나 그 이하인 것으로 만들고 싶을 때,

short_names = [name for name in names if len(name) < 5]
print(short_names)

# 글자 수가 5나 그 이상인 이름들을 모으고 대문자 형식으로 바꾸기.

long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)

# -----------------------------------------
# You are going to write a List Comprehension to create a new list called
# squared_numbers. This new list should contain every number in the list numbers
# but each number should be squared.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [number * number for number in numbers]
print(squared_numbers)

# -----------------------------------------
# 짝수인 숫자만 필터링 해보기.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

even_num = [even for even in numbers if even % 2 == 0]
print(even_num)

# -----------------------------------------
# 겹치는 데이터만 뽑기.

list1 = [1, 2, 3]
list2 = [2, 3, 4]

duplication_num = [dupl for dupl in list1 if dupl in list2]
print(duplication_num)



