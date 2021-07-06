"""
Date:14/04/2021
1739. Building Boxes - Leetcode Hard

The following problem is solved maths logic

The maximum of boxes that can be stored with diameter n = n*(n+1)*(n+2)//6
"""
class Solution:
    def minimumBoxes(self, n: int) -> int:
        
        n=10
        ans1=0
        cur=0
        while(cur<n and cur+(ans1+1)*(ans1+2)//2<=n):
            ans1+=1
            cur+=ans1*(ans1+1)//2

        rem_n=n-cur
        ans2=0
        while(ans2*(ans2+1)//2<rem_n):
            ans2+=1

        ans=ans1*(ans1+1)//2 + ans2
        #print(ans)
        return ans
    


        """


        curr=ans1=ans2=0
        
        while(curr+(ans1+1)*(ans1+2)//2 <= n):
            curr+=(ans1+1)*(ans1+2)//2
            ans1+=1
            
        while(curr<n):
            ans2+=1
            curr+=ans2
            
        return ans1*(ans1+1)//2 + ans2

        """


