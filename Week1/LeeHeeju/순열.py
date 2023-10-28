#순열
def DFS(L):
        #종료조건
        if (L == r):
            print(result)
        else:
              for i in range(len(n)):
                    if checklist[i] == 0 :
                          result[L] = n[i]
                          checklist[i] = 1
                          DFS(L+1)
                          checklist[i]=0


n = [1,2,3]
r= 2

result = [0]*r
checklist = [0]*len(n);
DFS(0)




