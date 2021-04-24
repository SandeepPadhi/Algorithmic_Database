"""
Date:24/04/2021
546. Remove Boxes - leetcode Hard

The following problem is solved using DP
"""

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i,j,k):
            if i>j:
                return 0
            ii=i+1
            count=1
            while(ii<j+1 and boxes[ii]==boxes[i]):
                count+=1
                ii+=1
            ans=dp(ii,j,0) + (k+count)**2
            for m in range(ii,j+1):
                if boxes[i]==boxes[m]:
                    ans=max(ans,dp(m,j,k+count) + dp(ii,m-1,0))
                    #break
            return ans
        return dp(0,len(boxes)-1,0)
        
        
        
        
        """
        #print(Counter(boxes))
        @lru_cache(None)
        def dp(boxes):
            if len(boxes)<=1:
                return len(boxes)
            freq=Counter(boxes)
            Ones=set()
            for n,c in freq.items():
                if c==1:
                    Ones.add(n)
            ans=0
            boxes=[b for b in boxes if b not in Ones]
            #boxes=list(boxes)
            #ans=0
            i=0
            while(i<len(boxes)):
                j=i
                while(j<len(boxes) and boxes[i]==boxes[j]):
                    j+=1
                l=j-i
                ans=max(ans,l*l + dp(tuple(boxes[:i]+boxes[j:])))
                i=j
            return ans + len(Ones)
            
        return dp(tuple(boxes))
    #[1,3,2,2,2,3,4,3,1,3,3,3,4,4,5,5,5,5,34,7,6,33,66,66,12,12,12,66,66,66,66,66,23,3]
        
        
        """