"""
Date:13/02/2021
133. Clone Graph - Leetcode-Medium
IMPORTANT

In the following program ,we first created an Adjacency List,then created 
Linked Link out of that Adjacency List.We then return the root pointer.

"""


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None:
            return None
        N=0
        visited=[False]*101
        def dfs(node):
            nonlocal N
            if visited[node.val]:
                return
            visited[node.val]=True
            if node==None:
                return
            N=max(N,node.val)
            for n in node.neighbors:
                dfs(n)
        dfs(node)
        Adj=[[] for _ in range(N+1)]
        
        #Here ,we create the Adjacency List
        visited=[False]*(N+1)
        def find(node):
            nonlocal Adj
            if node==None:
                return
            if visited[node.val]:
                return
            visited[node.val]=True
            for n in node.neighbors:
                Adj[node.val].append(n.val)
                find(n)
        find(node)
        
        #Here,we clone the graph using the Adjacency List
        Nodearray=[None]*(N+1)
        for i in range(1,N+1):
            Nodearray[i]=Node(i)
        
        for i in range(1,N+1):
            root=Nodearray[i]
            for n in Adj[i]:
                root.neighbors.append(Nodearray[n])
            
            
        
        
        
        return Nodearray[node.val]
        