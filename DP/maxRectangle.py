"""
Date:11/02/2021
The following program is solved using dp and around the center technique
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row=len(matrix)
        if row==0:
            return 0
        col=len(matrix[0])
        ans=0
        
        for i in range(col):
            matrix[0][i]=int(matrix[0][i])
            ans=max(ans,matrix[0][i])
        #print("matrix:{}".format(matrix))
        #print(ans)
        for i in range(1,row):
            for j in range(col):
                matrix[i][j]=int(matrix[i][j])
                if matrix[i][j]==1:
                    matrix[i][j]+=matrix[i-1][j]
        #print("matrix:{}".format(matrix))
        
        for mat in matrix:
            i=0
            while(i<col):
                h=mat[i]
                if h==0:
                    i+=1
                    continue
                j=i
                l,r=0,0
                while(j>=0 and mat[j]>=h):
                    l+=1
                    j-=1
                j=i
                while(j<col and mat[j]>=h):
                    r+=1
                    j+=1
                    
                w=l+r-1
                ans=max(ans,h*w)
                i+=1
        return ans

                
        