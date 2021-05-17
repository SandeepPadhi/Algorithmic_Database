A=[[2,3,3],[3,3,1],[6,3,6]]

def Minor(A,ii,jj,n):
    #print("Minor:ii:{} , jj:{}".format(ii,jj))
    #print("A:{}".format(A))
    M=[[0]*n for _ in range(n)]
    i=j=0
    for r in range(n):
        for c in range(n):
            if r!=ii and c!=jj:
                M[i][j]=A[r][c]
                j+=1
                if j==n-1:
                    j=0
                    i+=1
    #print("M:{}".format(M))
    return deter(M,n-1)
    

def deter(A,n):
    #print("deter")
    if n==1:
        return A[0][0]
    #print(A)

    ans=0
    for i in range(n):
        m=Minor(A,0,i,n)
        a=A[0][i]
        #print("m:{} , a:{}".format(m,a))
        ans+=(((-1)**i)*m*a)
    return ans


ans=deter(A,3)
print("ans:{}".format(ans))