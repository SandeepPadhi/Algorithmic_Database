"""
You should not use high as pivot,because if num[high] is the greatest element in the array ,
than it will get into infinite recursion.

while using randomized algorithm make sure you choose pivot from low-high-1

Link:
https://www.geeksforgeeks.org/hoares-vs-lomuto-partition-scheme-quicksort/
"""


arr = [1, 7, 8, 9, 1, 10]

def partition(arr,low,high):
    pivot=arr[low]
    #print("pivot:{}".format(pivot))
    i=low-1
    j=high+1
    while(True):
        
        j-=1
        while(pivot<arr[j]):
            j-=1
        
        i+=1
        while(arr[i]<pivot):
            i+=1
        
        if i>=j:
            return j
        
        arr[i],arr[j]=arr[j],arr[i]

def quicksort(arr,low,high):
    
    if low>=high:
        return
    pi=partition(arr,low,high)
    quicksort(arr,low,pi)
    quicksort(arr,pi+1,high)

quicksort(arr,0,len(arr)-1)
print(arr)