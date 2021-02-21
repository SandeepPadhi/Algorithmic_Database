"""
Date:17/02/2021
1760. Minimum Limit of Balls in a Bag -Lettcode Medium

The following problem is solved using binary search
"""
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low=1
        high=max(nums)
        
        ans=-1
        nums.sort(reverse=True)
        def check(maxval):
            i=0
            K=0
            numstmp=nums
            while(i<len(numstmp) and numstmp[i]>maxval):
                if numstmp[i]>maxval:
                    K+=(ceil(numstmp[i]/maxval)-1)
                i+=1
            if K>maxOperations:
                return False
            return True
        while(low<=high):
            
            mid=(low+high)//2
            if check(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    