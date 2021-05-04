def merge(arr, aux, lo, mid, hi):
    for i in range(lo, hi + 1):
        aux[i] = arr[i]

    i, j = lo, mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > hi:
            arr[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            arr[k] = aux[j]
            j += 1
        else:
            arr[k] = aux[i]
            i += 1

def sort(arr, aux, lo, hi):
    if lo >= hi:
        return
    mid = lo + (hi - lo) // 2
    sort(arr, aux, lo, mid)
    sort(arr, aux, mid + 1, hi)
    merge(arr, aux, lo, mid, hi)

"""

Arr=[3,6,4,8,9,1]
Aux=[0]*len(Arr)
low=0
high=len(Arr)-1
def merge(Arr,Aux,low,mid,high):
    for i in range(low,high+1):
        Aux[i]=Arr[i]
    i=low
    j=mid+1
    for k in range(low,high+1):
        if i>mid:
            Arr[k]=Aux[j]
            j+=1
        elif j>high:
            Arr[k]=Aux[i]
            i+=1
        elif Arr[i]<Arr[j]:
            Arr[k]=Aux[i]
            i+=1
        else:
            Arr[k]=Aux[j]
            j+=1

def sort(Arr,Aux,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    sort(Arr,Aux,low,mid)
    sort(Arr,Aux,mid+1,high)
    merge(Arr,Aux,low,mid,high)
sort(Arr,Aux,low,high)
print(Arr)



"""