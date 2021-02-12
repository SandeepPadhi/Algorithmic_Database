t=int(input())

def find():
    n=int(input())
    A=[int(i) for i in input().split()]
    i=0
    done=0
    while(i+1<n):
        minval=min(A[i],A[i+1])
        A[i],A[i+1]=A[i]-minval,A[i+1]-minval
        if A[i]!=0:
            if done==0:
                done=1
                A[i],A[i+1]=A[i+1],A[i]
            else:
                print("NO")
        i+=1
    
    j=0
    check=0
    while(j<n):
        if A[j]!=0:
            if A[j]-j>0:
                check=1
            break
        j+=1
    
    #print("A:{}".format(A))
    if check==0:
        print("YES")
    elif len(A)==2:
        print("NO")
    
    else:
        print("NO")

for _ in range(t):
    find()