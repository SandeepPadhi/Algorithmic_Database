"""
Date:18/04/2021
5736. Single-Threaded CPU - Leetcode Medium

The following problem is solved using Heap and logic.
This kind of problems are quite common.Remember them.
The key is to sort and loop over the array and put elements in the heap that satisfy the timing
"""


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks=[ (ent,pt,i) for i,(ent,pt) in enumerate(tasks)]
        tasks.sort()
        #print(tasks)
        heap=[]
        #t=tasks[0][0]
        i=0
        Ans=[]
        t=0
        while(i<len(tasks)):
            #print("t:{}".format(t))
            
            
            while(i<len(tasks) and tasks[i][0]<=t):
                ent,pt,ind=tasks[i]
                i+=1
                heapq.heappush(heap,(pt,ind))
            
            if len(heap)==0:
                if i<len(tasks):
                    t=tasks[i][0]
                continue
            
            #if len(heap)
            
            pt,ind=heapq.heappop(heap)
            #print("Adding ind:{} at t:{}".format(ind,t))
            Ans.append(ind)
            t+=pt
        while(len(heap)):
            pt,index=heapq.heappop(heap)
            Ans.append(index)
        return Ans
            
            
            
        

        #[6,1,2,9,4,10,0,11,5,13,3,8,12,7] - Expected