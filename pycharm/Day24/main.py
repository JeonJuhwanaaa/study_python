# 파일을 Read 하고 싶다면.

# file = open("my_file.txt")
# contents = file.read() # read 메소드는 파일의 컨텐츠를 문자열로 반환해준다.
# print(contents)

# # 우리가 열엇던 파일에서 모든 일이 끝나고 나면 파일을 닫아줘야한다.
# # 이유는 컴퓨터가 최고의 성능을 발휘하기 위함
# file.close()

# # ------------------------------------------
# # with 함수 사용 시 위 방법처럼 opne / close 를 굳이 사용할 필요가 없어진다.

with open("my_file.txt") as file:
    contents = file.read() # read 메소드는 파일의 컨텐츠를 문자열로 반환해준다.
    print(contents)


# -------------------------------------------
# 파일을 쓰고 싶다면. / 파일을 만들고 싶다면.

with open("new_file.txt", mode="w") as file:
    file.write("\nNew text.")