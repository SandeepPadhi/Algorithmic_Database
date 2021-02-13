"""
Date:12/02/2021
95. Unique Binary Search Trees II  -Leetcode - Medium

Following program is solved using Recursion.
"""
# Definition for a binary tree node.
class Treenode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Treenode]:
        
        def generateTree(N):
            R=[]
            if len(N)==0:
                return [None]
            for i in range(len(N)):
                left=generateTree(N[:i])
                right=generateTree(N[i+1:])
                for lroot in left:
                    for rroot in right:
                        root=Treenode(N[i])
                        root.left=lroot
                        root.right=rroot
                        R.append(root)
            return R

                    

                    
        
        N=[i for i in range(1,n+1)]
        Result=generateTree(N)
        return Result
        
        