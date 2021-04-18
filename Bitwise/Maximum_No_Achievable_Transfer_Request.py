"""
Date:18/04/2021
1601. Maximum Number of Achievable Transfer Requests - Leetcode Hard

The following problem is solved using bitmasking(Brute Force)
"""
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans=0
        for mask in range(1<<(len(requests))):
            In=[0]*n
            Out=[0]*n
            i=0
            while(mask):
                if mask&1:
                    fr,to=requests[i]
                    In[to]+=1
                    Out[fr]+=1
                mask>>=1
                i+=1
            if In==Out:
                ans=max(ans,sum(Out))
        return ans
            