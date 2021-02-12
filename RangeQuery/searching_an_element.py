"""
Date:30/01/2021
The following program is solved by storing the first index of element in case of consecutive
occurence of elements in an array
"""

Arr=[0,1,1,1,9,4,6,6,8,2,3,0]
Result=[i for i in range(len(Arr))]
for i in range(1,len(Arr)):
    if Arr[i]==Arr[i-1]:
        Result[i]=Result[i-1]
print(Result)

def query(l,r,x):
    p=r
    while(p>=l):
        if Arr[p]!=x:
            p=Result[p]-1
        else:
            return "Found at {}".format(p)
    return "Not found"
print(query(0,11,2))
