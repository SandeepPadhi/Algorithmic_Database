"""
Date:18/04/2021
1830. Minimum Number of Operations to Make String Sorted - Leetcode Hard

The following program is solved using combinatorics.
We also use the concept of multiplicative inverse ,ferment's theorem and Euler theorem
"""
class Solution:
    def makeStringSorted(self, s: str) -> int:
        n=len(s)
        mod=10**9 + 7
        fac=[0]*n
        invfac=[0]*n
        fac[0]=1
        invfac[0]=pow(1,mod-2,mod)
        for i in range(1,n):
            fac[i]=(i*fac[i-1])%mod
            invfac[i]=pow(fac[i],mod-2,mod)
        
        cnts=[0]*26
        total=0
        ans=0
        for c in s[::-1]:
            num=ord(c)-97
            cnts[num]+=1
            for i in range(num):
                if cnts[i]>0:
                    cnts[i]-=1
                    op=fac[total]
                    for j in range(26):
                        if cnts[j]>0:
                            op*=invfac[cnts[j]]
                            op%=mod
                    
                    cnts[i]+=1
                    ans+=op
                    ans%=mod
            total+=1
        return ans