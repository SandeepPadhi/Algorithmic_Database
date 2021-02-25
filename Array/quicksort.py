from itertools import permutations
A=[54, 546, 548, 60]
def partition(low,high):
    global A
    pivot=A[high]
    pindex=high
    for i in range(low,high+1):
        if i<pindex:
            if A[i]<=pivot:
                A[pindex],A[i]=A[i],A[pindex]
                pindex-=1
                
        else:
            break
    A[pindex],A[high]=A[high],A[pindex]
    print(pindex)
    return pindex
            
    

def quicksort(low,high):
    if low<high:
        p=partition(low,high)
        quicksort(low,p-1)
        quicksort(p+1,high)
quicksort(0,len(A)-1)
print(A)




"""
Quicksort 2:










# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
A=[54, 546, 548, 60,313,1,2,3,1,2,112]
def partition(low,high):
    global A
    #descending order
    pindex=high
    pivot=A[low]
    for i in range(high,low,-1):
        if A[i]<pivot:
            A[pindex],A[i]=A[i],A[pindex]
            pindex-=1
    A[pindex],A[low]=A[low],A[pindex]
    return pindex
        
def quicksort(low,high):
    if low<high:
        p=partition(low,high)
        quicksort(low,p-1)
        quicksort(p+1,high)
quicksort(0,len(A)-1)
print(A)






"""