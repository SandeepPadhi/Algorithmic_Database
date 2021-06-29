int Solution::isMatch(const string A, const string B) {
    const int lena=A.length();
    const int lenb=B.length();
    
    vector<vector<bool>> dp(lena+1,vector<bool>(lenb+1,false));
    dp[0][0]=true;
    int i=0;
    while(i<lenb && B[i]=='*'){
        dp[0][i+1]=true;
        i+=1;
    }
    for(int i=0;i<lena;i++){
        for(int j=0;j<lenb;j++){
            if (A[i]==B[j] || B[j]=='?') dp[i+1][j+1]=dp[i+1][j+1]||dp[i][j];
            else if (B[j]=='*') dp[i+1][j+1]=dp[i+1][j+1]||dp[i][j]||dp[i+1][j]||dp[i][j+1];
        }
    }
    return dp[lena][lenb];
    
}