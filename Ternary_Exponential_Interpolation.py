#Generally Binary Search is faster than Ternay Search.
#Ternay search can also be used for parabolic datai.e unimodal data

arr = [1, 2, 3, 4, 6, 7, 8, 9, 10,12,13,14,15,16,17]
key=3

#Ternary Search
def Ternary(arr,key):
    l=0
    h=len(arr)-1
    ans=-1
    while(l<=h):
        m1=l+(h-l)//3
        m2=m1+(h-l)//3
        if arr[m1]==key:
            ans=m1
            break
        elif arr[m2]==key:
            ans=m2
            break
        elif key<arr[m1]:
            h=m2-1
        elif key<arr[m2]:
            l=m1+1
            h=m2-1
        else:
            l=m2+1
    print("Ternary Search:")
    if ans==-1:
        return "Not found"
    return "Found at index:{}".format(ans)
    
print(Ternary(arr,10))
print()

def Exponential(arr,key):
    l=0
    n=len(arr)-1
    if arr[l]==key:
        return "Found at index:{}".format(l)
    l=1
    while(l<=n and arr[l]<key):
        l*=2
    low=l//2
    high=min(l,n)
    
    #Binary Search:
    ans=-1
    while(low<=high):
        mid=low+(high-low)//2
        if arr[mid]==key:
            ans=mid
            break
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    print("Exponential Search:")
    if ans==-1:
        return "Not found"
    return "Found at index:{}".format(ans)
 
print(Exponential(arr,15))
print()
    
def Interpolation(arr,key):#0(log(logn))-Time Complexity
    print("Interpolation Search")

    if key>arr[-1]:
        return "Not found"
    low=0
    high=len(arr)-1
    ans=-1
    while(low<=high):
        mid=low+((key-arr[low])//(arr[high]-arr[low]) )*(high-low)
        if arr[mid]==key:
            ans=mid
            break
        elif arr[mid]<key:
            high=mid-1
        else:
            low=mid+1
    if ans==-1:
        return "Not Found"
    return "Found at Index:{}".format(ans)
print(Interpolation(arr,17))
