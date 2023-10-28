from collections import deque

d = deque()
print(type(d))

for i in range(10): #덱에 오른쪽에다가 요소 삽입 
    d.append(i)
print(d)

#덱의 왼쪽에다 요소 삽입 
d.appendleft(10)
print(d)

#덱 중간에다가 요소 삽입
d.insert(5,11)
print(d)

# 덱 왼쪽/오른쪽에다 iterable한 객체를 통채로 append하여 연장
d.extend([0,0,0])
print(d)
d.extendleft([0,0,0])
print(d)

#덱의 오른쪽에서 요소삭제
for i in range(10):
    d.pop()
print(d)

#덱의 왼쪽에서 요소 삭제
for i in range(3):
    d.popleft()
print(d)

# 왼쪽으로 밀기
d.rotate(-2)
print(d)

#오른쪽으로 밀기
d.rotate(2)
print(d)

#가장 앞의 요소와 가장 마지막 요소 반황
print(d[0],d[-1])

#비었는지 확인
print(not bool(d))





