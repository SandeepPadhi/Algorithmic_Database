

import heapq
import numpy as np
import random
class State(object):
    def __init__(self,val,end,path,parent):
        self.path=path[:]+[val]
        self.parent=parent
        self.value=val
        self.children=[]
        self.visited=visited
        self.dist=self.getdist(val,end)

    #finds distance between start and end string--->Heuristics
    def getdist(self,val,end):
        count=0
        for i in range(len(end)):
            count+=abs(i-val.index(end[i]))**7
        return count

    def getchildren(self,visited):
        if len(self.children)==0:
            for i in range(len(self.value)-1):
                val=self.value[:i]+self.value[i+1]+self.value[i]+self.value[i+2:]
                if val in visited or getdist(val,end)>self.dist:
                    continue
                child=State(val,end,self.path[:],self)
                self.children.append(child)


end='abcdefghijklmnopqrstuvwxyz123456789)(*&^%$#@!~QWERTYUIOPASDFGHJKLZXCVBNM'
#start='*&^%$#@!~QWERTYUIOPASDFGHJKLabcdefghijklmnopqrstuvwxyz123456789)('
start='ZXCVBNMLKJHGFDSAPOIUYTREWQ~!@#$%^&*()987654321zyxwvutsrqponmlkjihgfedcba'

visited=set()

game=State(start,end,[],0)

#finds distance between start and end string--->Heuristics

def getdist(val,end):
    count=0
    for i in range(len(val)):
        count+=abs(i-end.index(val[i]))**7
    return count
heap=[(getdist(start,end),0,0,game)]


count=0
Ans=None

#We use priority queue depending on the distance value.
#Each state stores the path till itselfs and other things as can be found in the class above
while(len(heap) and len(heap)<500000):#To avoid memory overflow
    fn,c,cost,node=heapq.heappop(heap)
    #print("fn:{},c:{} , count:{}".format(fn,c,count))
    if node.value==end:
        Ans=node
        break
    print("val:{}".format(node.value))
    visited.add(node.value)
    node.getchildren(visited)
    #print("here")
    for child in node.children:
        if child.value not in visited:
            d=getdist(child.value,end)
            heapq.heappush(heap,(d,random.randint(0,1000000000),cost+1,child))
            count+=1

print("Path from start to end is as follows:")
for g in Ans.path:
    print("{}->".format(g))
print("Final ans:{},count:{}".format(len(Ans.path),count))

    




