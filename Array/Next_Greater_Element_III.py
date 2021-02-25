"""
Date:25/02/2021
556. Next Greater Element III - Leetcode  Medium

The following program is solved using some logic,sorting
"""
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        N=[]
        tmp=n
        while(tmp):
            N.append(tmp%10)
            tmp//=10
        N.reverse()
        i=len(N)-1
        while(i-1>=0 and N[i-1]>=N[i]):
            i-=1
            
        if i-1>=0:
            N=N[:i]+sorted(N[i:])
            j=i
            while(j<len(N) and N[i-1]>=N[j]):
                j+=1
            if j<len(N):
                N[i-1],N[j]=N[j],N[i-1]
            
        newn=0
        for i in range(len(N)):
            newn*=10
            newn+=N[i]
            
            
        return -1 if newn==n or newn>2**31-1 else newn
        