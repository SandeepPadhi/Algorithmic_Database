"""
Date:24/04/2021
1591. Strange Printer II - Leetcode Hard

VERY IMPORTANT

The following problem is solved using DFS
"""
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        
        def dfs(c):
            nonlocal printing,printable
            
            if c in printable:
                return True
            if c in printing:
                #print("yes")
                return False
            
            printing.add(c)
            for i in range(border[c][0],border[c][1]+1):
                for j in range(border[c][2],border[c][3]+1):
                    if targetGrid[i][j]!=c:
                        if not dfs(targetGrid[i][j]):
                            return False
            printable.add(c)
            return True
        
        border={}
        m=len(targetGrid)
        n=len(targetGrid[0])
        for i in range(m):
            for j in range(n):
                c=targetGrid[i][j]
                if c not in border:
                    border[c]=(i,i,j,j)
                else:
                    border[c]=(min(border[c][0],i),max(border[c][1],i),min(border[c][2],j),max(border[c][3],j))
        
        color=set(border.keys())
        
        printing=set()
        printable=set()
    
        for c in color:
            if not dfs(c):
                return False
        return True
        
        
        
        """
        m=len(targetGrid)
        n=len(targetGrid[0])
        mat=[[0]*n for _ in range(m)]
        color=set()
        for i in range(m):
            for j in range(n):
                color.add(targetGrid[i][j])
        #lookup={color:{tl: , tr: , bl: ,br: }}
        lookup={}
        for i in range(m):
            for j in range(n):
                c=targetGrid[i][j]
                if c not in lookup:
                    lookup[c]={'j1':j,'j2':j,'i1':i,'i2':i ,'A':1}
                else:
                    j1=lookup[c]['j1']
                    j2=lookup[c]['j2']
                    i1=lookup[c]['i1']
                    i2=lookup[c]['i2']
                    if i<i1:
                        i1=i
                    if i>i2:
                        i2=i
                    if j<j1:
                        j1=j
                    if j>j2:
                        j2=j
                    lookup[c]['j1']=j1
                    lookup[c]['j2']=j2
                    lookup[c]['i1']=i1
                    lookup[c]['i2']=i2
                    A=(j2-j1+1)*(i2-i1+1)
                    lookup[c]['A']=max(lookup[c]['A'],A)
        #print("lookup:{}".format(lookup))
        for c in lookup:
            j1=lookup[c]['j1']
            j2=lookup[c]['j2']
            i1=lookup[c]['i1']
            i2=lookup[c]['i2']
            
            if targetGrid[i1][j1]==c and targetGrid[i1][j2]==c and targetGrid[i2][j1]==c and targetGrid[i2][j2]==c:
                pass
            else:
                print("YES")
                return False

        
        
        
        heap=[]
        for c in lookup:
            heapq.heappush(heap,(-lookup[c]['A'],c))
        
        while(heap):
            _,c=heapq.heappop(heap)
            #print("c:{}".format(c))
            i1,i2,j1,j2=lookup[c]['i1'],lookup[c]['i2'],lookup[c]['j1'],lookup[c]['j2']
            for i in range(i1,i2+1):
                for j in range(j1,j2+1):
                    mat[i][j]=c
        
        
               
        
        #print(mat)
        if mat==targetGrid:
            return True
        return False
        
        
        
        
        
        """
        
        