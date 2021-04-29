/*
Date:27/04/2021
1483. Kth Ancestor of a Tree Node - Leetcode Hard

The following problem is solved using Binary Lifting technique or jump pointer technique
*/

class TreeAncestor {
public:
    int log=0;
    vector<vector<int>> up;
    vector<int> depth;
    TreeAncestor(int n, vector<int>& parent) {
        depth= vector<int>(n);

        while(1<<(log)<=n) log+=1;
        log+=5;
        up=vector<vector<int>>(n,vector<int>(log));
        cout<<up[0][1]<<endl;
        parent[0]=0;
        for(int i=0;i<n;i++) up[i][0]=parent[i];
        
        vector<bool> V=vector
            
            <bool>(n);
        V[0]=true;
        depth[0]=0;
        for(int i=n-1;i>=0;i--){
            if (!V[i]){
                vector<int> Stack;
                int tempnode=i;
                while(!V[tempnode]){
                    Stack.push_back(tempnode);
                    tempnode=parent[tempnode];
                }
                
                while(Stack.size()){
                    depth[Stack[Stack.size()-1]]=depth[tempnode]+1;
                    tempnode=Stack[Stack.size()-1];
                    Stack.pop_back();
                    V[tempnode]=true;
                }
                
            }
        }
        
        //cout<<"here"<<endl;
        
        //cout<<"up"<<up<<end;
        
        for(int j=1;j<log;j++){
            for(int v=0;v<n;v++){
                //cout<<"j:"<<j<<", v:"<<v<<endl;
                //cout<<up[0][0]<<endl;
                //cout<<up[v][j-1]<<endl;
                up[v][j]=up[up[v][j-1]][j-1];
            }
        }
        
    //cout<<"perfect"<<endl;
    }
    
    int getKthAncestor(int node, int k) {
        if(depth[node]<k){
            return -1;
        }
        
        for(int i=0;i<=log;i++){
            if(k&(1<<i)){
                node=up[node][i];
            }
        }
    
        return node;
    }
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor* obj = new TreeAncestor(n, parent);
 * int param_1 = obj->getKthAncestor(node,k);
 */