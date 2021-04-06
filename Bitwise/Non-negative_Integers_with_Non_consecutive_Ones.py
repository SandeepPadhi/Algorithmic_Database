"""
Date:6/03/2021
600. Non-negative Integers without Consecutive Ones - Leetcode Hard

The following program is solved using recursion + bitwise + DP
"""
class Solution:
    def findIntegers(self, num: int) -> int:
         
        ln=0
        temp=num
        while(temp):
            ln+=1
            temp>>=1
        dp=[0]*(ln+1)
        dp[0]=1
        if ln>=1:
            dp[1]=2
        if ln>=2:
            dp[2]=3
        if ln>=3:
            dp[3]=5
        for i in range(4,ln+1):
            dp[i]=dp[i-1]+dp[i-2]
        temp=num
        start=ln-1
        Ans=0
        Ans+=dp[start]
        end=start-1
        while(end>=0 and not (temp&(1<<end)>0)):
            end-=1
        if end==-1:
            Ans+=1
        elif start-end==1:
            Ans+=dp[end]
        else:
            xor=0
            for i in range(end+1):
                xor+=(1<<i)
            val=num&xor
            Ans+=self.findIntegers(val)
            
        return Ans