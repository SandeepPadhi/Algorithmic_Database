"""
Date:19/05/2021
543. Diameter of Binary Tree - Leetcode Easy

The following problem is solved using recursion
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0,0
        
        def find(root):
            if root.left==None and root.right==None:
                return 0,0
            if root.left==None:
                lh,dl=find(root.right)
                return lh+1,max(lh+1,dl)
            if root.right==None:
                rh,dr=find(root.left)
                return rh+1,max(rh+1,dr)
            lh,dl=find(root.left)
            rh,dr=find(root.right)
            lh+=1
            rh+=1
            H=max(lh,rh)
            return H,max(dl,dr,lh+rh)
            
            
            
        h,d=find(root)
        return d