"""
Date:28/01/2021
The following program is used to find xor of range:[L,R]
It is implemented using Fenwick Tree
"""
Array = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5]
array=[]
print("Array initital:{}".format(array))
def build():
    global array
    array=[0]+Array
    for idx in range(1,len(array)):
        idx2=idx+(idx&-idx)
        if idx2<len(array):
            array[idx2]^=array[idx]
def prefix(idx):
    idx+=1
    result=0
    while(idx):
        result^=array[idx]
        idx-=(idx&-idx)
    return result

def update(idx,val):
    global array
    val=val^Array[idx]
    idx+=1
    #print("update index:{} with {}".format(idx,val))
    while(idx<len(array)):
        array[idx]^=val
        idx+=(idx&-idx)


def query(l,r):
    pr=prefix(r)
    pl=prefix(l-1)
    #print("pr:{} , pl:{}".format(pr,pl))
    return pr^pl
#
build()
print(query(0,2))
update(1,4)
print(query(1,1))
print(query(0,2))
