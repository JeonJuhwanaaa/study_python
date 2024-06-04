num1 = 10
num2 = 11

if num2 % 2 == 0:        # 들여쓰기는 : 로 쓴다 / 들여쓰기는 꼭 
    print("짝수입니다")
    print("짝짝짝")

elif num1 == 0:
    print("0입니다")
else:
    print("홀수입니다.")

while num1 < 20:
    print(num1)
    num1 += 1

for num1 in [1,2,3,4,5]:
    print(num1)