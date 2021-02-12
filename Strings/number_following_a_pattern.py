"""
Date:6/02/2021
Following problem is solved using recursion.IMPORTANT PROBLEM
Link:https://practice.geeksforgeeks.org/problems/number-following-a-pattern/0/?company[]=Goldman%20Sachs&company[]=Goldman%20Sachs&difficulty[]=1&difficulty[]=2&page=1&query=company[]Goldman%20Sachsdifficulty[]1difficulty[]2page1company[]Goldman%20Sachs#
"""
#code
def find():
    P=[p for p in input()]
    N=len(P)+1
    Done=[False for _ in range(N+1)]
    def check(L,ind,Done,Last,Num):
        if L==N:
            return Num
        
        if P[ind]=='I':
            for i in range(Last+1,N+1):
                if Done[i]==False:
                    Done[i]=True
                    Num_ = Num*10 + i
                    Ans=check(L+1,ind+1,Done,i,Num_)
                    if Ans:
                        return Ans
                    Done[i]=False
        else:
            for i in range(1,Last):
                if Done[i]==False:
                    Done[i]=True
                    Num_ = Num*10 + i
                    Ans=check(L+1,ind+1,Done,i,Num_)
                    if Ans:
                        return Ans
                    Done[i]=False
        return False
    
    for i in range(1,N+1):
        Done[i]=True
        Ans=check(1,0,Done,i,i)
        if Ans:
            print(Ans)
            return
        Done[i]=False
    
                
            


T=int(input())
for _ in range(T):
    find()