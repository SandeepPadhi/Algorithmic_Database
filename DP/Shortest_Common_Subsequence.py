"""
Date:25/03/2021
1092. Shortest Common Supersequence - Leetcode Hard

The following problem is solved using DP+Three Pointer Technique

Concepts used there are:
1.)find LCS (not just lcs_len but also actual LCS)
2).Three Pointer
"""

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1=len(str1)
        n2=len(str2)
        dp=[[0 for _ in range(n2+1)] for _ in range(n1+1)]
        for i in range(n1):
            for j in range(n2):
                if str1[i]==str2[j]:
                    dp[i+1][j+1]=1+dp[i][j]
                else:
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
        lcs_len=dp[-1][-1]
        LCS=[]
        i=n1
        j=n2
        while(i>0 and j>0):
            if str1[i-1]==str2[j-1]:
                LCS.append(str1[i-1])
                i-=1
                j-=1
            else:
                if dp[i][j-1]>dp[i-1][j]:
                    j-=1
                else:
                    i-=1
        LCS.reverse()
        #print("LCS:{}".format(LCS))
        #print("lcs_len:{}".format(lcs_len))
        Ans=""
        i=0
        j=0
        k=0
        while(i<n1 and j<n2 and k<lcs_len):
            while(i<n1 and str1[i]!=LCS[k]):
                Ans+=str1[i]
                i+=1
            while(j<n2 and str2[j]!=LCS[k]):
                Ans+=str2[j]
                j+=1
            Ans+=LCS[k]
            k+=1
            i+=1
            j+=1
        Ans="".join(Ans)
        if i<n1:
            Ans+=str1[i:]
        if j<n2:
            Ans+=str2[j:]
        
        
        return Ans