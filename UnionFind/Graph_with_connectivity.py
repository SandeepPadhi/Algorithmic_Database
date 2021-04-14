"""
Date:14/04/2021
1627. Graph Connectivity With Threshold - Leetcode Hard

The following problem is solved using Union-Find Algorithm + Maths+logic
"""
class DSU:
    def __init__(self,n):
        self.parent=list(range(n+1))
        self.rank=[1]*(n+1)
    
    def find(self,x):
        if x!=self.parent[x]:
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
    

class Sieve:
    def __init__(self,n):
        self.sieve=[i for i in range(n+1)]
        self.n=n

        self.solve()
        
    def solve(self):
        for i in range(2,self.n+1):
            for j in range(i+i,self.n+1,i):
                self.sieve[j]=i
                
    

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        if threshold==0:
            return [True]*len(queries)
        
        start=threshold
        
        dsu=DSU(n)
        Done=[False]*(n+1)
        
        for i in range(start+1,n+1):
            if Done[i]:
                continue
                
            Done[i]=True
            for j in range(2*i,n+1,i):
                Done[j]=True
                #if gcd(i,j)>threshold:
                dsu.union(i,j)
        
        Result=[]
        for a,b in queries:
            if dsu.find(a)==dsu.find(b):
                Result.append(True)
            else:
                Result.append(False)
                
        return Result
            
        
        