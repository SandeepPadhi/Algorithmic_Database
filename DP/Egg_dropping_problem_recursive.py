#User function Template for python3

# Function to get minimum number of trials needed in worst
# case with n eggs and k floors

from functools import lru_cache

@lru_cache(None)
def eggDrop(n, k):
    # code here
    if k==0 or k==1:
        return k
    if n==1:
        return k
    min=10000
    for x in range(1,k+1):
        res=max(eggDrop(n-1,k-x),eggDrop(n,x-1))
        if res<min:
            min=res
    return min+1


                
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        print(eggDrop(n,k))
# } Driver Code Ends