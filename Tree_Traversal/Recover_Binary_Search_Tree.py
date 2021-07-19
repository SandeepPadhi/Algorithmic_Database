"""
Date:8/07/2021
99. Recover Binary Search Tree - Leetcode Medium

The following problem is solved using morris inorder traversal.
Time complexity:O(N)
Space complexity:O(1)


The idea is to keep track of predecessor.When we move right,we make cur node as predecessor.
Due to morris traversal,predecessor's right becomes node.So ,when we reach node again,is predecessor will be the predecessor(offcourse)
as we moved to the right of predecessor to reach the cur node.
"""



class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        """
            
        cur=root
        predecessor=None
        first=None
        second=None
        while(cur):
            if not cur.left:
                if predecessor and predecessor.val>cur.val:
                    if not first:
                        first=predecessor
                    second=cur
                
                predecessor=cur
                cur=cur.right
            else:
                prev=cur.left
                while(prev.right is not None and prev.right!=cur):
                    prev=prev.right
                if prev.right is None:
                    prev.right=cur
                    cur=cur.left
                else:
                    
                    if predecessor.val>cur.val:
                        if not first:
                            first=predecessor
                        second=cur
                    
                    prev.right=None
                    predecessor=cur
                    cur=cur.right
        first.val,second.val=second.val,first.val



        """
        SOLUTION USING STACK


        Stack=[]
        def dfs(root,Stack):
            if not root:
                return
            dfs(root.left,Stack)
            Stack.append(root)
            print(root.val)
            dfs(root.right,Stack)
        
        dfs(root,Stack)
        first=None
        second=None
        for i in range(1,len(Stack)):
            if Stack[i-1].val>Stack[i].val:
                if not first:
                    first=Stack[i-1]
                    second=Stack[i]
                else:
                    second=Stack[i]
                    break
        
        first.val,second.val=second.val,first.val
            
        
        """
                
                        
