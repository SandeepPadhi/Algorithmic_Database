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
        if Rank[xroot]<Rank[yroot]:
            Parent[xroot]=yroot
        elif Rank[xroot]>Rank[yroot]:
            Parent[yroot]=xroot
        else:
            Parent[xroot]=yroot
            Rank[xroot]=Rank[xroot]=1

    def KruskalMST(self):
        Parent=[]
        Rank=[]
        #MakeSet
        for node in range(self.V):
            Parent.append(node)
            Rank.append(0)
        GraphSorted=sorted(self.Graph,key=lambda item:item[2])
        Result=[]
        Weight=0
        e=0
        Edgelen=len(GraphSorted)
        for u,v,w in GraphSorted:
            x=self.findParent(Parent,u)
            y=self.findParent(Parent,v)
            if x==y:
                continue

            if x!=y:
                self.Union(Parent,Rank,x,y)
                Result.append([u,v])
                Weight=Weight+w
                e=e+1
            if e==(self.V-1):
                return Result,Weight
        return Result,Weight
            
g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
  
Result,TreeWeight = g.KruskalMST()
print("Weigth of Minimum Spanning Tree:{}".format(TreeWeight))
for i in Result:
    print(i)


    
