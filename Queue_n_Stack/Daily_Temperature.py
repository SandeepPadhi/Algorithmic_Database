"""
Date:25/02/2021
739. Daily Temperatures - Leetcode Medium

The following program is solved using monotonic stack.
Whenever, the problem has a flow from left to right or right to left and is increasing or decreasing in nature.
And,we are somehow dealing with indices i.e distances/positions of list elements...
then that is the indication to use Monotonic Stack
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        nextgreater=[0]*len(T)
        stack=[]
        for i in range(len(T)):
            while(len(stack) and T[stack[-1]]<T[i]):
                t=stack.pop()
                nextgreater[t]=i-t
            stack.append(i)
        return nextgreater
        