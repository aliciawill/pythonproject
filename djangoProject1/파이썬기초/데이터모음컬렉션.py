# 데이터모음: 컬렉션
# 리스트, 튜플, 딕셔너리, 셋
# 우리가족의 나이 모음
age = [100, 88, 33, 17] #이미 알고 있는 경우
ages = [] #age = list() #처음에 모르고 있는 경우
ages.append(300)
ages.append(100)
ages.append(50)
ages.append(17)
print(ages)

#튜플(읽기 전용)
winner = ('김연아', '송연아', '정연아')
# winner[0] = '박연아'
print(winner)

#딕셔너리(사전, 키:값저장)
phone = {1: '010', 2: '011', 3:'019'}
print(phone)
print(phone[1])
print(phone.get(1))



