"""
Date:5/02/2021
Following program is solved using hashing.
We worked out a mathematical equation a+(d/2)=b,where d is the difference in sum btw two values.
Link:https://practice.geeksforgeeks.org/problems/swapping-pairs-make-sum-equal4142/1#
"""
class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        A=sum(a)
        B=sum(b)
        Aset=set(a)
        Bset=set(b)
        if A>B:
            d=(A-B)
            if d&1:
                return -1
            d=d//2
            for bb in b:
                if d+bb in Aset:
                    return 1
        else:
            d=B-A
            if d&1:
                return -1
            d=d//2
            for aa in a:
                if d+aa in Bset:
                    return 1
        return -1
            


#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends