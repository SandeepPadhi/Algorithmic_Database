"""
Date:2/01/2021
The following,program is used find maximum subarray xor using Trie data structure.
Time Complexity:O(N)
"""

arr = [8, 1, 2, 12, 7, 6]

class Node:
    def __init__(self):
        self.left=None#0,left
        self.right=None#1,right
        self.data=None
        self.level=0
        
def insert(prexor,root):
    temp=root
    for i in range(31,-1,-1):
        val=prexor&(1<<i)
        if val:
            if not temp.right:
                temp.right=Node()
            temp=temp.right
        else:
            if not temp.left:
                temp.left=Node()
            temp=temp.left
        temp.level=i+1

    temp.data=prexor

def query(prexor,root):
    temp=root
    for i in range(31,-1,-1):
        val=prexor&(1<<i)
        if val:
            if temp.left:
                temp=temp.left
            else:
                temp=temp.right
        else:
            if temp.right:
                temp=temp.right
            else:
                temp=temp.left
    return temp.data
            

root=Node()

prexor=0
ans=0
i=0
for a in arr:
    prexor^=a
    insert(prexor,root)
    res=query(prexor,root)
    ans=max(ans,prexor^res)
print("Max subarray xor:{}".format(ans))
    