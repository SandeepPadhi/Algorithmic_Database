
"""
Date:18/03/2021
1552. Magnetic Force Between Two Balls - Leetcode Medium

The following program is solved using Binary Search

Here,one thing is realise is that first ball will always be at the earliest position and
last ball will always be at last position.

For rest ,we have to apply binary search ,where in every iteration we set minimum force.
If minimum force is satisfied we move the limit up and so on...

"""

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        N = len(position)
        position.sort()
        m-=2
        low,high = 1 , position[-1]
        ans = position[-1] - position[0]
        
        def check(M):
            count = m
            i=1
            prev = position[0]
            while(count and i<N-1):
                if position[i]-prev>=M:
                    count-=1
                    prev=position[i]
                i+=1
            
            if count==0 and position[-1] - prev>=M:
                return True
            return False
                
                
        
        while(low<=high):
            mid = (low + high)//2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
        
        