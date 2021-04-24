"""
Date:24/04/2021
664. Strange Printer - leetcode hard

The following program is solved using DP - bottom up approach
"""
class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0
        n=len(s)
        dp =[[sys.maxsize]*n for _ in range(len(s))]
        for i in range(n):
            dp[i][i]=1
        
        for l in range(2,n+1):
            for i in range(n-l+1):
                j=i+l-1
                dp[i][j]=1+dp[i+1][j]
                for k in range(i+1,j+1):
                    if s[k]==s[i]:
                        dp[i][j]=min(dp[i][j],dp[i][k-1] + (dp[k+1][j] if (k+1)<=j else 0))
        
        return dp[0][-1]
        
        
        
        """
        boxes=['#' for _ in s]
        
        
        def find(i,j,boxes):
            if i>j:
                return 0
            ans=10000000000000
            original=[b for b in boxes[i:j+1]]
            
            #print("i:{} , j:{} , boxes len:{}".format(i,j,len(boxes)))
            box_com=Counter(boxes[i:j+1])
            #print(box_com)
            box_com=box_com.most_common(1)[0][0]
            #print("box_com:{}".format(box_com))
            #s_com=Counter(s[i:j+1]).most_common(1)[0]
            s_count=Counter(s[i:j+1]).most_common(1)
            s_count=s_count[0][1]
                            
            if s_count==1:
                if boxes[i] in s[i:j+1]:
                    return j-i
                else:
                    return j-i+1

            
            #print(s_count)

            #print(Counter(original[i:j+1]))
            
            for c,n in Counter(s[i:j+1]).items():
                #print("c:{} , n:{} , s_count:{}".format(c,n,s_count))
                if s_count==n:
                    if box_com!=c:
                        val=1
                        for k in range(i,j+1):
                            boxes[k]=c
                    else:
                        val=0
                    
                    print("boxes:{} , s:{} ,i:{} , j:{},s_count:{} , c:{}".format(boxes[i:j+1],s,i,j,s_count,c))
                    #print("s_com:{}".format(s_com[0]))
                    left=i
                    while(left<j+1):
                        while(left<j+1 and s[left]==c):
                            left+=1
                        right=left
                        while(right<j+1 and s[right]!=c):
                            right+=1
                        val+=find(left,right-1,boxes)
                        left=right
                    #print("val:{}".format(val))
                    ans=min(ans,val)
                    m=0
                    for k in range(i,j+1):
                        boxes[k]=original[m]
                        m+=1

            return ans

        
        return find(0,len(s)-1,boxes)
        
        
        """