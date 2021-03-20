"""
Date:20/03/2021
1632. Rank Transform of a Matrix

VERY IMPORTANT...ONE OF THE MOST INTUITIVE PROBLEM.

The use of R and C to store rank in the increasing order of the values of matrix is also an important
idea which can be used in many problems

The following program is solved using Union-Find + DP + Sorting
"""
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        
        Parent = [[(i,j) for j in range(len(matrix[0]))] for i in range(len(matrix))]
        Rank = [[ 1 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        R=[0]*len(matrix)
        C=[0]*len(matrix[0])
        Ans = [[ 0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        
        #Union-all Elements
        def find(x,y):
            if Parent[x][y]==(x,y):
                return (x,y)
            Parent[x][y]=find(Parent[x][y][0],Parent[x][y][1])
            return Parent[x][y]
        
        def Union(p1,p2):
            x1,y1=p1[0],p1[1]
            x2,y2=p2[0],p2[1]
            
            P1 = find(x1,y1)
            P2= find(x2,y2)
            
            if Rank[P1[0]][P1[1]]>Rank[P2[0]][P2[1]]:
                Parent[P2[0]][P2[1]] = P1
                Rank[P1[0]][P1[1]]+=1
            else:
                Rank[P2[0]][P2[1]]+=1
                Parent[P1[0]][P1[1]] = P2
            
            find(x1,y1)
            find(x2,y2)
            
                
            
        
        for i in range(len(matrix)):
            V=set()
            M={}
            for j in range(len(matrix[0])):
                if matrix[i][j] in V:
                    Union(M[matrix[i][j]],(i,j))
                else:
                    M[matrix[i][j]]=(i,j)
                    V.add(matrix[i][j])
            
        for j in range(len(matrix[0])):
            V=set()
            M={}
            for i in range(len(matrix)):
                if matrix[i][j] in V:
                    Union(M[matrix[i][j]],(i,j))
                else:
                    M[matrix[i][j]]=(i,j)
                    V.add(matrix[i][j])
        
        #print("Parent:{}".format(Parent))
        Map={}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                P=find(i,j)
                if P not in Map:
                    Map[P]=[]
                Map[P].append((i,j))
        #print("Map:{}".format(Map))
        
        U=[]
        for x,y in Map:
            U.append((matrix[x][y],Map[(x,y)]))
        U.sort()
        
        for _ , Con in U :
            r=0
            for x,y in Con:
                r=max(r,R[x],C[y])
            for x,y in Con:
                R[x]=r+1
                C[y]=r+1
                Ans[x][y]=r+1
            
        return Ans
            
        
        
                
        
        
                    
        
        