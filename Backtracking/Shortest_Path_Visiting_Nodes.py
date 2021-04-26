/*
Date:26/04/2021
847. Shortest Path Visiting All Nodes - Leetcode hard

The following problem is solved brute force
*/


#define MAX 15
#define INF 1000

class Solution {
public:
    int shortestpath[MAX][MAX];
    int N=0;
    int dp[MAX][1<<MAX];
    
    int calculate(int x,int mask){
        if(mask==((1<<N)-1)) return 0;
        
        if(dp[x][mask]>=0) return dp[x][mask];
        int cost=INF;
        for(int i=0;i<N;i++){
            if((mask&(1<<i))==0){
                int val=calculate(i,mask|(1<<i))+shortestpath[x][i];
                
                if (val<cost) cost=val;
            }
        }
        
        dp[x][mask]=cost;
        //cout<<cost;
        return cost;
    }
    
    int shortestPathLength(vector<vector<int>>& graph) {
        N=graph.size();
        int best=INF;
        for(int i=0;i<graph.size();i++) for(int j=0;j<N;j++) shortestpath[i][j]=MAX;
        
        //building adjacency graph
        for(int i=0;i<N;i++) for(int j=0;j<graph[i].size();j++)
            shortestpath[i][graph[i][j]]=1;
        
        //floyd-warshall algo
        for(int k=0;k<N;k++) for(int i=0;i<N;i++) for(int j=0;j<N;j++)
            if (shortestpath[i][k]+shortestpath[k][j]<shortestpath[i][j]){
                shortestpath[i][j]=shortestpath[i][k]+shortestpath[k][j];
            }
        
        for(int i=0;i<N;i++) for(int j=0;j<(1<<N);j++) dp[i][j]=-1;
        
        for(int i=0;i<N;i++){
            int val=calculate(i,1<<i);
            if (val<best) best=val;
        }
        
        
        return best;
        
    }
};