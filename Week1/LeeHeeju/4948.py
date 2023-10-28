import sys

num = 123456*2+1
numList=[1]*num; #모두 소수라고 일단 생각

#에라토스테네스의 소수 구하기 방법
for i in range(2,num):
    if(numList[i] == 1):
        for j in range(i*2,num,i):
            numList[j] = 0;


while(True):
    n = int(sys.stdin.readline())
    count=0
    if(n == 0):
        break
    for i in range(n+1,2*n+1,1):
        count+=numList[i]
    print(count)


    




# # 시간초과
# while (True):
#     n = int(sys.stdin.readline());
#     count = 0

#     if(n == 0):
#         break;
#     else:
#         for i in range(n+1,2*n+1):
#             isPrime = True
#             for j in range(2,int(math.sqrt(i))+1):
#                 if(i % j == 0):
#                     isPrime=False
#                     break;
#             if(isPrime==True and i > 1):
#              count+=1
            
#     print(count)



      
