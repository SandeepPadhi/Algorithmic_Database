"""
Date:2/01/2021
The following program finds if string forms a chain or not
the idea is to use check if graph forms Eulerian Circuit or not
"""
#User function Template for python3
class Solution:
    
                
    def isCircle(self, N, A):
        # code here
        Adj=[[] for _ in  range(26)]
        I=[0]*26
        for w in A:
            u,v=w[0],w[-1]
            Adj[ord(u)-97].append(ord(v)-97)
            I[ord(v)-97]+=1
        #print("Adj:{}".format(Adj))
        #print("I:{}".format(I))
        for i in range(26):
            
            if len(Adj[i])!=I[i]:
                return 0
        
        C=0
        V=[False]*26
        def dfs(u):
            nonlocal V
            V[u]=True
            for v in Adj[u]:
                if V[v]==False:
                    dfs(v)
        
        for i in range(26):
            if V[i]==False and len(Adj[i])>0:
                dfs(i)
                C+=1
        #print("C:{}".format(C))
        if C==1:
            return 1
        return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        A = input().split()
        
        ob = Solution()
        print(ob.isCircle(N, A))
# } Driver Code Ends