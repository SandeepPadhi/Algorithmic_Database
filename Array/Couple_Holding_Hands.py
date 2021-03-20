"""
Date:20/03/2021
765. Couples Holding Hands

The following problem is solved using simple mapping
"""
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        count=0
        N=len(row)
        L=[0]*N
        
        for i in range(N):
            L[row[i]]=i
        
        for i in range(N//2):
            x,y=2*i,2*i+1
            first=row[x]
            second = first^1
            if second!=row[y]:
                count+=1
                ind1,ind2=y,L[second]
                row[ind1],row[ind2]=row[ind2],row[ind1]
                L[row[ind1]]=ind1
                L[row[ind2]]=ind2
        
        return count
                
        
        