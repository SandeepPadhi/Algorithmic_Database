"""
Date:22/03/2021
854. K-Similar Strings

The following problem is solved using BFS
"""

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        
        def neighbors(s1,s2,Q,Done):
            s1=[s for s in s1]
            i=0
            while(s1[i]==s2[i]):
                i+=1
            for j in range(i+1,len(s1)):
                if s1[j]==s2[i]:
                    s1[i],s1[j]=s1[j],s1[i]
                    s="".join(s1)
                    if s not in Done:
                        Q.append(s)
                        Done.add(s)
                    s1[i],s1[j]=s1[j],s1[i]

                    
                    
        Q=deque()
        Q.append(s1)
        K=0
        Done={s1}
        while(len(Q)):
            N=len(Q)
            while(N>0):
                s1=Q.popleft()
                if s1==s2:
                    return K
                neighbors(s1,s2,Q,Done)
                N-=1 
            K+=1
        
        
        return K