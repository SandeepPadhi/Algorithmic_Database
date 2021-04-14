"""
Date:13/04/2021
815. Bus Routes - Leetcode Hard

The following program is solved using BFS
"""
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        from collections import deque,defaultdict

        graph=defaultdict(set)
        for routeId,route in enumerate(routes):
            for stop in route:
                graph[stop].add(routeId)
        #print(graph)
        queue=deque()
        seen_stop=set()
        seen_route=set()
        seen_stop.add(source)
        
        queue.append(source)
        #print("queue start:{}".format(queue))
        ans=0
        while(len(queue)>0):
            count=len(queue)
            #print("queue:{}".format(list(queue)))
            #print("count:{}".format(count))
            for _ in range(count):
                stop=queue.popleft()
                if stop==target:
                    #print("found")
                    return ans
                
                for routeId in graph[stop]:
                    if routeId not in seen_route:
                        seen_route.add(routeId)
                        
                        for newstop in routes[routeId]:
                            if newstop not in seen_stop:
                                seen_stop.add(newstop)
                                queue.append(newstop)
                                
            ans+=1
        
        
        return -1
            
        