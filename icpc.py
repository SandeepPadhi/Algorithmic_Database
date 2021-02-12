T=int(input())
import math
def bfs(node,result,Adj):
		visited=[0 for _ in range(0,N+1)]
		queue=[node]
		n1=node
		while(len(queue)):
			node=queue.pop(0)
			for i in adj[node]:
				if math.gcd(i,n1)==1:
					result[n1]=i
					return
				queue.append(i)
		
		
def check():
	N=int(input())
	S=[0]+list(map(int,input().split()))
	Adj=[[] for _ in range(1,N+1)]
	for _ in range(N):
		#We will be reversing the edges
		u,v = map(int,input().split())
		Adj[v].append(u)
	result=[-1 for _ in range(1,N+1)]
	for i in range(1,N+1):
		bfs(i,result,Adj)
		
	
	for i in range(1,N+1):
		print(result[i],end=" ")
		 


for _ in range(T):
	check()