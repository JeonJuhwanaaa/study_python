number = 10
print(type(number))

print(id(10))
print(id(number))

# id() 는 주소 값을 출력

number += 1
print(id(number))

number -= 1
print(id(number))

print(type("test"))

print(type([]))     # List  -   # [] 배열은 항상 List / (Array 아님)
print(type(()))     # tuple -   tuple 에는 상수라서 추가, 삭제, 수정 불가
print(type({}))     # dict

# 변수타입 입력 없이 변수명 입력하면 자동적으로 타입을 정해줌

print([1,2,3,4])
print((1,2,3,4))
print({"id": 1, "name": "전주환"})

list1 = [1,2,3,4]
tp = (5,6,7,8)
dict1 = {"id": 1, "name": "전주환"}

print(list1[0])
print(tp[0])
print(dict1["id"])   # key 값 넣기

list1.append(5)      # add 와 같음 - 끝이 하나씩 추가
print(list1)

list1.append(5)
print(list1)
print(tp.index(7))
list2 = list(tp)

print(list2)
print(dict1.keys())
print(dict1.values())

print(dict1.items())
print(list(dict1.items())[0])   # 형변환해서 인덱스 가져오기

print(True)     # 무조건 대문자로 시작해야 함
print(False)    # 무조건 대문자로 시작해야 함