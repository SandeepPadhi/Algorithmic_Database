"""
Date:19/03/2021
134. Gas Station - Leetcode Medium

The following problem is solved using Two Pointer Approach
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N=len(gas)
        start = 0
        end = 0
        Done=True
        G=0
        done=True
        while(start!=end or  done or G<0):
            done=False
            if G<0:
                if end<=start:
                    return -1
                start = end
                G=0
            G+=(gas[end]-cost[end])
            end = (end+1)%N
        return start
            
   
        
        """
        N=len(gas)
        for start in range(len(gas)):
            G = gas[start] - cost[start]
            j=(start + 1)%N
            if G<0:
                continue
            while(j!=start and G>0):
                G+=(gas[j]-cost[j])
                j=(j+1)%N
            if j==start and G>=0:
                return start
        return -1
        
        
        
        """