edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]

V=8

Adj=[[] for _ in range(V)]
Discovered=[False]*V
result=[]
Indegree=[0]*V
for u,v in edges:
    Adj[u].append(v)
    Indegree[v]+=1
    
def findTopological(Indegree,Discovered,path,result):
    if len(path)==V:
        result.append(path)
        return
    
    for u in range(V):
        if Indegree[u]==0 and not Discovered[u]:
            for v in Adj[u]:
                Indegree[v]-=1
            Discovered[u]=True
            findTopological(Indegree,Discovered,path+[u],result)
            
            Discovered[u]=False
            #path.pop()
            for v in Adj[u]:
                Indegree[v]+=1
            Discovered[u]=False

findTopological(Indegree,Discovered,[],result)
print("Result are as follows of len:{}".format(len(result)))

for path in result:
    print("path:{}".format(path))
