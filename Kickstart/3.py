T=int(input())

def find():
    import heapq
    
    R,C = map(int,input().split())
    grid=[]
    for _ in range(R):
        grid.append(list(map(int,input().split())))
    V=[[False for _ in range(C)] for _ in range(R)]
    
    heap=[]
    for i in range(R):
        for j in range(C):
            heapq.heappush(heap,(-grid[i][j],i,j))
    
    Ans=0
    while(len(heap)>0):
        #print("len of heap:{}".format(len(heap)))
        val,i,j =  heapq.heappop(heap)
        
        if V[i][j]==True:
            continue
        V[i][j]=True
        
        for di,dj in [(-1,0),(1,0),(0,1),(0,-1)]:
            ni,nj = i+di,j+dj
            if not(0<=ni<R) or not(0<=nj<C) or V[ni][nj]==True :
                continue
            
            h=grid[i][j]-grid[ni][nj]
            
            if h<2:
                continue
            
            Ans+=(h-1)
            grid[ni][nj]=grid[i][j]-1
            heapq.heappush(heap,(-grid[ni][nj],ni,nj))
    return Ans
            
            


for i in range(1,T+1):
    Ans = find()
    print("Case #{}: {}".format(i,Ans))