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


def postorder(root):
    Stack=[]
    current=root
    Map={}
    while(True):
        if current is not None :
            Stack.append(current)
            Map[current]=1
            current=current.left
        elif Stack:
            current=Stack.pop()
            if Map[current]==1:
                Map[current]=2
                Stack.append(current)
                current=current.right
            else:
                print(current.val)
                Map[current]=3
                current=None
            
        else:
            break
        

postorder(root)