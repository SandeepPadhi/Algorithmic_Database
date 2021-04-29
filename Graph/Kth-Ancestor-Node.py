"""
Date:267/04/2021
1483. Kth Ancestor of a Tree Node - Leetcode Hard

The following problem is solved using Binary Lifting technique or jump pointer technique
"""
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.log=ceil(log(n,2))
        self.log=20
        self.up=[[0]*(self.log+1) for _ in range(n)] #up[n][log]
        self.parent=parent
        print(parent)
        self.parent[0]=0
        self.depth=[0]*(n+1)
        
        
        V=[False]*(n+1)
        V[0]=True
        for node in range(n-1,-1,-1):
            if not V[node]:
                tempnode=node
                Stack=[]
                while(not V[tempnode]):
                    Stack.append(tempnode)
                    tempnode=parent[tempnode]
                while(Stack):
                    self.depth[Stack[-1]]=self.depth[tempnode]+1
                    tempnode=Stack.pop()
                    V[tempnode]=True
        
        #print(self.depth)
  
        for i in range(n):
            self.up[i][0]=parent[i]
            
        for j in range(1,self.log+1):
            for v in range(n):
                self.up[v][j]=self.up[self.up[v][j-1]][j-1]
        
            
    def getKthAncestor(self, node: int, k: int) -> int:
            if self.depth[node]<k:
                return -1
            #ans=-1
            for i in range(20):
                if k&(1<<i):
                    node=self.up[node][i]
                
            return node
        

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)