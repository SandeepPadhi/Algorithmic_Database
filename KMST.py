class Graph:
    def __init__(self,Vertices):
        self.V=Vertices
        self.Graph=[]
    def addEdge(self,u,v,w):
        self.Graph.append([u,v,w])
    def findParent(self,Parent,x):
        if Parent[x]==x:
            return x
        Parent[x]=self.findParent(Parent,Parent[x])
        return Parent[x]
    def Union(self,Parent,Rank,x,y):
        xroot=self.findParent(Parent,x)
        yroot=self.findParent(Parent,y)
        if xroot==yroot:
            return
        if Rank[xroot]>Rank[yroot]:
            Parent[yroot]=xroot
        elif Rank[yroot]>Rank[xroot]:
            Parent[xroot]=yroot
        else:
            Parent[xroot]=yroot
            Rank[xroot]=Rank[xroot]+1
    def KruskalMST(self):
        Parent=[]
        Rank=[]
        for node in range(self.V):
            Parent.append(node)
            Rank.append(0)

        e=0
        GraphSorted=sorted(self.Graph,key=lambda item:item[2])
        lenGraph=len(GraphSorted)
        weight=0
        Result=[]
        for u,v,w in GraphSorted:
            x=self.findParent(Parent,u)
            y=self.findParent(Parent,v)
            if x==y:
                continue
            if x!=y:
                self.Union(Parent,Rank,u,v)
                Result.append([u,v])
                weight=weight+w
                e=e+1
            if e==(self.V-1):
                break
        return weight,Result

g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
  
weight,Result= g.KruskalMST() 
print("Weight of Minimum Spanning Tree:{}".format(weight))
for i in Result:
    print(i)
            
