def gcd(a, b):
    a, b = min(a, b), max(a, b)
    while b:
        a, b = b, a % b
    return a
 
N = int(input())
 
L = sorted([int(input()) for _ in range(N)])
 
# 인접 요소들의 차(-)를 새 LIST에 추가
NEW_L = list()
for i in range(1, N):
    NEW_L.append(L[i] - L[i-1])
 
# 새 LIST의 모든 요소들의 최대공약수
a = NEW_L[0] 
for i in range(1, N-1):
    a = gcd(a, NEW_L[i])
 
# 처음부터 끝까지 계산하면 시간초과 -> 제곱근을 활용하여 한 번에 값 추가
result = set() #중복값이 있을 수도 있으니 set으로 설정
for i in range(2, int(a**0.5) + 1):
    if a % i == 0:
        result.add(i)
        result.add(a // i)
result.add(a)
print(*sorted(list(result)))