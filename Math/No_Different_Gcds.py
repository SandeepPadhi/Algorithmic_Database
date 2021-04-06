class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        
        def gcd(a,b):
            while(b):
                a,b=b,a%b
            return a
        
        numset=set(nums)
        maxn=max(nums)
        ans=0
        for x in range(1,maxn+1):
            curGCD=0
            for num in range(x,maxn+1,x):
                if num in numset:
                    curGCD=gcd(curGCD,num)
                    if curGCD==x:
                        ans+=1
                        break
        return ans
        
        
        """
        import math
        nums=set(nums)
        G=set(nums)
        for n in nums:
            p=set()
            for g in G:
                p.add(math.gcd(g,n))
            G=G.union(p)
        return len(G)
        
        
        """