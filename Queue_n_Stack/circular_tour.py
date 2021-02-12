"""
Date:5/02/2021
The following program is solved using Queue.
It is basically two pointer problem with circular queue
"""

'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''
#Your task isto complete this function
#Your function should return the starting point

def tour(lis, n):
    start=0
    end=1
    balance=lis[0][0]-lis[0][1]
    while(balance<0 or start!=end):
        while(balance<0 and start!=end):
            balance-=lis[start][0]-lis[start][1]
            start=(start+1)%n
            if start==0:
                return -1
        balance+=lis[end][0]-lis[end][1]
        end=(end+1)%n
    
    
    return start
#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends