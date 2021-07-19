N=int(input())
rtg=list(map(int,input().split()))
rnge=list(map(int,input().split()))

maxrating=max(rtg)+1
Sieve=[i for i in range(maxrating+1)]

for x in range(2,int(pow(maxrating,0.5))+1,1):
    if Sieve[x]==x:
        for j in range(x*x,len(Sieve),x):
            Sieve[j]=x

#print("Sieve:{}".format(Sieve))


def factors(x):
    fac=set()
    #print("x:{}".format(x))
    while(x>1):
        fac.add(Sieve[x])
        f=Sieve[x]
        while(x%f==0):
            x=x//f
    return list(fac)

Ans=[0]
for i in range(1,len(rtg)):
    fac=factors(rtg[i])
    cnt=0
    for f in fac:
        for j in range(i-1,i-rnge[i]-1,-1):
            if rtg[j]%f==0:
                cnt+=1 
                break
    Ans.append(cnt)
for c in Ans:
    print("{} ".format(c),end="")

#print(factors(10))

