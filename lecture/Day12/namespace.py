# 전역변수 / 지역변수 이해

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemiss inside function: {enemies}") # 2 출력


# increase_enemies()
# print(f"enemiss inside function: {enemies}") # 1 출력


# -------------------------------------------------------------------

# Local Scope / 지역 변수

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion() # 지역변수 호출

# print(drink_potion) # 전역변수 호출

# -------------------------------------------------------------------

# Global Scope / 전역 변수

# player_health = 10 # 전역 변수

# def game():
#     def drink_potion():
#         potion_strength = 2 # 지역 변수
#         print(player_health)

#     drink_potion()

# print(player_health)

# -------------------------------------------------------------------

# There is no Block Scope / C++ 이나 Java 경우 있지만 Python 에는 없다.

# game_level = 3

# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
    
#     print(new_enemy)

# -------------------------------------------------------------------

# How to Modify Variables with Global Scope

# Modifying Global Scope

# enemies = 1

# def increase_enemise():
#     global enemies # 2.  전역 변수를 가지고 있다고 명시해야 한다.
#     enemies += 1 # 1. 전역 변수랑 같은 변수이름을 수정하려고 한다면
#     print(f"enemies inside function: {enemies}")

# increase_enemise()
# print(f"enemies inside function: {enemies}")

# 이런 식으로 한다면 번거롭기도하고 헷갈리기 쉬움
# 지역 범위를 가진 함수 내부에서는 수정하지말고 대신 무엇을 할 수 있을끼?
# enemies의 수를 변경하는 함수같은 기능을 가지려면
# 함수 내부에서 전역 범위를 수정하지 않고 어떻게 이것이 가능 할까?
# 반환문을 적용하자. / return 함수

# enemies = 1

# def increase_enemise():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# enemies = increase_enemise()
# print(f"enemies inside function: {enemies}")

# -------------------------------------------------------------------

# Python Constants & Global Scope / 전역 상수(변하지 않는)

PI = 3.14159
URL = "https://www.google.com"

# Constant (상수) 는 Python의 명명 규칙은 모두 < 대문자 > 로 바꾸는 것.

# -------------------------------------------------------------------

