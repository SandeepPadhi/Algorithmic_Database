"""
Following problem is solved using logic and is classic problem
"""
"""

def leastInterval(tasks, n):
        #First job with highest count whose waiting time ==0
        Count={}
        for t in tasks:
            if t not in Count:
                Count[t]=0
            Count[t]+=1
        
        counts=list(Count.values())
        counts.sort()
        maxx=counts[-1]-1
        idle=2*maxx
        for i in range(len(counts)-1):
            idle-=min(counts[i],maxx)
        

        
        return idle + len(tasks) if idle>0 else len(tasks)
L=["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(leastInterval(L,n))

"""

#Following implementation is made using heaps
def leastInterval(self,tasks, n):
        #First job with highest count whose waiting time ==0
        Count={}
        for t in tasks:
            if t not in Count:
                Count[t]=0
            Count[t]+=1
        
        counts=list(Count.values())
        counts.sort()
        maxx=counts[-1]-1
        idle=n*maxx
        for i in range(len(counts)-1):
            idle-=min(counts[i],maxx)
        

        
        return idle + len(tasks) if idle>0 else len(tasks)
L=["A","A","A","B","B","B"]
n = 2
print(leastInterval(L,n))