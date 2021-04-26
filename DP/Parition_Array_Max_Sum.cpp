/*
Date:26/04/2021
1043. Partition Array for Maximum Sum - Leetcode Medium

The following problem is solved dp
*/

#define INF 10000000


class Solution {
public:
    int dp[500][500];
    
    int max(int a,int b){
        if(a>b) return a;
        return b;
        
    }
    
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n=arr.size();
        vector<int> dp(n+1,-INF);
        dp[0]=0;
        for(int i=0;i<n;i++){
            int intervalmax=-INF;
            for(int j=i;j<n&&j-i+1<=k;j++){
                intervalmax=max(intervalmax,arr[j]);
                dp[j+1]=max(dp[j+1],dp[i]+(j-i+1)*intervalmax);
            }
            
        }
        
        return dp[n];
        
        /*
        
        cout<<min(12,43);
        for(int i=0;i<arr.size();i++)
            for(int j=0;j<arr.size();j++) 
                dp[i][j]=-1;
        
        for(int i=0;i<arr.size();i++) dp[i][i]=arr[i];
        
        //return calculate(0,arr.size()-1,k,arr);
        
        //cout<<"starting"<<endl;
        for(int size=2;size<=arr.size();size++){
            for(int left=0;left<arr.size()-size+1;left++){
                int right=left+size-1;
                int ans=-INF;
                int maxval=-INF;
                for(int mid=left;mid<=min(right,left+k-1);mid++){
                    //cout<<"left"<<left<<", mid:<<"<<mid<<",right: "<<right<<", size: "<<size<<endl;

                    maxval=max(maxval,arr[mid]);
                    int d=mid-left+1;
                    if(mid+1<=right) ans=max(ans,d*maxval+dp[mid+1][right]);
                    else ans=max(ans,d*maxval);
                    
                    
                }
                //cout<<"left:"<<left<<" , right:"<<right<<" , ans:"<<ans<<endl;
                dp[left][right]=ans;
            }
        }
        
        
        return dp[0][arr.size()-1];
        
        */
        //return calculate(0,arr.size()-1,k,arr);
    }
    
    int calculate(int left,int right,int k,vector<int>& arr){
        if (left>right){
            return 0;
        }
        if (dp[left][right]!=-1) return dp[left][right];
        int ans=-INF;
        int maxval=-INF;
        for(int mid=left;mid<=min(left+k-1,right);mid++){
            int d=mid-left+1;
            if (arr[mid]>maxval) maxval=arr[mid];
            ans=max(ans,d*maxval+calculate(mid+1,right,k,arr));
        }
        
        
        dp[left][right]=ans;
        return ans;            
    }
    
};