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

# 실제 표처럼 출력이 된다. / 컬럼 명, 인덱스 번호 별로 출력 가능.
# 문자열을 주의해서 사용해야 한다. 컬럼 명이 꼭 일치해야 함. (대소문자 구분 해야함.)
data = pandas.read_csv("weather_data.csv")
# print(data)
print(data["day"]) # 해당 컬럼만 출력 가능.
print(data["temp"]) # 해당 컬럼만 출력 가능.
print(data["condition"]) # 해당 컬럼만 출력 가능.

# 위 코드와 같은 결과를 출력한다.
print(data.day)
print(data.temp)
print(data.condition)

# -----------------------------------------------------
#
# # DataFrame 과 Serise
#
# # DataFrame -> Pandas 에서 기본적으로 전체 표.
# # Serise -> 그 표의 각각의 개별 열들.
#
# print(type(data)) # 데이터타입은 DataFrame
# print(type(data["day"])) # 데이터타입은 Serise
#
# # data 데이터프레임을 딕셔너리로 넣기.
# data_dict = data.to_dict()
# print(data_dict)
#
# # temp 시리즈를 리스트로 담기.
# temp_list = data["temp"].to_list()
# print(len(temp_list)) # list에 담아서 갯수 구하기.
# print(temp_list)
#
# # 온도 열(시리즈)에서 원소 값의 평균 구하기. / mean() 메소드 사용하기.
# temp_aver = data["temp"].mean() # 시리즈 값들의 평균 값
# print(temp_aver)
#
# # 하나의 열(시리즈)에서 최고/최소 값 구하기.
# print(data["temp"].max()) # 최대 값
# print(data["temp"].min()) # 최소 값
#
# # Get Data in Row
# print(data[data.day == "Monday"])
#
# # weather_data.csv 에서 온도가 가장 높은 데이터가 있는 행을 출력.
# print(data[data.temp == data.temp.max()])

# 특정 행의 날씨 상태를 원한다면.
monday = data[data.day == "Monday"]
print(monday.condition)

# 해당 요일의 온도 표시를 섭씨 -> 화씨로 변경
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# -----------------------------------------------------------------------

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

frame = pandas.DataFrame(data_dict)
# print(frame)
frame.to_csv("new_data.csv")