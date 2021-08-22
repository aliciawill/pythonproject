# 가게2.py
# 실수 입력값을 2개 받아서, 나누기 기능처리를 해보세요.
# (계산기.py를 import)

# 1. 별명을 사용: 함수정의.계산기 대신에 별명 cal만 써도 된다.
# import 함수정의.계산기 as cal

# 2. from이라는 키워드 사용: 경로를 안써도 된다.
from 함수정의.계산기 import div
# from 함수정의.계산기 import div, add
# from 함수정의.계산기 import *


num1 = float(input('숫자입력1>> '))
num2 = float(input('숫자입력2>> '))

# result4 = cal.div(num1, num2)
result4 = div(num1, num2)
print(result4)