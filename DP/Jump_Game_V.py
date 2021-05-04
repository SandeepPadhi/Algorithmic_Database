"""
Date:4/05/2021
1340. Jump Game V - Leetcode Hard

The following program is solved using DP and Sorting
"""

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        Ans=[1]*len(arr)
        N=len(arr)
        
        Arr=[[arr[i],i] for i in range(N)]
        Arr.sort(reverse=True)
        
        for _,i in Arr:
            j=i-1
            while(j>=0 and abs(i-j)<=d and arr[j]<arr[i]):
                Ans[j]=max(Ans[j],Ans[i]+1)
                j-=1
            j=i+1
            while(j<N and abs(j-i)<=d and arr[j]<arr[i]):
                Ans[j]=max(Ans[j],Ans[i]+1)
                j+=1
        return max(Ans)