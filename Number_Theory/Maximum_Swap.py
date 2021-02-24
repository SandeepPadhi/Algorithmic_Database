"""
Date:23/02/2021
The following program solved using simple maths.
Solved using loops+hashing by storing occurances of numbers and swipping the numbers from left to right in descending order of maxvalues
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        lookup={}
        nums=[n for n in str(num)]
        for i in range(len(nums)):
            n=nums[i]
            if n not in lookup:
                lookup[n]=[]
            lookup[n].append(i)
        i=0
        for curmax in sorted(lookup.keys(),reverse=True):
            while(i<len(nums) and nums[i]==curmax and len(lookup[curmax])>0):
                lookup[nums[i]].pop(0)
                i+=1
            if len(lookup[curmax])==0:
                continue
            index=lookup[curmax][-1]
            nums[i],nums[index]=nums[index],nums[i]
            break
        #print(nums)
        Ans=0
        for n in nums:
            Ans*=10
            Ans+=int(n)
        return Ans
            
        