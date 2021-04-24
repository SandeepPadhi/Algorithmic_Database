"""
Date:24/04/2021
1793. Maximum Score of a Good Subarray - Leetcode Hard


We have solved the problem using Segment Tree, but it gives TLE
"""
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        
        S=[sys.maxsize]*4*len(nums)
        


        #Below function can also be used as update function by removing comments.
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

        
        
                  