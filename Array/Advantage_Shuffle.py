"""
Date:11/03/2021
870. Advantage Shuffle - Medium Shuffle

The following program is solved using sorting and deque
"""

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        B=[(b,i) for i,b in enumerate(B)]
        A.sort()
        A=deque(A)
        B.sort()
        Ans=[]
        i,j=0,0
        unexplored=[]
        while(len(A)):
            a=A.popleft()
            if a<=B[j][0]:
                unexplored.append(a)
            else:
                Ans.append((a,B[j][1]))
                j+=1
        while(j<len(B)):
            Ans.append((unexplored.pop(),B[j][1]))
            j+=1
        Ans.sort(key=lambda x:x[1])
        return [Ans[i][0] for i in range(len(Ans))]
            
        
        
      