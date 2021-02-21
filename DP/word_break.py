"""
Date:16/02/2021
The following program is solved is using both recursion and DP.
Link:https://practice.geeksforgeeks.org/problems/word-break1352/1#
"""
def wordBreak(line, dictionary):
    # Complete this function
    
    dp=[[False for _ in range(len(line))] for _ in range(len(line))]
    for size in range(1,len(line)+1):
        #print("size:{}".format(size))
        for i in range(len(line)-size+1):
            j=i+size-1
            word=line[i:j+1]
            if word in dictionary:
                dp[i][j]=True
                continue
            for k in range(i,j):
                if dp[i][k] and dp[k+1][j]:
                    dp[i][j]=True
                    break
    return dp[0][-1]
        
    
    
    
    """
    dp={}
    def find(word):
        nonlocal dp
        if word in dp:
            return dp[word]
        if word in dictionary:
            dp[word]=True
            return True
        for i in range(1,len(word)):
            if find(word[:i]) and find(word[i:]):
                dp[word]=True
                return True
        dp[word]=False
        return False
            
            
    if find(line):
        return 1
    return 0
    
    
    """
    