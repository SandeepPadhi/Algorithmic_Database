"""
Date:3/04/2021
978. Longest Turbulent Subarray - Leetcode Medium

The following problem is solved using Dp + loop
"""
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        Sign=[]
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                Sign.append(0)
            elif arr[i]<arr[i+1]:
                Sign.append(-1)
            else:
                Sign.append(1)
        Equal=True
        maxlen=1
        l=0
        prev=-1
        print(Sign)
        for s in Sign:
            if (s==0):
                #print("s=0")
                Equal=True
            elif Equal:
                #print("start")
                prev=s
                Equal=False
                l=2
            else:
                if prev*s<0:
                    l+=1
                else:
                    maxlen=max(maxlen,l)
                    l=2
                prev=s
            maxlen=max(maxlen,l)
            #print("l:{}".format(l))

        return maxlen
                
                