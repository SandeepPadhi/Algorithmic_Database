N,V=map(int,input().split())
R=list(map(int,input().split()))
count={}
for r in R:
	if r not in count:
		count[r]=0
	count[r]+=1
dp=[0]*len(R)
def factorial(n):
	global dp
	if dp[n]>1:
		return dp[n]
	if n==0 or n==1:
		dp[n]=1
		return 1
	dp[n] = n*factorial(n-1)
	return dp[n]
Ans=1
M=(10**9 + 7)
for c in count:
	Ans*=(factorial(count[c])%M)
print(Ans%M)
	