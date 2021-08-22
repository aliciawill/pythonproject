# 파이썬에서는 파이썬 파일 하나를 모듈로 본다.

# 계산기는 산술연산자 기능을 가지고 있어야한다.
# 기능은 함수로 정의한다.
def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y # /나누기 연산자할 때, 소수점까지 구해준다.
    #return x // y # //나누기 연산자할 때, 소수점을 버린다.


#계산기.py모듈을 혼자 실행한다면, main 안에 있는 문장들을 실행해주세요.
if __name__ == '__main__':
    result1 = add(200, 100) #300, 함수사용(호출한다, call)
    # 함수는 호출할 때 실행된다.!
    result2 = add(300, 200) #500

    print('resutl1', result1)
    print('resutl2', result2)
    # run: 컨트롤+쉬프트+f10

    # 자동완성기능 : 컨트롤+스페이스바
    if result2 > 400:
        print('숫자가 아주 커요.')
    else:
        print('숫자가 아주 작아요.')


    # 입력받을 때 컴퓨터는 데이터타입을 인식못한다. 무조건 문자열(string,  스트링)으로 인식한다.
    # 컴퓨터가 모듈내에 가지고 데이터의 타입을 변환하고자 하는 경우에는
    # 프로그래머가 변환해서 사용한다.
    n1 = int(input('숫자1를 입력>> ')) #'300'
    n2 = int(input('숫자2를 입력>> ')) #'100'
    print(add(n1, n2))

    