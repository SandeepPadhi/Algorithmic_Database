"""
Date:17/05/2021
987. Vertical Order Traversal of a Binary Tree - Leetcode Hard

The following problem is solved using Map + sort
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        lookup={}
        
        def dfs(root,row,col):
            nonlocal lookup
            
            if col not in lookup:
                lookup[col]={}
            if row not in lookup[col]:
                lookup[col][row]=[]
            lookup[col][row].append(root.val)
            
            if root.left:
                dfs(root.left,row+1,col-1)
            if root.right:
                dfs(root.right,row+1,col+1)
        
        #print(lookup)
        dfs(root,0,0)
        
        Ans=[]
        for col in lookup:
            R=[]
            for row in lookup[col]:
                lookup[col][row].sort()
                R.append((row,lookup[col][row]))
            R.sort()
            C=[]
            for _ , r in R:
                C.extend(r)
            Ans.append((col,C))
        Ans.sort()
        
        
        Vorder=[]
        for _,a in Ans:
            Vorder.append(a)
        
        return Vorder
                
            