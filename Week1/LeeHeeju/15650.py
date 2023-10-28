#n과M
import sys
a,b = map(int,sys.stdin.readline().split(" "))
result=[0]*b
num = [i for i in range(1,a+1)]

def DFS(L,BeginWith):
    if (L == b):
        print(" ".join(map(str,result)))
    else:
        for i in range(BeginWith,len(num)):
            result[L] = num[i]
            DFS(L+1,i+1)
DFS(0,0)
    


        



