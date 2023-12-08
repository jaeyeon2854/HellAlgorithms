import math

n=int(input())

# 소수 판별
def primenumber(N):
    if N == 1:
        return False
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

# 입력받은 값 절반으로 나누고 소수인지 판별
# 소수 될때까지 두 값 더하고 뺌
for i in range(n):
    num = int(input())

    A = num //2
    B = num //2

    for j in range(num//2):
        if primenumber(A) and primenumber(B):
            print(A,B)
            break
        else:
            A -=1
            B +=1