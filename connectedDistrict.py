T=int(input())

def PrintConnection(NumParent):
    for i in range(len(NumParent)):
        if NumParent[i]!=-1:
            print("{} {}".format(i,NumParent[i]))


def BuildGraph(District,n):
    Graph=[[-1 for _ in range(n)] for _ in  range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j and District[i]!=District[j]:
                Graph[i][j]=1
    return Graph

def DFS(NumParent,Graph,District,Root,Visited):
    Visited[Root]=True
    for i in range(len(District)):
        if Visited[i]==False and i!=Root and Graph[Root][i]==1:
            NumParent[i]=Root
            dfs(NumParent,Graph,District,i,Visited)

def dfs(NumParent,Graph,District,Root,Visited):
    count=0
    for i in range(len(District)):
        if Visited[i]==False:
            DFS(NumParent,Graph,District,i,Visited)
            count=count+1
    if count==1:
        return True
    return False


def Compute():
    N=int(input())
    District=[int(i) for i in input().split(" ")]
    Graph=BuildGraph(District,N)
    NumParent=[-1 for _ in range(N)]
    Visited=[False for _ in range(N)]
    Root=0
    if dfs(NumParent,Graph,District,Root,Visited):
        PrintConnection(NumParent)
    else:
        print("NO")

for t in range(T):
    Compute()

"""
Input
Copy

4
5
1 2 2 1 3
3
1 1 1
4
1 1000 101 1000
4
1 2 3 4

Output
Copy

YES
1 3
3 5
5 4
1 2
NO
YES
1 2
2 3
3 4
YES
1 2
1 3
1 4

"""    