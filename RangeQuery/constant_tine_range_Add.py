"""
Date:28/01/2021
The following problem is solved by adding num so that it is applied to all indices to
its right.Hence,num is substracted from index r-1 so that its effect gets nullified

link:https://www.geeksforgeeks.org/constant-time-range-add-operation-array/
"""

S=[0 ,0, 0, 0, 0, 0, 0, 0, 0, 0]

def add(num,l,r):
    global S
    S[l]=S[l]+num
    if r+1<len(S):
        S[r+1]=S[r+1]-num
add(10,2,5)
add(10,2,5)
add(20,2,5)
add(20,2,5)
import math
for i in range(1,len(S)):
    S[i]+=S[i-1]
    S[i]=math.ceil(S[i])
print(S)

"""
Output:
[0, 0, 60, 60, 60, 60, 0, 0, 0, 0]

"""