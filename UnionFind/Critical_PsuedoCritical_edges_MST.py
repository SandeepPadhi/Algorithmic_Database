"""
Date:16/05/2021
1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree - Leetcode Hard

The following problem is solved using Union Find + Krushkal algorithm 
"""

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges =[(w,a,b,i) for i,(a,b,w) in enumerate(edges) ]
        edges.sort()
        
        #print(edges)
        #We will find MST
        
        
        def findMST(inc,exc):
            parent=[i for i in range(n)]
            rank=[1]*n
    
            def find(p,parent):
                if parent[p]!=p:
                    parent[p]=find(parent[p],parent)
                return parent[p]
        
            def union(u,v,parent,rank):
                p1=find(u,parent)
                p2=find(v,parent)
                
                if rank[p1]>rank[p2]:
                    parent[p2]=p1
                    #rank[p1]+=rank[p2]
                else:
                    rank[p2]+=1
                    parent[p1]=p2
            
            mst=0
            count=0
            if inc>=0:
                w,u,v,_ = edges[inc]
                mst+=w
                union(u,v,parent,rank)
                count+=1
                
         
            for i in range(len(edges)):
                    
                if i==exc:
                    continue
                    
                w,u,v,_=edges[i]
                if find(u,parent)!=find(v,parent):
                    count+=1
                    union(u,v,parent,rank)
                    mst+=w
                    
            return mst,count
        
        
        C=[]
        P=[]
        mst,_=findMST(-1,-1)
        #print(mst)
        
        
        for i in range(len(edges)):
            #print("edges:{}".format(edges[i]))
            #exclusion
            mst1,count=findMST(-1,i)
            #print("mst1:{},count:{}".format(mst1,count))
            if mst<mst1 or count!=(n-1):
                #print("yes")
                C.append(edges[i][3])
            else:
                if mst==findMST(i,-1)[0]:
                    P.append(edges[i][3])
        
        return [C,P]
        
                
                