# Python 에서 Class 만들기

# Class 이름은 파스칼 표기법 사용 (단어 첫 알파벳은 항상 대문자 사용) / ex) ClassName
# 반면 카멜 표기법은 두번째 단어부터 대문자 / ex) className
# 스네이크 표기법 단어와 단어사이 _(언더바) 사용 / ex) class_name

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username # 매개변수와 속성의 이름이 같은 것이 일반적인 관행이지만 무조건은 아니다.
        self.followers = 0
        self.following = 0
        print("new user being created...")

    def follow(self, user): # 클래스 안 메소드는 함수와는 다르게 첫 매개변수로 self 매개변수가 있어야한다.
        user.followers += 1
        self.following += 1

user_1 = User("001", "angela") # 클래스가 새로운 객체를 만들 때마다 __init__ 함수가 호출된다는 것!
# user_1.id = "001"
# user_1.username = "angela"
# print(user_1.username)

print(user_1.followers)

user_2 = User("001", "jack") # 클래스가 새로운 객체를 만들 때마다 __init__ 함수가 호출된다는 것!
# user_2.id = "002"
# user_2.username = "jack"

user_1.follow(user_2) # user_1 이 user_2 를 follow 하겠다
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


# --------------------------------------------------------------------

# Constructor
# 객체 초기화 될 때 변수나 카운터의 시작 값을 지정 가능
# 파이썬에서 생성자를 만들려면 init 함수라는 특별한 함수를 사용해야 한다.

# Ex)
# class Car:
#     def __init__(self):
#     # initialise attributes

# 언더바 두개를 앞 뒤에 붙여 줌.
# 보통 속성을 초기화하는 데 사용된다.
# init 함수 안에서 속성을 초기화하거나 시작 값을 지정합니다.
# 중요한 사실은 이 클래스에서 새로운 객체를 만들 때마다 init 함수가 호출된다는 것이다.

# Ex)
# class Car:
#     def __init__(self, seats):
#         self.seats = seats
#
#     my_car = Car(5)
#     my_car.seats = 5 랑 같은 의미