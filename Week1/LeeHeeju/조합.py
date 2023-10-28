
def DFS(L,BeginWith):
    if (L == r):
        print(result)
    else:
        for i in range(BeginWith,len(n)):
            result[L]=n[i]
            DFS(L+1,i+1)


n = [1,2,3]
r = 2
result =[0]*2
DFS(0,0) #level,BeginWith