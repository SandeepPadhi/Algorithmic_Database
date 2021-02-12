"""
Date:30/01/2021
The following program updates values over a range.
Record array is created to store query frequencies
We use segment Tree for solving
"""
n = 5
m = 5
arr = [0]*(n+1)
S=[0]*4*(n+1)
# Build query matrix 
query = [[],[1, 1, 2 ],[1, 1, 2 ],[ 1, 4, 5 ],[2, 1, 2 ],  
        [ 2, 1, 3 ],[ 2, 1, 3 ],[ 2, 3, 4]]

def update(node,start,end,left,right,val):
    global S
    print("start:{},end:{},left:{},right:{}".format(start,end,left,right))
    if end<left or start>right:
        return 0
    if left<=start and end<=right:
        S[node]+=(end-start+1)*val
        return (end-start+1)*val
    mid=(start+end)//2
    S1=update(2*node+1,start,mid,left,right,val)
    S2=update(2*node+2,mid+1,end,left,right,val)
    S[node]=S[node]+S1+S2
    return S[node]

def Query(node,start,end,l,r):
    if end<l or start>r:
        return 0
    if l<=start and end<=r:
        return S[node]
    mid=(start+end)//2
    S1=Query(2*node+1,start,mid,l,r)
    S2=Query(2*node+2,mid+1,end,l,r)
    return S1+S2

record={}

def updatequery(q):
    global record
    if len(q)==0:
        return
    if q[0]==1:
        if q not in record:
            record[q]=0
        record[q]+=1
        
    else:
        for i in range(q[1],q[2]+1):
            updatequery(tuple(query[i]))
    

for q in query:
    updatequery(tuple(q))
print("record:{}".format(record))
for q in record:
    update(0,0,len(arr)-1,q[1],q[2],record[q])
result=[]
for i in range(len(arr)):
    result.append(Query(0,0,len(arr)-1,i+1,i+1))
result.pop()

print(result)

        
        
        
    
