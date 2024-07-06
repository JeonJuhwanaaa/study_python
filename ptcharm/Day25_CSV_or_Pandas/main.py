# csv 파일 리스트로 불러오기.

with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

# -----------------------------------------------------

# << csv 라이브러리 사용. >>
# 한줄로 된 리스트 형식말고 한줄에 한 인덱스 형식으로 가져오기.
# 리스트에서 필요한 데이터만 빼기.

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    # print(data)
    temperatures = []
    for row in data:
        # print(row)
        # temperatures = row[1] # 리스트 형식에서 온도 데이터만 가져오기.
        # print(temperatures)
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# -----------------------------------------------------

# << Pandas 라이브러리 사용. >> (package install 필요)
# https://pandas.pydata.org/docs/ -> 판다스 공식문서.

# 위 csv 라이브러리처럼 data_file로 열 필요도 없고 csv.readr 메소드를 사용할 필요도 없다.

import pandas

# 실제 표처럼 출력이 된다. / 컬럼명, 인덱스 번호 별로 출력 가능.
data = pandas.read_csv("weather_data.csv")
# print(data)
print(data["day"]) # 해당 컬럼만 출력 가능.
print(data["temp"]) # 해당 컬럼만 출력 가능.
print(data["condition"]) # 해당 컬럼만 출력 가능.