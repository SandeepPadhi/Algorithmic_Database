"""
Date:14/04/2021
1697. Checking Existence of Edge Length Limited Paths - Leetcode Hard

VERY IMPORTANT....CONNECTIVITY PROBLEMS ARE OFTEN SOLVED USING UNION-FIND

The following program is solved using Union Find + Sorting

The Idea here is to iteratively build connectivity Tree using union find by only considering edges within limits.


One more important idea that we got from here is that we dont have to always process the queries in order they appear
"""

class DSU:
    def __init__(self,n):
        self.parent=list(range(n+1))
        self.rank=[0]*(n+1)
        self.n=n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        p1=self.find(x)
        p2=self.find(y)
        if p1!=p2:
            if self.rank[p1]>self.rank[p2]:
                self.parent[p2]=p1
            elif self.rank[p2]>self.rank[p1]:
                self.parent[p1]=p2
            else:
                self.parent[p1]=p2
                self.rank[p2]+=1
        
    

class Solution:
    
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x:x[2])
        
        done=set()
        Edge=collections.deque()
        for u,v,dis in edgeList:
            if (u,v) in done:
                continue
            done.add((u,v))
            Edge.append((u,v,dis))
        #print("Edge:{}".format(Edge))
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key=lambda x:x[2])
        
        dsu=DSU(n)
        
        Ans=[False]*len(queries)
        for p,q,t,i in queries:
            while(len(Edge)):
                u,v,w=Edge.popleft()
                if w>=t:
                    Edge.appendleft((u,v,w))
                    break
                dsu.union(u,v)
            if dsu.find(p)==dsu.find(q):
                Ans[i]=True
            else:
                Ans[i]=False
                
        return Ans
        
        