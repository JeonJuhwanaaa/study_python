from flask import Flask
import time


app = Flask(__name__)

# print(__name__) # __main__ 이 출력된다. ->> 현재 파일 내에서 코드가 실행 중이라는 뜻이다.


@app.route('/') #Python Decorators
def hello_world():
    return "Hello_World!"
#
# # 현재 파일 내에서 코드가 실행 중 이라면.
if __name__ == "__main__":
    app.run()


## Python Decorator Function ->
# 특정 기능을 수행하고, 전달받은 function의 호출을 제어
# 단순히 다른 함수를 감싸 추가 기능을 부여하는 함수.


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after
    return wrapper_function

# 방법1 ) @delay_decorator 표시해주기.
# Decorator function.
@delay_decorator
def say_hello():
    print("Hello")

@app.route('/bye')
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

say_bye()

# 방법2 ) 직접적으로 함수 안에 감싸주기.
decorated_function = delay_decorator(say_greeting)
decorated_function()