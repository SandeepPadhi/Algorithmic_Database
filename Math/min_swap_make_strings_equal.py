"""
Date:24/02/2021
1247. Minimum Swaps to Make Strings Equal - Leetcode - Medium

The following problem is solved using loops and keeping counts of x's and y's in both string fast current index
"""

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        s1=[s for s in s1]
        s2=[s for s in s2]
        x1c,x2c,y1c,y2c=0,0,0,0
        for s in s1:
            if s=='x':
                x1c+=1
            else:
                y1c+=1
        for s in s2:
            if s=='x':
                x2c+=1
            else:
                y2c+=1
        
        if (x1c+x2c)&1==1 or (y1c+y2c)&1==1:
            return -1
        count=0
        
        def find1(start,c):
                last=-1
                for i in range(start,len(s1)):
                    if s1[i]==c:
                        last=i
                        if s1[i]!=s2[i]:
                            return i
                return last
        
                    
        def find2(start,c):
                last=-1
                for i in range(start,len(s2)):
                    if s2[i]==c:
                        last=i
                        if s1[i]!=s2[i]:
                            return i
                return last
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                if s1[i]=='x':
                    x1c-=1
                    x2c-=1
                else:
                    y1c-=1
                    y2c-=1
                continue
                
            if s2[i]=='x':
                if x2c>y1c:
                    #find for x in s2
                    ind=find2(i+1,'x')
                    s1[i],s2[ind]=s2[ind],s1[i]
                    x2c-=1
                    y2c+=1
                else:
                    #find for y in s1
                    ind=find1(i+1,'y')
                    s2[i],s1[ind]=s1[ind],s2[i]
                    y1c-=1
                    x1c+=1
                
            else:
                if y2c>x1c:
                    #find for y in s2
                    ind=find2(i+1,'y')
                    s1[i],s2[ind]=s2[ind],s1[i]
                    y2c-=1
                    x2c+=1
                else:
                    #find for x in s1
                    ind=find1(i+1,'x')
                    s2[i],s1[ind]=s1[ind],s2[i]
                    x1c-=1
                    y1c+=1
            count+=1
            i+=1
        return count
                
            
            