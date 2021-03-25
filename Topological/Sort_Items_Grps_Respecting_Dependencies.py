"""
Date:23/03/2021
1203. Sort Items by Groups Respecting Dependencies - Leetcode Hard

The following problem is solved using Two layer Topological Sorting
We have created extra nodes and reconfigured groups and added extra directed edges to comvert our problems to 
Topological Sort problem
"""
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        lowest=n
        lookup={}
        #print("group before:{}".format(group))
        for i in range(len(group)):
            if group[i]!=-1:
                if group[i] in lookup:
                    group[i]=lookup[group[i]]
                else:
                    lookup[group[i]]=lowest
                    group[i]=lowest
                    lowest+=1
            
        for i in range(len(group)):
            if group[i]==-1:
                group[i]=lowest
                lowest+=1
        
        #print("group:{}".format(group))
        N=lowest
        #print("N:{}".format(N))
        Adj=[[] for _ in range(N)]
        Indegree=[0]*N

    
    
        for i in range(len(group)):
            Adj[group[i]].append(i)
            Indegree[i]+=1
        
        for i,items in enumerate(beforeItems):
            for item in items:
                if group[i]==group[item]:
                    Adj[item].append(i)
                    Indegree[i]+=1
                else:
                    Adj[item].append(i)
                    Indegree[i]+=1
                    Adj[item].append(group[i])
                    Indegree[group[i]]+=1
        #print("Indegree:{}".format(Indegree))
        #print("Adj:{}".format(Adj))
        
        Q=deque()
        for i in range(N):
            if Indegree[i]==0:
                Q.append(i)
        group_order=[]
        G={}
        while(len(Q)):
            u=Q.popleft()
            if u>=n:
                group_order.append(u)
                G[u]=[]
            else:
                G[group[u]].append(u)
        
            for v in Adj[u]:
                Indegree[v]-=1
                if Indegree[v]==0:
                    Q.append(v)
        for i in range(N):
            if Indegree[i]!=0:
                return []
        
        Ans=[]
        for u in group_order:
            Ans.extend(G[u])
        return Ans