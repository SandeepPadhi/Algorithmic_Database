"""
Date:28/04/2021
1123. Lowest Common Ancestor of Deepest Leaves - Leetcode Medium

The following program is solved using DFS and by making Parent Array
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        Depth={}
        maxdepth=-1
        Parent={root:root}
        
        def dfs(root,depth):
            nonlocal maxdepth,Depth,Parent
            if not root:
                return
            
            if root.left==None and root.right==None:
                if depth not in Depth:
                    Depth[depth]=set()
                Depth[depth].add(root)
                maxdepth=max(maxdepth,depth)
                return
            
            dfs(root.left,depth+1)
            if root.left:
                Parent[root.left]=root
            dfs(root.right,depth+1)
            if root.right:
                Parent[root.right]=root
            
        dfs(root,0)
        
        def lca(root,p,q):
            if p==q:
                return p
            while(p!=q):
                p=Parent[p]
                q=Parent[q]
            return p
            
        def check(Node):
            for i in range(1,len(Node)):
                if Node[i-1]!=Node[i]:
                    return False
            return True
        
        Node=list(Depth[maxdepth])
        if len(Node)==1:
            return Node[0]
        #print("len of Node:{}".format(len(Node)))
        
        while(not check(Node)):
            for i in range(len(Node)):
                Node[i]=Parent[Node[i]]
        return Node[0]
        
        
#[1,2,3,null,4,6,null,15,5,10,null,null,null,null,7,11,null,8,12,null,null,null,9,13,14]        