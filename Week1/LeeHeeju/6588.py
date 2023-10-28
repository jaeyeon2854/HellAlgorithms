#골드바흐의 추측 
import sys
numList=[True] * (1000001)

for i in range(2,1001):
    if(numList[i]):
         for j in range(i+i,1000001,i):
             numList[j] = False



while(True):
    num= int(sys.stdin.readline())
    if (num == 0):
        break
    a = 2
    b = num-a
    for i in range(2,1000):
        if  numList[a] and numList[b]:
            print(f"{num} = {a} + {b}")
            break
        a+=1
        b-=1
    else:
        print("Goldbach's conjecture is wrong.")


    

