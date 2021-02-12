"""
Date:1/01/2021
Following program is called Kanjans Algorithm for counting no of set bits in number

"""

n=0b101011101
def count(n):
    res=0
    while(n):
        rsb=n&-n
        n-=rsb
        res+=1
    return res
ans=count(n)
print(ans)