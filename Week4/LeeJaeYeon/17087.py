def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n,s=map(int,input().split())
arr = list(map(int, input().split()))

dis = []
for i in range(n):
    dis.append(abs(s - arr[i]))
#print(dis)

ans=dis[0]
for i in dis:
	ans=gcd(i,ans)
print(ans)
		