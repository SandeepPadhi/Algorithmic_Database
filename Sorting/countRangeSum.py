"""
Date:12/04/2021
327. Count of Range Sum - Leetcode Hard

The following problem is solved using Mergesort

"""
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix=[0]
        for n in nums:
            prefix.append(prefix[-1]+n)
        
        def Mergesort(low,high,Prefix):
            if low==high:
                return 0
            cnt=0
            mid=(low+high)//2
            cnt=Mergesort(low,mid,Prefix)+Mergesort(mid+1,high,Prefix)
            
            i=j=mid+1
            for left in Prefix[low:mid+1]:
                while(i<=high and Prefix[i]-left<lower):
                    i+=1
                while(j<=high and Prefix[j]-left<=upper):
                    j+=1
                cnt+=(j-i)
            Prefix[low:high+1]=sorted(Prefix[low:high+1])
            return cnt
        return Mergesort(0,len(prefix)-1,prefix)
            
        
        
        
        """
        The following problem is solved using Hashing

        
        hashmap=defaultdict(lambda:0)
        prefix=[0]
        cnt=0
        hashmap[0]=1
        for n in nums:
            prefix.append(prefix[-1]+n)
            for target in range(lower,upper+1):
                cnt+=hashmap[prefix[-1]-target]
            hashmap[prefix[-1]]+=1
                
        
        return cnt
        
        
                    
        
        """