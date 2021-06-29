"""
Date:18/06/2021
The following problem is solved using two approaches:
1)Heap-Not so efficient

2)Queues and Stack-efficient
->Here,we keep the stack always in descending order of values.
We,store index in the stack.

Here,deque is used to simulated stack and queue.
"""


import heapq
from collections import deque
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        Q=deque()
        Ans=[]
        for i in range(B):
            while(Q and A[i]>A[Q[-1]]):
                Q.pop()
            Q.append(i)
        #print(Q)
        for i in range(B,len(A)):
            Ans.append(A[Q[0]])
            while(Q and Q[0]<=i-B):
                Q.popleft()
            
            while(Q and A[i]>A[Q[-1]]):
                Q.pop()
            Q.append(i)
        Ans.append(A[Q[0]])
        return Ans


        


        """
        N=len(A)
        heap=[]
        size=0
        Ans=[]
        for right in range(N):
            if len(heap)<B:
                heapq.heappush(heap,(-A[right],right))
                if len(heap)==B:
                    Ans.append(-heap[0][0])
            else:
                while(heap and heap[0][1]<right-B+1):
                    heapq.heappop(heap)
                heapq.heappush(heap,(-A[right],right))
                Ans.append(-heap[0][0])
        
        
        return Ans

        """