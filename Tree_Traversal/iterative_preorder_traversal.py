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
root.left.right.right=Node(6.5)
root.right=Node(10)


def preorder(root):
    Stack=[]
    current=root
    while(True):
        if current is not None:
            print(current.val)
            Stack.append(current)
            current=current.left
        elif Stack:
            current=Stack.pop()
            current=current.right
        else:
            break
        
        
preorder(root)