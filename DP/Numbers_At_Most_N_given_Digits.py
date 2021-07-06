"""
Date:30/06/2021
902. Numbers At Most N Given Digit Set - Leetcode Hard

The following problem is solved using Dp + combinatorics
"""
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        nstr=[int(nn) for nn in str(n)]
        nlen=len(nstr)
        ans=0
        digits=[int(d) for d in digits]
        lendigit=len(digits)
        digits.sort()
        for i in range(1,nlen):
            ans+=pow(lendigit,i)
        dp=[0]*nlen
        for i in range(nlen-1,-1,-1):
            for j in range(lendigit):
                if digits[j]<nstr[i]:
                    dp[i]+=pow(lendigit,nlen-i-1)
                elif digits[j]==nstr[i]:
                    if i==nlen-1:
                        dp[i]+=1
                        break
                    else:
                        dp[i]+=dp[i+1]
                    break
                else:
                    break
        return dp[0]+ans
                
                    
                            