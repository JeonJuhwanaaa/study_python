# random 모듈

# import random

# # 1 ~ 10 정수 랜덤 출력
# random_integer = random.randint(1,10) 
# print(random_integer)

# # 0 ~ 1 사이 부동소수점 랜덤 출력
# random_float = random.random()
# print(random_float)

# # 0.000... ~ 4.999... 사이 소수점 랜덤 출력
# random_number = random_float * 5
# print(random_number)

# -------------------------------------------------
# 동전 앞,뒷면 랜덤 굴리기

import random

coin = random.randint(1,2)

if coin == 1:
  print("Tails")
else:
  print("Heads")

# -------------------------------------------------