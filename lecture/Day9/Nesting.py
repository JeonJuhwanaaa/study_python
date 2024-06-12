# << python Nesting >>

# ex) Value 자리에 [] / {} 가 중첩으로 존재
# {
#     Key: Value,
#     Key: [List],
#     Key: {Dict}   
# }

# -----------------------------------------------------------------------------------------------------

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berilin"
}

# Nesting a List in a Dictionary

travel_log = {
    # "France": "Paris", "Lille", "Dijon" - 쉼표로 구분해서 쓰면 하나당 값은 하나만 가능하므로 오류가 발생한다.
    # 대신 세 문자열을 대괄호로 묶어주어서 리스트로 만들어 하나의 값으로 바꿔주면 된다.
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# 중첩이라는 개념은 dictionary에만 있는 것은 아니다.
# 리스트안에 리스트를 중첩할 수도 있다.

# ex) ["A", "B", ["C", "D"]]

# -----------------------------------------------------------------------------------------------------
# 과제 - "France"  키 안에 dictionary를 만들고 "cities_visited" 라는 키 안에 ["Paris", "Lille", "Dijon"] 리스트 넣어주기

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# -----------------------------------------------------------------------------------------------------
 
#Nesting Dictionary in a List

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]

# -----------------------------------------------------------------------------------------------------

# << List 안에 Dictionary 값 추가 하기 >>

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 

def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")