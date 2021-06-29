/*
Date:27/05/2021

*/


int Solution::isMatch(const string A, const string B) {
    
    int lena=A.length();
    int lenb=B.length();
    
    vector<vector<bool>> dp(lena+1,vector<bool>(lenb+1,false));
    dp[0][0]=true;
    
    int i=0;
    while(i<lenb && B[i]=='*'){
        dp[0][i+1]=true;
        i+=1;
    }
    
    for(int i=0;i<lena;i++)
        for(int j=0;j<lenb;j++){
            if (B[j]=='.' || A[i]==B[j]) dp[i+1][j+1]=dp[i][j];
            else if (B[j]=='*'){
                //match karna hai
                if (j-1>=0 && (B[j-1]==A[i] || B[j-1]=='.')){
                    dp[i+1][j+1]=dp[i+1][j+1]||dp[i][j+1]||dp[i][j-1];//match again,match once
                }
                dp[i+1][j+1]=dp[i+1][j+1]||dp[i+1][j-1];//don't match
            }
        }
    if (dp[lena][lenb]) return 1;
    return 0;
    
}
