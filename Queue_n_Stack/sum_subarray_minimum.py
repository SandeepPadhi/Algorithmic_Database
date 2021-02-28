"""
Date:25/02/2021
VERY IMPORTANT
907. Sum of Subarray Minimums - Leetcode Medium

The following program is solved using monotonic stack
"""
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        Ans=0
        stack=[-1]
        Ans=0
        for i in range(len(arr)):
            ind=i
            while(len(stack)>1 and arr[stack[-1]]>arr[i]):
                p=stack.pop()
                right=i-p
                left=p-stack[-1]
                Ans+=(right*left)*arr[p]
            stack.append(i)
            
        while(len(stack)>1):
            p=stack.pop()
            right=len(arr)-p
            left=p-stack[-1]
            Ans+=(right*left)*arr[p]
        M=10**9+7    
        return Ans%M