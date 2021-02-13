"""
Date:13/02/2021
Minimize the Heights II - GeeksforGeeks
https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1#
"""
class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        mindiff=arr[-1]-arr[0]
        for i in range(1,n):
            minval=min(arr[0]+k,arr[i]-k)
            maxval=max(arr[i-1]+k,arr[-1]-k)
            if minval<0:
                continue
            mindiff=min(mindiff,maxval-minval)
        return mindiff
