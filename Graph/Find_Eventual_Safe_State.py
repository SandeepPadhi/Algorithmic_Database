"""
Date:3/03/2021
802. Find Eventual Safe States - Leetcode Medium

The following problem is solved using DFS for directed Edges
"""
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V=[0]*len(graph)
        Ans=[True]*len(graph)
        
        def update(path,Ans):
            for p in path:
                Ans[p]=False
        def find(n,V,Ans,path):
            V[n]=1
            for p in graph[n]:
                if V[p]==1 or not Ans[p]:
                    update(path,Ans)
                    return
                elif V[p]==2:
                    pass
                else:
                    find(p,V,Ans,path+[p])
            V[n]=2
            return
                    
        for i in range(len(graph)):
            if V[i]==0:
                find(i,V,Ans,[i])
        return [i for i in range(len(graph)) if Ans[i]==True]
            
        
        
        