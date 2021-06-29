"""
Date:19/05/2021
Problem name : Delete a node from BST.

Link:https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/

The following problem is to insert and delete a node from BST.
Here,the concept of inorder successor is used.
"""


class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.key)
    inorder(node.right)
    
def findInorderSuccessor(node):
    Ans=node
    while(node):
        Ans=node
        node=node.left
    return Ans


def insert(node,key):
    if node is None:
        return Node(key)
    
    if key<=node.key:
        node.left=insert(node.left,key)
    elif key>node.key:
        node.right=insert(node.right,key)
    return node

def deleteNode(node,key):
    #print("yes")
    if node is None:
        return node 
    print("node.key:{} ,key:{}".format(node.key,key))

    #print("yes1")
    if key<node.key:
        print("moving left")
        node.left=deleteNode(node.left,key)
    elif key>node.key:
        print("moving right")
        node.right=deleteNode(node.right,key)
    else:
        print("found")
        if node.left is None:
            temp=node.right
            node=None
            return temp
        elif node.right is None:
            temp=node.left
            node=None
            return temp
        else:
            #find inordersuccessor
            inordersuccessor=findInorderSuccessor(node.right)
            node.key=inordersuccessor.key
            node.right=deleteNode(node.right,inordersuccessor.key)
            return node
    
    return node

root = None
root = insert(root, 50)
root = insert(root, 30)

root = insert(root, 20)

root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree")
inorder(root)


print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
root = deleteNode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 50")
root = deleteNode(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)




