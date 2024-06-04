print(__name__)

# from calculation.addition import add1, add2
# from calculation.subtraction import sub1, sub2

import calculation.addition as addtion          # as 사용 가능
import calculation.subtraction as subtraction

# 안에 from을 넣으면 메인일 때만  
if __name__ == "__main__":
    # from calculation.addition import add1
    # from calculation.subtraction import sub1
    result1 = calculation.addition.add1(10, 20)         # import 자체를 통째로 가져와서 쓰는 방법
    result2 = subtraction.sub1(50, 10)                  # as 사용한 걸 사용

    print(result1)
    print(result2)