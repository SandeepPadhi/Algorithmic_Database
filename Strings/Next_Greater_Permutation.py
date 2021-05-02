A=[1,4,3,6,3,7,5,7,7,7,5,3,2,5,3,3]
At=A[::]#produces deep copy of the A
print(A)

"""
Note:Below functions take list as parameter which is manipulated.It does not return anything
"""

#Finds next greater permutation
def findNextGreater(A):
    ans=-1
    found=False
    for i in range(len(A)-2,-1,-1):
        if A[i]<A[i+1]:
            ans=i
            found=True
            break
    if not found:
        return
    else:
        #Here ,we find nextgreater element>A[i]
        i=ans
        j=i
        while(j<len(A)-1 and A[i]<A[j+1]):
            j+=1
        A[i],A[j]=A[j],A[i]
        A[i+1:]=A[i+1:][::-1]
        return
    
findNextGreater(A)
print("nextgreater:{}".format(A))

