class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        print("len of nums:{}".format(len(nums)))
        ans=1
        right=left=len(nums)-1
        while(left>=0 and right>=0):
            while(left>=0):
                k-=(nums[right]-nums[left])
                if k>=0:
                    ans=max(ans,right-left+1)
                    left-=1
                else:
                    break
            
            #print("left:{},right:{},ans:{},k:{}".format(left,right,ans,k))
            
            if left<0:
                break
            while(right>left and right>=0 and k<0):
                right-=1
                k+=(right-left+1)*(nums[right+1]-nums[right])
            print("after:left:{},right:{},k:{}".format(left,right,k))
            left-=1
            
        
        return ans