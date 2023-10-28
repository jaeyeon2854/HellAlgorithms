#소수 구하기


import sys

a, b = map(int, sys.stdin.readline().split())


def primeNumber(a):
    if (a == 1):
        return False;
    else:
        for j in range(2,int(a**0.5)+1):
            if (a%j == 0):
                return False;
        return True;

for i in range(a,b+1):
     if(primeNumber(i)):
          print(i)
          
            
