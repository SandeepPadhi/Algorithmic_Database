"""
Date:21/02/2021

1766. Tree of Coprimes - Leetcode-Medium
Link:https://leetcode.com/problems/tree-of-coprimes/


The following problem is a Tree implementation.
It makes use of fact that max val of nums[i]<=50.
So,we can make use of that fact to store that latest nodes and their depth with nums[i] values at any time.


Path[i]=stores (node_no,depth) of latest node in the current path whose nodeval=i.
By,doing it have made it free of the order and depth of the current path,because at max their will be only 50 node_values in the current path.
"""
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        Adj=[[] for _ in range(len(nums))]
        for u,v in edges:
            Adj[u].append(v)
            Adj[v].append(u)
        Ans=[-1]*len(nums)
        path=[(-1,-1) for _ in range(51)]#(depth,val)
        def dfs(node,parent,depth):
            nonlocal Ans,path
            bestdepth=-1
            val=-1
            for i in range(1,len(path)):
                anc_no,anc_depth=path[i]
                if anc_no!=-1 and gcd(i,nums[node])==1 and anc_depth>bestdepth:#we try to find the closest node whose gcd is 1
                    bestdepth=anc_depth
                    val=anc_no
            prev=path[nums[node]]
            path[nums[node]]=(node,depth)
            Ans[node]=val
            for v in Adj[node]:
                if v!=parent:
                    dfs(v,node,depth+1)
            path[nums[node]]=prev#restore old val
                    
                  
            
        path[nums[0]]=(0,0)
        for v in Adj[0]:
            dfs(v,0,1)
        return Ans
        