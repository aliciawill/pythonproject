# 함수(function, 펑션): 기능처리
# print: 출력하다.
# data--입력(input)---->파이썬프로그램---출력(output)-->data2
# 기본입력장치: 키보드
# 기본출력장치: 모니터

# 모니터에 출력하는 기능을 정의
# 기능 정의의 단위: 함수
# 함수를 만드는 것을 "정의"한다

def add(x, y):
    print(x + y, '더하기 기능 처리 구현')
    return x + y #300

def minus():
    pass

a1 = add(200, 100) #300, 함수를 사용, 기능 처리를 하게 됨, 호출
a2 = add(500, 300) #800
a3 = add(a1, a2)
print(a3)