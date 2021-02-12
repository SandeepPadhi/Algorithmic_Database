#Edges=[(9,4),(4,2),(4,1),(2,8),(1,8),(9,7),(9,6),(6,5),(7,5),(5,3)]
Edges=[(1,2),(2,3),(3,1)]
V=0
for u,v in Edges:
    V=max(V,u,v)
Adj=[[] for _ in range(V+1)]
for u,v in Edges:
    Adj[u].append(v)
    Adj[v].append(u)

print("Adj:{}".format(Adj))
INF=1000
Disc=[INF]*(V+1)
Low=[INF]*(V+1)
Visited=[False]*(V+1)
Result=[]
Parent=[i for i in range(V+1)]
time=0
def AP(root):
    global time,Visited,Low,Result,parent,Disc
     
    Visited[root]=True
    Disc[root]=time
    Low[root]=time
    print("{} -> discovered at {}".format(root,Disc[root]))

    time+=1
    children=0
    print("Children of {} :{}".format(root,Adj[root]))
    for child in Adj[root]:
        if Visited[child]==False:
            Parent[child]=root
            children+=1
            AP(child)
            print("back to :{}".format(root))
            Low[root]=min(Low[root],Low[child])

            if Parent[root]==root and children>1:
                Result.append(root)
            if Parent[root]!=root and Low[child]>=Disc[root]:
                print("root:{},Disc:{}".format(root,Disc[root]))
                print("child:{},Low:{}".format(child,Low[child]))
                Result.append(root)
                
            
            
            
        elif Parent[root]!=child:
            Low[root]=min(Low[root],Disc[child])

    

for i in range(1,V+1):
    if Visited[i]==False:
        AP(i)

print("Articulation Points are {}".format(Result))
print("Parent:{}".format(Parent))
print("Disc:{}".format(Disc))
print("Low:{}".format(Low))

