# 함수

def add(num1, num2):
    return num1 + num2

result1 = add(10, 20)
print(result1)

def add(num1, num2, num3, num4):
    return num1 + num2, num3 + num4     # 리턴은 하나의 값만 받아야하는데, 파이썬은 두개의 값도 가능하다

result2 = add(10, 20, 30, 40)           # 하나의 함수에 2개의 리턴 값을 받으면 tuple로 묶여서 나온다
print(result2)
# print(result3)

r1, r2 = (1, 2)                         # 비구조 할당이 된다
print(r1, r2)

nums = [5,2,7,3,1]
nums.sort()
nums.reverse()
print(nums)

name = "전주환"
print(name.find("주"))
print(name.find("황"))                  # 없는 것일땐 -1

# print(nums.index(10))

user = {
    "username": "testuser",
    "password": "1234",
    "name": "전주환",
    "email": "test@naver.com"
}

print(user)
user.update({                           # dict 으로 넣어줄 것
    "phone": "010-0000-0000",
    "name": "전주황"    
})
user["age"] = 30
print(user)