"""
Date:23/05/2021
Problem:Print all possible shortest chains to reach a target word

The following program is solved using BFS
Link:https://www.geeksforgeeks.org/print-all-possible-shortest-chains-to-reach-a-target-word/
"""

from collections import deque

string = ["poon", "plee", "same", "poie", "plea", "plie", "poin"]
beginWord = "toon"
endWord = "plea"
#print(set(beginWord))
queue=deque()
S=set()
S.add(beginWord)
#print(S)
queue.append(([beginWord],S))
#print(queue.popleft())

def check(s1,s2):
    count=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            count+=1
        if count>1:
            return False
    return True

P=set()
P.add('sandeep')
print('sandeep' not in P)
flag=True
while(queue and flag):
    count=len(queue)
    while(count):
        (path,S)=queue.popleft()
        #print("path:{} , S:{}".format(path,S))
        for s in string:
            if s not in S and check(s,path[-1]):
                if s==endWord:
                    print(path+[s])
                    flag=False
                    continue
                path1=path.copy()
                path1.append(s)
                SS=S.copy()
                SS.add(s)
                queue.append((path1,SS))
        count-=1

