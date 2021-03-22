def find():
    R,C = map(int,input().split())
    grid=[]
    Ans=0
    for _ in range(R):
        g=list(map(int,input().split()))
        grid.append(g)

    Up=[[0 for _ in range(C)] for _ in range(R)]
    Down=[[0 for _ in range(C)] for _ in range(R)]
    Left=[[0 for _ in range(C)] for _ in range(R)]
    Right=[[0 for _ in range(C)] for _ in range(R)]
    
    for i in range(1,R):
      for j in range(C):
        Up[i][j]+=Up[i-1][j]
    
    for i in range(R-2,-1,-1):
      for j in range(C):
        Down[i][j]+=Down[i+1][j]
      
    for i in range(R):
      for j in range(1,C):
        Left[i][j]+=Left[i][j-1]
    
    for i in range(R):
      for j in range(C-2,-1,-1):
        Right[i][j]+=Right[i][j-1]
    
    Ans=0
    for i in range(R):
      for j in range(C):
        if grid[i][j]==0:
          continue
        l,r,u,d = Left[i][j],Right[i][j],Up[i][j],Down[i][j]
        
        if (l==1 and r==1) or (u==1 and d==1):
          continue

        V=[]
        if l>1:
          V.append(l)
        if r>1:
          V.append(r)
        if u>1:
          V.append(u)
        if d>1:
          V.append(d)
        V.sort()
        n1,n2=V[0],V[1]
        Ans=0
        for i in range(1,n1+1):
          if 2*i<=n2:
            Ans+=1
        
        for i in range(2,n2+1):
          if 2*i<=n1:
            Ans+=1
    return Ans
          
"""
2
4 3
1 0 0
1 0 1
1 0 0
1 1 0
6 4
1 0 0 0
1 0 0 1
1 1 1 1
1 0 1 0
1 0 1 0
1 1 1 0

"""

        





T=int(input())
for i in range(1,T+1):
    Ans=find()
    print("Case #{}: {}".format(i,Ans))