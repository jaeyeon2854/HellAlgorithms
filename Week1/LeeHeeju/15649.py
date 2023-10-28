import sys

a,r = map(int,sys.stdin.readline().split());


def DFS(L):
    if(L == r):
        print (' '.join(map(str,result)))
    else:
        for i in range(len(n)):
            if(checklist[i] == 0):
                result[L] = n[i]
                checklist[i] = 1
                DFS(L+1)
                checklist[i] = 0
 

n = [i for i in range(1,a+1)];
checklist = [0]*a;
result =[0]*r;
DFS(0)