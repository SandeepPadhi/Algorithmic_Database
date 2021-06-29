"""
Date:20/06/2021

The following program is to do inorder traversal using Morris traversal.
Time Complexity : O(N)
Space Complexity : O(1)
"""

class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

root=Node(9)
root.left=Node(7)
root.left.left=Node(6)
root.left.left.left=Node(5)
root.left.left.right=Node(6.5)
root.left.right=Node(8)
root.left.right.left=Node(7)
root.left.right.right=Node(8.5)
root.right=Node(10)

def findPredecessor(root):
    node=root.left
    while(node.right and node.right!=root):
        node=node.right
    return node

node=findPredecessor(root)
def Morris_Inorder_Traversal(root):
    curr=root
    while(curr):
        if curr.left==None:
            print(curr.val)
            curr=curr.right
        else:
            pred=findPredecessor(curr)
            if pred.right==None:
                pred.right=curr
                curr=curr.left
            else:
                pred.right=None
                print(curr.val)
                curr=curr.right

Morris_Inorder_Traversal(root)

            
        
        