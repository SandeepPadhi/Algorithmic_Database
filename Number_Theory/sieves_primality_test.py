import math
maxn=1000000
spf=[i for i in range(maxn+1)]

def sieve(spf):
    for i in range(2,int(math.sqrt(maxn))+1,1):
        if spf[i]==i:
            for j in range(i*i,maxn+1):
                spf[j]=i
def isPrime(x):
    return True if spf[x]==x else False

sieve(spf)

print(isPrime(31))