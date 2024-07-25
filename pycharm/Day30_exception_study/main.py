## << Exception Errors >>

# 💡FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# -------------------------------------------------------------------------
# 💡KeyError

# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]
# -------------------------------------------------------------------------
# 💡IndexError

# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]
# -------------------------------------------------------------------------
# 💡TypeError

# text = "abc"
# print(text + 5)
# -------------------------------------------------------------------------

# 💡try : 예외를 유발할 수 있는 뭔가를 실행하는 코드 블록
# 💡except : try에서 실행한 코드 블록이 예외가 있다면 실행하는 코드 블록
# 💡else : 예외가 없었을 때 실행할 코드를 정의
# 💡finally : 기본적으로 어떤 일이 일어나더라도 항상 실행해야 할 코드

# try: # 우선 코드 실행 시도.
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["asdasd"])
# except FileNotFoundError: # 혹시 try 문에서 FileNotFoundError 가 발생 시 실행.
#     # print("There was an error")
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message: # 혹시 try 문에서 KeyError 가 발생 시 실행.
#     print(f"That key {error_message} does not exist.")
# else: # try 문에서 예외 발생 하지 않을 때 실행.
#     content = file.read()
#     print(content)
# finally: # try 문에서 예외가 발생하든 말든 무조건 실행.
#     file.close()
#     print("File was closed.")

# -------------------------------------------------------------------------
# 💡 << Raising Exceptions >>
# 의도적으로 예외를 발생시켜 예외처리하는 것.

# raise 예외종류(예외 메세지)

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
