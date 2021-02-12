

#Complete this function
def trappingWater(arr,n):
    #Your code here
    ''
    i=0
    j=1
    hmax=max(arr)
    equal=0
    Area=0
    while(i<n):
        s=0
        while(j<n and arr[i]>arr[j]):
            s+=arr[j]
            j+=1
        if j==n:
            break
        d=j-i-1
        Area+=(d*arr[i]-s)
        if arr[j]==arr[i] and arr[j]==hmax:
            equal+=(d*arr[i]-s)
        i=j
        j+=1
    
    i=n-1
    j=i-1
    while(i>=0):
        s=0
        while(j>=0 and arr[j]<arr[i]):
            s+=arr[j]
            j-=1
        if j<0:
            break
        d=i-j-1
        Area+=(d*arr[i]-s)

        i=j
        j=i-1
    
    
    return Area-equal
    
    
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            print(trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends