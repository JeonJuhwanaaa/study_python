import pandas

# csv 파일을 가져온 후 pandas 라이브러리로 데이터 가져오기.
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240708.csv")

# Primary Fur Color 컬럼 중 Gray 속성의 데이터만 가져오기.
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]

# 각 색깔 별 갯수 확인하기.
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

# 각 색깔 별 데이터를 가져온 후 컬럼 명 / 속성 / 데이터 값 으로 딕셔너리로 만들기.
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

# 만든 딕셔너리로 csv 파일로 새로 만들기.
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count_csv")