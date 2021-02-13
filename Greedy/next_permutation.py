"""
Date:13/02/2021
Next Permutation -GeeksforGeeks
https://practice.geeksforgeeks.org/problems/next-permutation5226/1#
The following program is solved using greedy approach
"""
class Solution:
    def nextPermutation(self, N, arr):
        # code here
        for i in range(N-1,-1,-1):
            a1=arr[i]
            B=sorted(arr[i+1:])
            
            for j in range(len(B)):
                if B[j]>a1:
                    arr[i],B[j]=B[j],arr[i]
                    arr=arr[:i+1]+sorted(B)
                    return arr
                
        return sorted(arr)
        
