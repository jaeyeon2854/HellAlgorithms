#골드바흐의 추측
import sys

num = 10000
numList = [True] * (num+1)

def isPrime():
    for i in range(2,num+1):
        if(numList):
            for j in range(i*2,num+1,i):
                numList[j] = False;

isPrime()

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a,b = n//2,n//2
    while a >1:
        if (numList[a] and numList[b]):
            print(a,b)
            break
        else:
            a-=1
            b+=1



# n = int(sys.stdin.readline())
# for i in range(n):
#     sum = 0
#     a = int(sys.stdin.readline())
#     for j in range(2,num+1):
#         if(numList[j]):
#             sum = a - j
#             if (numList[sum]):
#                 print(j, sum)
#                 break

