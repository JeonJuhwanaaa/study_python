age: int
name: str
height: float
is_human: bool

# Type Hints : 화살표를 사용하여 리턴형태가 어떤 타입으로 되어있는지 힌트를 준다.
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive
    # return "ABCDEFG" # 이런 경우 Type Hint 를 boolean 타입으로 지정했는데 String 으로 마무리하고있어서 에러발생.

# print(police_check(19))

if police_check(19):
    print("You may pass.")
else:
    print("Pay a fine.")

