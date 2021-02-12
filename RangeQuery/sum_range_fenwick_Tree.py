"""
Date:28/01/2021
The following program is for sum of range:[L,R]
It is implemented using Fenwick Tree
"""
Array = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5]
array=[]
def build():
    global array
    array=[0]+Array
    for idx in range(1,len(array)):
        idx2=idx+(idx&-idx)
        if idx2<len(array):
            array[idx2]+=array[idx]

def prefix(idx):
    idx+=1
    result=0
    while(idx):
        result+=array[idx]
        idx-=(idx&-idx)
    return result

def query(l,r):
    return prefix(r)-prefix(l-1)

def update(idx,val):
    val=val-Array[idx]
    idx+=1
    while(idx<len(array)):
        array[idx]+=val
        idx+=(idx&-idx)

build()
print(query(0,2))
update(1,3)
print(query(0,2))