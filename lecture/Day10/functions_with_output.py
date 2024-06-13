# Functions with Output

# .title() -> 문자열 첫번째 알파벳만 대문자로 나머진 소문자 변형

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    # 1. print() 로 출력 방법
    # print(f"{formated_f_name} {formated_l_name}")

    # 2. return 으로 출력 방법
    return f"{formated_f_name} {formated_l_name}"

# 1. print() 로 출력하는 경우 호출방법
# format_name("AnGElA", "YU")

# 2. return 으로 출력하는 경우 호출방법
formated_string = format_name("AnGElA", "YU")
print(formated_string)

# 컴퓨터는 return 함수를 만나면 그 함수 호출 끝으로 여긴다.
# 즉, return 값 뒤에 다른 코드를 입력해도 컴퓨터는 인식 안하고 끝낸다.

# -----------------------------------------------------------------------------------------------------

# Days in month

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1]
  

  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)



