class Node:
    def __init__(self):
        self.children={}
        self.end=False

def insert(key,root):
    for k in key:
        if k not in root.children:
            root.children[k]=Node()
        root=root.children[k]
    root.end=True

def delete(key,root):
    for k in key:
        if k not in root.children:
            return False
        root=root.children[k]
    if root.end==True:
        root.end=False
    if len(root.children)==0:
        del root

def search(key,root):
    for k in key:
        if k not in root.children:
            return False
        root=root.children[k]
    return root!=None and root.end


keys = ["the","a","there","anaswe","any","by","their"] 
root=Node()
for key in keys:
    insert(key,root)

for key in keys:
    print("{} is {}".format(key,search(key,root)))

print("{} is {}".format("the",search("the",root)))

delete('any',root)
print("{} is {}".format("any",search("any",root)))

        









