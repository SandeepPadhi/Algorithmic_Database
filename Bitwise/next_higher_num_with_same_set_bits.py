"""
Date:1/01/2021
Following code is to find the next higher number with same number of set bits.
1.First we store the indices of all set bits.
2.Then check of second last set bit is just next of last set bit or not.
3.Then accordingly decide what to do.
"""

n=0b110000101
ind=[]
i=1
j=0

def count(n):
    res=0
    while(n):
        rsb=n&-n
        n-=rsb
        res+=1
    return res
k=count(n)
print("k:{}".format(k))
while(i<=n):
    print("while")
    if n&i:
        ind.append(j)
    i<<=1
    j+=1
ans=0
if len(ind)==0:
    print("no possible ")
else:
    if ind[-1]-ind[-2]==1:
        res1=1<<(ind[-1]+1)
        res2=1<<(k-1)
        res2-=1
        ans=res1+res2
    else:
        res1=(1<<ind[-1])
        res2=(1<<(ind[-2]+1))
        res3=1<<(k-2)
        res3-=1
        ans=res1+res2+res3
print("ans:{}".format(bin(ans)))
        

        