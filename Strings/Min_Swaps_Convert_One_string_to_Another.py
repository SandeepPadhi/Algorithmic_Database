A=[3,1,2]
B=[1,2,3]
print(A)

def findMinSwaps(A,B):
    result=0
    for i in range(len(A)):
        if A[i]==B[i]:
            continue
        j=i
        while(j<len(B) and A[i]!=B[j]):
            j+=1
        while(j!=i):
            B[j],B[j-1]=B[j-1],B[j-1]
            result+=1
            j-=1
    return result
        
        
ans=findMinSwaps(A[::],B[::])
print("min swaps to convert A to At:{}".format(ans))

