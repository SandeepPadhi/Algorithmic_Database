"""
Date:12/02/2021
84. Largest Rectangle in Histogram-Hard

The following program is solved using stack.
Time complexity:O(N)

"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea=0
        stack=[]
        for i,h in enumerate(heights):
            start=i
            while(stack and stack[-1][1]>=h):
                index,height=stack.pop()
                maxarea=max(maxarea,height*(i-index))
                start=index
            stack.append((start,h))
        while(stack):
            i,h=stack.pop()
            maxarea=max(maxarea,h*(len(heights)-i))
        return maxarea
        
