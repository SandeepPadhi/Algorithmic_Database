
"""
Date:9/03/2021
Add One Row to Tree - Leetcode Medium
The following program is solved using recursion
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        if d==1:
            node=TreeNode(v)
            node.left=root
            return node
        
        def find(root,d):
            if d==2:
                nodeleft,noderight=TreeNode(v),TreeNode(v)

                if root.left:
                    root.left,nodeleft.left=nodeleft,root.left
                else:
                    root.left=nodeleft
                    
                if root.right:
                    root.right,noderight.right=noderight,root.right
                else:
                    root.right=noderight
                return

                
                
            if root.left:
                find(root.left,d-1)
            if root.right:
                find(root.right,d-1)
        find(root,d)
            
        return root