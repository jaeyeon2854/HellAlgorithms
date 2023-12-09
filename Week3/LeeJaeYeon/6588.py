import sys

input = sys.stdin.readline

r = 1000000

check = [True for _ in range(r)]

for i in range(2, int(r**0.6)):
    if check[i] == True:
        for j in range(i*2, r, i):
            if check[j] == True:
                check[j] = False # 에라토스테네스의 체
while True:
    n = int(input())
    flag=0
    if n == 0:
        break
    for i in range(3, n-2,2): # 입력받은 수가 에라토스테네스의 체에 속하는지, 즉 소수인지
        if check[i] == True:
            if check[n-i] == True:
                print("{} = {} + {}".format(n,i, n-i))
                flag=1
                break
    if flag ==0 :
        print("Goldbach's conjecture is wrong.")