# import smtplib
#
# ## ※ 오타 주의 ※
#
# my_email = "juhwan6720@gmail.com"
# password = "wjswnghks6720!!"
#
# # Gmail 일 경우 -> smtp.gmail.com
# # Yahoo 일 경우 -> smtp.mail.yahoo.com
# # 그 외는 Google 에 검색해볼 것. / ex) 네이버 smtp
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # tls 약자 -> Transport Layer Security / 보안
#     # 이메일 서버와의 연결을 안전하게 만드는 방식
#     # 우리가 이메일을 전송할 때 만일 다른 누군가가 전송 과정에서 이메일을 가로채고 읽으려 한다면,
#     # 이게 작동돼서 메세지가 암호화될 것이다.
#     connection.starttls()
#
#     # 로그인
#     connection.login(user=my_email, password=password)
#     # 마지막으로 실제로 이메일을 전송.
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="w7285@naver.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

# --------------------------------------------------------------------------
# << datetime 모듈 >>

# import datetime as dt
#
# now = dt.datetime.now()
# # print(now)
# year = now.year
# # print(type(year))
# if year == 2024:
#     print("Wear a face mask")
# month = now.month
# day_of_week = now.weekday()
# # print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995 , month=6 , day=6)
# print(date_of_birth)

# --------------------------------------------------------------------------
# << Challenge >>

# Objective : send a motivational quote via email on the current weekday (you can change it to Monday afterwards)

# Hint :
# 1. Use the datatime module to obtain the current day of the week.
# 2. Open the quotes.txt file and obtain a list of quotes.
# 3. Use the random module to pick a random quote from your list of quotes.
# 4. Use the smtplib to send the email to yourself.

import smtplib
import datetime as dt
import random

MY_EMAIL = ""
MY_PASSWORD = ""

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0: # if 일요일이라면 이메일을 보내라.
    with open("quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL , to_addrs="", msg="")

# --------------------------------------------------------------------------
