data = [100, 200, 300] #리스트, 순서를 가진다, 위치값 0시작

print(data[0]) #인덱스
print(data[1])
print(data[2])

for i in range(0, 3): #0, 1, 2
    data[i] = 10 + i
    print(data[i])
#for-each
for x in data: #[100, 200, 300]
    print(x)


