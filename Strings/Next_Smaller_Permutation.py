A=[1,4,3,6,3,7,5,7,7,7,5,3,2,5,3,3]
At=A[::]#produces deep copy of the A
#print(A)

"""
Note:Below functions take list as parameter which is manipulated.It does not return anything
"""

    
#produces next smaller permutation
def findNextSmaller(A):
    
    for i in range(len(A)-2,-1,-1):
        if A[i]>A[i+1]:
            found=True
            ans=i
            break
    if not found:
        A.sort(reverse=True)
        return
    else:
        i=ans
        j=i
        while(j<len(A)-1 and A[i]>A[j+1]):
            j+=1
        A[i],A[j]=A[j],A[i]
        A[i+1:]=A[i+1:][::-1]
        return 

findNextSmaller(A)
print("nextSmaller:{}".format(A))