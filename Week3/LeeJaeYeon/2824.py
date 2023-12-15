n=input().split()
a = list(map(int, input().split()))

m=input().split()
b = list(map(int, input().split()))

def gcd(a, b):
		while b > 0:
					a,b = b, a % b 
		return a

A = 1
B = 1
for i in a:
	A *= i
for i in b:
	B *= i

print(str(gcd(A,B))[-9:])