# *args / Unlimited Positional Arguments 라 불림 -> 인수를 얼마든지 받아들일수 있다.

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2, 4, 5, 6, 7, 7))


# **kwargs -> keyword arguments
# 기본적으로 딕셔너리 형식을 가진다.
def calculate(n, **kwargs):
    # print(kwargs) - dict 형식
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car)
