"""
Date:24/03/2021
1353. Maximum Number of Events That Can Be Attended - Leetcode Medium

The following problem is solved using greedy approach -->sorting with start time + min heap with end time
"""
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        totaldays=max( end for start,end in events)
        heap=[]
        eventid=0
        Totalevents=0
        for d in range(1,totaldays+1):
            while(eventid<len(events) and events[eventid][0]==d):
                heapq.heappush(heap,events[eventid][1])
                eventid+=1
            
            while(len(heap)>0 and heap[0]<d):
                heapq.heappop(heap)
            
            if len(heap):
                heapq.heappop(heap)
                Totalevents+=1
        return Totalevents
                
        
        
        
        
        
        
        
        
        
        
        
        