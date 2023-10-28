#소수 찾기

import sys
import math
a = int(sys.stdin.readline());
number = map(int,sys.stdin.readline().split());
count=0

def PrimeNumber(a):
    if (a == 1):
        return False;
    else:
        for i in range(2,int(math.sqrt(a))+1):
            if(a % i == 0):
                return False;
        return True;

for i in number:
    if(PrimeNumber(i)):
        count+=1


print(count)
    