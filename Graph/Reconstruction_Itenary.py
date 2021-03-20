"""
Date:20/03/2021
332. Reconstruct Itinerary - Leetcode Medium

The following problem is solved using Greedy + DFS + Sorting
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        T={}
        Lookup={}
        Ans=[]
        for u,v in tickets:
            if u not in Lookup:
                Lookup[u]=[]
            Lookup[u].append(v)
            s=u+v
            if s not in T:
                T[s]=0
            T[s]+=1
        
        for u in Lookup:
            Lookup[u].sort()
        Done=set()
        def find(path,V,u,count):
            nonlocal T
            
            if count==len(tickets):
                Ans.append(path)
                return True
            
            if u not in Lookup:
                return False
            
            for v in Lookup[u]:
                s=u+v
                if T[s]>0:
                    T[s]-=1
                    if find(path+[v],V,v,count+1):
                        return True
                    T[s]+=1
            return False
        find(['JFK'],set(),'JFK',0)
        Ans.sort()
        return Ans[0]
            
            
            