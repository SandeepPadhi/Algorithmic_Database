
"""
Kahn's Topological Sort using Indegree
"""

from collections import deque
edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]
V=8
Adj=[[] for _ in range(V)]
Indegree=[0]*V
Result=[]
Queue=deque()
for u,v in edges:
    Adj[u].append(v)
    Indegree[v]+=1


for i in range(V):
    if Indegree[i]==0:
        Queue.append(i)



while(Queue):
    m=Queue.popleft() #Here,popleft and pop (i.e stack and queue both will work)
                      #Because,low element whose one of ancestor has indegree zero cannot be processed
                      #unless that ancestor with indegree zero is processed
                      #stack has behaviour of depth-first
                      #queue has behaviour like fire starting from circumference and moving towards the centre
    Result.append(m)
    for u in Adj[m]:
        Indegree[u]-=1
        if Indegree[u]==0:
            Queue.append(u)
            
print("Result:{}".format(Result))