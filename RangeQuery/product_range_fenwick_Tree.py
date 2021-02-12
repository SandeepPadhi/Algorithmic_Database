"""
Date:28/01/2021
The following is program to find product of range:[L,R]
It is implemented using fenwick Tree
"""

Array = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5]
array=[]
def build():
    global array
    array=[1]+Array
    for idx in range(1,len(array)):
        idx2=idx+(idx&-idx)
        if idx2<len(array):
            array[idx2]*=array[idx]
def prefix(idx):
    result=1
    idx+=1
    while(idx):
        result*=array[idx]
        idx-=(idx&-idx)
    return result

def update(idx,val):#here,val is the value to be replaced at index idx
    val=val/Array[idx]#This is value to update...for addition,val is the new value to ne update..for mul..val to be propogated
    #Basically,val is the value to be propogated across the tree which is its updation
    idx+=1
    while(idx<len(array)):
        array[idx]*=val
        idx+=(idx&-idx)
        
def query(l,r):
    return prefix(r)/prefix(l-1)
    
build()
print(query(0,2))
update(2,4)
print(query(0,2))