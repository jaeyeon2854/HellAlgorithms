# dfs 방법
n = int(input())
temp = []

def dfs():
    if len(temp) == n:
        print(*temp)
        return
    for i in range(1, n + 1):
        if i not in temp:
            temp.append(i)
            dfs()
            temp.pop()

dfs()

# permutations함수 사용 방법
import itertools

N = int(input())

num=list(range(1,N+1))

a = itertools.permutations(num,N)

k = list(a)

for i in k:
    p = str(i)
    p = p.replace("(","").replace(",","").replace(")","")
    print(p)