"""
Date:6/02/2021
The following problem is solved using recursion
"""
#User function Template for python3

# Function to get minimum number of trials needed in worst
# case with n eggs and k floors
def eggDrop(n,k):
    if k==1 or k==0:
        return k
    if n==1:
        return k
    lookup=[[10000 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(k+1):
        lookup[i][1]=i
    for i in range(1,n+1):
        lookup[1][i]=1
        lookup[0][i]=0
    for floor in range(2,k+1):
        for egg in range(2,n+1):
            #min=10000
            for x in range(1,floor):
                res=1+max(lookup[floor-x][egg],lookup[x-1][egg-1])
                lookup[floor][egg]=min(lookup[floor][egg],res)
    return lookup[-1][-1]
                
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