"""
Date:16/02/2021
The following problem is solved using hashing.
The idea is to find the occurence of middle variable in the triplet..it will garentee that elements are different and we are not refering to 
two element as same.for ex: -36,18-> there sum is -18 and 18 is also part of array and hence this can be misleading.

The solution to this to find the middle element of the triplet,which is what we have done here.

Link:https://practice.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1#
"""

def findTriplets(arr,n):
    #code here
    lookup={}
    for i in range(n):
        s=set()
        for j in range(i+1,n):
            x=arr[i]+arr[j]
            if -x in s:
                return 1
            else:
                s.add(arr[j])
    return 0
