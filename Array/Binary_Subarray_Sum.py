"""
Date:4/02/2021
930. Binary Subarrays With Sum - Leetcode Medium

The following problem is solved using simple permutation - combination techinque
The idea:
1) S>0:
    then we have to just 1st and Sth '1' in the array starting from some index i which has A[i]=1.
    then ,we just have to find the number of zeros to the left of 1st ones and to the right of last 1 and mulplitply them
    

2)S==0:
then simply apply formula n*(n+1)/2 between any two 1's,when n is the distance between any two 1's
"""

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        
        def find1(A):
            #If S>1
            I=[i for i in range(len(A)) if A[i]==1]
            cnt=0
            print(I)
            for i in range(len(I)):
                if i+S-1<len(I):
                    j=i+S-1
                    if i==0:
                        left=I[i]+1
                    else:
                        left=I[i]-I[i-1]
                    if j==len(I)-1:
                        right=len(A)-I[j]
                    else:
                        right=I[j+1]-I[j]
                    cnt+=left*right
                else:
                    break
            return cnt
        
        def find0(A):
            cnt=0
            I=[i for i in range(len(A)) if A[i]==1]
            I=[-1]+I+[len(A)]
            for left in range(len(I)-1):
                right=I[left+1]
                d=right-I[left]-1
                cnt=cnt + d*(d+1)//2
            return cnt
        return find0(A) if S==0 else find1(A)
                
                