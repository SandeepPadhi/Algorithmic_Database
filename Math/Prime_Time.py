"""
Date:11/04/2021
Google Codejam-Round 1A
Prime Time
The following problem is solved using sieve of erathonos
"""
import math
Sieve=[i for i in range(50001)]
for i in range(2,int(math.sqrt(50000))+1):
    if Sieve[i]!=i:
        continue
    for j in range(i*i,50001,i):
        Sieve[j]=i
        
T=int(input())

def find():
    Sum=0
    Product=1
    M=int(input())
    Count=[0 for i in range(500)]
    Maxsum=0
    for _ in range(M):
        P,N=map(int,input().split())
        Product*=(P**N)
        Count[P]=N
        Sum+=(P*N)
    Ans=0
    for num in range(2,Sum+1):
        temp=num
        prodsum=0
        done=True
        while(temp>1):
            #print("temp:{}".format(temp))
            s=Sieve[temp]
            if s>499:
                done=False
                break
            
            cnt=0
            while(temp%s==0):
                cnt+=1
                temp//=s
            if Count[s]<cnt:
                done=False
                break
            prodsum+=(s*cnt)
        if done and Sum-prodsum==num:
            Ans=num
    return Ans
            
            
                
        
        

for t in range(1,T+1):
    print("Case #{}: {}".format(t,find()))