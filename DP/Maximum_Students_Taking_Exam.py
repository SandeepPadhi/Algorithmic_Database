"""
Date:17/04/2021
1349. Maximum Students Taking Exam - Leetcode Hard

The following problem is solved using bitwise manipulation and DP
"""
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m=len(seats)
        n=len(seats[0])
        
        @lru_cache(None)
        def dp(pos,prevrow,currow):
            if pos==m*n:
                return 0
            
            i,j=divmod(pos,n)
            if j==0:
                prevrow=currow
                currow=0

            #Not take seat
            ans=dp(pos+1,prevrow,currow)
            
            #Take seat
            if seats[i][j]=='.':
                l=tl=r=tr=True
                
                if j!=0:
                    l=(currow&(1<<(j-1))==0)
                    if i>0:
                        tl=(prevrow&(1<<(j-1))==0)
                if j!=n-1:
                    tr=(prevrow&(1<<(j+1))==0)
                    
        
                if l and tl and r and tr:
                    ans=max(ans,1+dp(pos+1,prevrow,currow|1<<j))
            
            
            return ans
        
        
        
        
        
        return dp(0,0,0)

    
    
    """
    def maxStudents(self, seats: List[List[str]]) -> int:
        row=len(seats)
        col=len(seats[0])
        
        if col==1:
            count=0
            for s in seats:
                if s[0]=='.':
                    count+=1
            return count
        
        
        @lru_cache(None)
        def find(prev,row_no):
            #print("prev:{},row_no:{}".format(prev,row_no))
            if row_no==-1:
                return 0
            Ans=0
            for seat in range(1<<col):
                temp=seat
                count=0
                i=0
                done=False
                while(temp>>i):
                    if (temp>>i)&1==1 and seats[row_no][i]=="#":
                        done=True
                        break
                    elif (temp>>i)&1==1 and seats[row_no][i]=='.':
                        if i==0:
                            if (prev>>(i+1))&1==1 or (seats[row_no][i+1]=='.' and (temp>>(i+1))&1==1):
                                done=True
                                break
                        elif i==col-1:
                            if (prev>>(i-1))&1==1 or  (seats[row_no][i-1]=='.' and (temp>>(i-1))&1==1):
                                done=True
                                break
                        else:
                            if (prev>>(i+1))&1==1 or (prev>>(i-1))&1==1 or (seats[row_no][i-1]=='.' and (temp>>(i-1))&1==1 )or (seats[row_no][i+1]=='.' and (temp>>(i+1))&1==1):
                                done=True
                                break 
                        count+=1

                    i+=1
                if done:
                    continue
                #print("Seat:{},prev:{},row_no:{}".format(seat,prev,row_no))

                Ans=max(Ans,count+find(seat,row_no-1))        
            
            #print("RETURNING prev:{},row_no:{},Ans:{}".format(prev,row_no,Ans))
            return Ans
        
        return find(0,row-1)
    
    
    """