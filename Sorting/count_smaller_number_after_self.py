"""
Date:12/04/2021
315. Count of Smaller Numbers After Self - Leetcode Hard

IMPORTANT

The following problem is solved using Merge Sort
"""


class Solution:
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        def merge(Res,Aux,Arr,low,mid,high):
            for i in range(low,high+1):
                Aux[i]=Arr[i]
            
            i,j=low,mid+1
            for k in range(low,high+1):
                if i>mid:
                    Arr[k]=Arr[j]
                    j+=1
                elif j>high:
                    Arr[k]=Aux[i]
                    Res[Aux[i][0]]+=(k-i)
                    i+=1
                elif Aux[i][1]<=Aux[j][1]:
                    Arr[k]=Aux[i]
                    Res[Aux[i][0]]+=(k-i)
                    i+=1
                else:
                    Arr[k]=Aux[j]
                    j+=1
        
        def sort(Res,Aux,Arr,low,high):
            if low>=high:
                return
            mid=(low+high)//2
            sort(Res,Aux,Arr,low,mid)
            sort(Res,Aux,Arr,mid+1,high)
            merge(Res,Aux,Arr,low,mid,high)
        
        Res=[0]*len(nums)
        Aux=[0]*len(nums)
        Arr=list(enumerate(nums))
        sort(Res,Aux,Arr,0,len(nums)-1)
        return Res
        
        
        
        
        
        
        
        
        
        
        """
        count=[0]
        Sorted=[nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            ans=bisect.bisect_left(Sorted,nums[i])
            count.append(ans)
            Sorted.insert(ans,nums[i])
        
        count.reverse()
        return count
        """