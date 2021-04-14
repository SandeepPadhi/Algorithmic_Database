"""
Date:14/04/2021
1442. Count Triplets That Can Form Two Arrays of Equal XOR - Leetcode Medium

The following program is solved using prefix-Xor.

If we can divide the array into two equal subarrays having same xor than it implies that 
the xor of array is 0.Hence,no of divisions possible is len_of_array - 1 

"""
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix=[0]
        for i in range(len(arr)):
            prefix.append(prefix[-1]^arr[i])
        count=0
        for i in range(1,len(prefix)):
            for j in range(i+1,len(prefix)):
                if prefix[j]-prefix[i-1]==0:
                    x=j-i+1
                    count+=(x-1)
        return count
                    
        