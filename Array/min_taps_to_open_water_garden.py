"""
Date:14/02/2021

1326. Minimum Number of Taps to Open to Water a Garden - Leetcode Hard


The following problem was solved using sorting and Stack.
First Sort as per starting time.
Then ,remove unnecessary elements in one iterations
"""

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        R=[]
        for i in range(n+1):
            R.append((max(0,i-ranges[i]),min(n,i+ranges[i])))
        R.sort(key=lambda x:(x[0],-x[-1]))
        i=1
        while(i<len(R)):
            if i>1:
                if R[i][0]<=R[i-2][1] and R[i][1]>R[i-1][1]:
                    R.pop(i-1)
                    i-=1
                elif R[i-1][1]<R[i][1] and R[i-1][1]>=R[i][0]:
                    i+=1
                else:
                    R.pop(i)
            else:
                if R[i-1][1]<R[i][1] and R[i-1][1]>=R[i][0]:
                    i+=1
                else:
                    R.pop(i)
            #print("R:{}".format(R))
        #print("R:{}".format(R))
        if R[-1][1]==n:
            return len(R)
        return -1
