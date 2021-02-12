# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        Ans=None
        #-2 couldnt find anything from that root
        #return -1 or 1 if we find anything between p and q respectively
        #return zero if root
        #p=-1
        #q=1
        def find(root):
            nonlocal Ans
            if root==None:
                return -2
            if root.val==p.val:
                l=find(root.left)
                if l==1:
                    Ans=root
                    return 0
                
                r=find(root.right)
                if r==1:
                    Ans=root
                    return 0
                return -1

            if root.val==q.val:
                l=find(root.left)
                if l==-1:
                    Ans=root
                    return 0

                r=find(root.right)
                if r==-1:
                    Ans=root
                    return 0
                return 1
            
            l=find(root.left)
            if l==0:
                return 0
            r=find(root.right)
            if r==0:
                return 0
            if l==-r:
                Ans=root
                return 0
            if l==-1 or l==1:
                return  l
            if r==1 or r==-1:
                return r
            return -2
        return Ans

