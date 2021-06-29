"""
Date:27/06/2021

The idea here is to store prefix sum of count.But here we are only interested in 
knowing odd or even count.So we use bitmaxking to represent the count.

We then use Hashing to find those count.
Odd-Odd=even
Even-Even=even
Even-odd=odd
odd-even=odd
"""
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        total=0
        lookup=collections.defaultdict(int)
        lookup[0]=1
        cur=0
        for c in word:
            c=ord(c)-ord('a')
            cur^=(1<<c)
            total+=lookup[cur]
            for j in range(10):
                delta=cur^(1<<j)
                total+=lookup[delta]
            
            lookup[cur]+=1
            
    
        return total