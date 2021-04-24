"""
Date:24/04/2021
1793. Maximum Score of a Good Subarray - Leetcode Hard

We have solved the problem using greedy approach.

We notice that the subarray will always contain kth element.So we must start from kth element and expand left or right.
We choose left or right depending upon which ever is greater.The reason for choosing greater is that it will have less impact on the minimum value of subarray

"""
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        maxscore=nums[k]
        minval=nums[k]
        
        i=k
        j=k
        while(i>=0 or j<len(nums)):
            if i==0:
                while(j<len(nums)):
                    minval=min(minval,nums[j])
                    maxscore=max(maxscore,minval*(j-i+1))
                    j+=1
                break
            elif j==len(nums)-1:
                while(i>=0):
                    minval=min(minval,nums[i])
                    maxscore=max(maxscore,minval*(j-i+1))
                    i-=1
                break
            else:
                if nums[i-1]>nums[j+1]:
                    i-=1
                    minval=min(minval,nums[i])
                    maxscore=max(maxscore,minval*(j-i+1))
                else:
                    j+=1
                    minval=min(minval,nums[j])
                    maxscore=max(maxscore,minval*(j-i+1))
        return maxscore
        
        
        
        """
        
        Note:We have attempted to solve the below problem using segment Trees but gives TLE

        
        S=[sys.maxsize]*4*len(nums)
        
        def build(segpos,left,right):
            if left==right:
                S[segpos]=nums[left]
                return 
            mid=(left+right)//2
            #if pos<=mid:
            build(2*segpos,left,mid)
            #else:
            build(2*segpos+1,mid+1,right)
            S[segpos]=min(S[2*segpos],S[2*segpos+1])
        
        
        def query(segpos,segleft,segright,left,right):
            if left>right:
                return sys.maxsize
            if segleft==left and segright==right:
                return S[segpos]
            
            segmid=(segleft+segright)//2
            v1=query(2*segpos,segleft,segmid,left,min(segmid,right))
            v2=query(2*segpos+1,segmid+1,segright,max(segmid+1,left),right)
            return min(v1,v2)
        
        
        build(1,0,len(nums)-1)
        
        #print("min val:{}".format(query(1,0,len(nums)-1,3,len(nums)-1)))
        
        
        Ans=-1
        for i in range(k+1):
            for j in range(k,len(nums)):
                minval=query(1,0,len(nums)-1,i,j)
                Ans=max(Ans,minval*(j-i+1))
        return Ans

        
        
        """                