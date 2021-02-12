
"""
Date:4/01/2021
The following program finds the length of Longest Common Sequence and prints it.


Note that in any subsequence problem Parent child relation is very important and 
perhaps the only way to find the subsequence as per the condition
"""
X = "AGGTAB"
Y = "GXTXAYB"
m=len(X)
n=len(Y)
LCS=[[0 for _ in range(n+1)] for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if X[i-1]==Y[j-1]:
            LCS[i][j]=1+LCS[i-1][j-1]
        else:
            LCS[i][j]=max(LCS[i][j-1],LCS[i-1][j])

lcs=LCS[-1][-1]
print("Len of lcs:{}".format(lcs))
R=[]
i=m
j=n
while(i>1 and j>0):
        if X[i-1]==Y[j-1]:
            R.append(X[i-1])
            i-=1
            j-=1
        else:
            if LCS[i][j-1]>LCS[i-1][j]:
                j-=1
            else:
                i-=1
R.reverse()
print("Longest common subsequence is {}".format("".join(R)))