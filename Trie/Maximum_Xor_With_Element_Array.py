"""
Date:14/04/2021
1707. Maximum XOR With an Element From Array - Leetcode Hard

The following problem is solved using Trie-Prefix Tree using Dictionary
"""


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        root={}
        nums.sort()
        q=[(m,x,i) for i,(x,m) in enumerate(queries)]
        q.sort()
        Ans=[-1]*len(q)
        j=0
        
        def insert(num):
            nonlocal root
            curr=root
            for i in range(31,-1,-1):
                bit=(num>>i)&1
                if bit not in curr:
                    curr[bit]={}
                curr=curr[bit]
            curr['#']=num
        
        def query(num):
            nonlocal root
            curr=root
            Ans=0
            for i in range(31,-1,-1):
                target = ((num>>i)&1)^1
                if target in curr:
                    #Ans+=(1<<i)
                    curr=curr[target]
                else:
                    curr=curr[target^1]
            #print("curr:{}".format(curr))
            Ans=num^curr['#']
            return Ans
        
    
        for m,x,i in q:
            while(j<len(nums) and nums[j]<=m):
                insert(nums[j])
                j+=1
            if j==0:
                continue
            #print(root)
            Ans[i]=query(x)
        return Ans
                