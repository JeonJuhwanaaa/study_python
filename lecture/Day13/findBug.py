# --------------- FIND DEBUG / 유용한 디버그 팁들 ------------------------

# 1. Describe Problem

# def my_function():
#     for i in range(1,20):
#         if i == 20:
#             print("You got it")

# my_function()

# 여기서 오류가 발생하는 이유 -> range(1,20) 은 1에서 19까지 숫자를 출력한다. 즉, 20 숫자는 출력 xx
# 해결 -> range(1,21) 로 수정해주면 my_function() 호출 시 "You got it" 이 출력될 것이다.

# range 함수를 정확히 알 것!
# 1. range(5) -> 0 에서 5 -1 까지 숫자를 출력 / 0, 1, 2, 3, 4 출력
# 2. range(1,4) -> 1 에서 4 -1 까지 숫자를 출력 / 1, 2, 3 출력
# 3. range(2,6,2) -> 2 에서 5 -1 까지 2만큼 증가하는 숫자를 출력 / 2, 4 출력

# -----------------------------------------------------------------------

# 2. Reproduce the Bug

# from random import randint
# dice_imgs = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
# dice_num = randint(1,6)
# print(dice_imgs[dice_num])

# 오류가 발생하는 이유 -> index 번호가 0부터 5까지인데, dice_num 은 1부터 6 인덱스번호를 출력하게 되있기때문이다.
# 해결 -> randint(0,5) 로 수정해주면 dice_imgs 리스트 안 모든 인덱스번호 포함된다.

# range 함수와 달리 randint 함수는 ()안에 index 번호가 들어가야 한다.

# -----------------------------------------------------------------------

# 3. Play Computer / 컴퓨터의 입장에서 생각해보기

# year = int(input("What's your year of birth?"))

# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# 1994 를 입력 시 아무런 출력이 발생하지 않는 버그 발견
# 비교연산자를 year = 1994 를 추가해주거나 >= 또는 <= 로 수정해주면 해결된다.

# 비교연산자 정확히 알 것!

# -----------------------------------------------------------------------

# 4.Print is your friend.

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of awords per page: "))
# total_words = pages * word_per_page

# print(total_words)

# # 어떤 것이 오류인지 확인하려면 print 함수를 사용해 하나하나 확인해보기

# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_page}")

# 오류가 발생한 이유 -> print(pages) 랑 print(word_per_page) 각각 넣어 확인해보면
# print(pages) 는 잘 입력한대로 출력이 되지만, print(word_per_page) 는 0이 출력돼서 항상 결과 값이 0 으로 출력 되는걸확인할수있다.
# word_per_page 함수에 =(대입)이 아닌 ==(동등 비교연산자) 를 써서 어떤 수를 입력해도 결과는 0 으로 나온다.
# 해결 -> 동등 비교연산자 == 를 = 로 수정해주면 된다.  

# -----------------------------------------------------------------------

# 5. Use a Debugger

# python tutor 사이트를 사용해서 버그 확인하기. / https://pythontutor.com/python-compiler.html#mode=edit

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item) # 여기서 오류 발생 -> for 문 밖에서 new_item 변수를 불러오기 때문

#     print(b_list)

# mutate([1,2,3,5,8,13])

# 오류 발생 이유 -> b_list.append 함수가 for문 안에 있는 new_item 변수를 불러와서 mutate 함수를 호출해도 모든 값들이 출력되지 않았다.
# 해결 -> b_list.append 함수를 for 문 밖이 아닌 안으로 들여쓰기 해주면 해결이 된다.

# 지역변수 / 전역변수 주의할 것!

# -----------------------------------------------------------------------

# 6. Take a Break / 충분한 휴식을 갖고 오류를 찾자.

# -----------------------------------------------------------------------

# 7. Ask a Friend / 주변 동료에게 물어서 오류 찾기.

# 친구에게 코드를 살펴봐달라고 부탁하는 것이 정말 좋은 이유는
# 각자 서로 다른 가정을 하기 때문이다. 즉, 나와는 다른 시각으로 코드를 볼수 있고
# 코드가 어떻게 돌아가는지 매우 명확하게 볼 수 있다.
# 서로서로 도움으로써 서로 배워가며 성장할 수 있다.

# -----------------------------------------------------------------------

# 8. Run Often / 코드를 자주 실행해보고 오류를 확인해보자.

# 코드가 많이 쌓였을 때 실행을 해야 된다. 하지만, 그때 여러 오류가 발생한다면 찾기 힘들다.

# -----------------------------------------------------------------------

# 9. Ask StackOverflow / StackOverflow 사이트를 이용하자.

# StackOverflow 사이트는 다른 개발자들과 의견을 나누기 위해 만들어진 사이트이다.

# -----------------------------------------------------------------------

# 마지막으로 오류 발생하는 것을 두려워하지말자. 누구나 실수를 할수있고 누구나 생길수있는 일이다.
# 버그를 만드는 것이 프로그래머가 되는 길에서 가장 중요한 과정이다.
# 이러한 오류들을 맞이함으로써 나중에 같은 오류가 발생하면 대처할 능력이 생기게되고 경험이 쌓여
# 더 나은 나로 성장할 수 있는 기회가 생긴다.