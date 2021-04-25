"""
Date:25/04/2021
1298. Maximum Candies You Can Get from Boxes - Leetcod Hard

The following problem is solved using simple Queue ,loop and logic
"""
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        Boxes=[False]*len(status)
        
        ans=0
        
        Q=deque()
        seen=set()

        for i in initialBoxes:
            Boxes[i]=True
            
        def check(Boxes,Q,status,seen):    
            for i in range(len(status)):
                
                if i not in seen and  Boxes[i]&status[i]:
                    Q.append(i)
                    seen.add(i)
        check(Boxes,Q,status,seen)
        
        
        while(Q):
            #print(Q)
            I=Q.pop()
            ans+=candies[I]
            
            for c in containedBoxes[I]:
                Boxes[c]=True
                if status[c] and c not in seen:
                    seen.add(c)
                    Q.append(c)
                
            for k in keys[I]:
                status[k]=True
                if k not in seen and Boxes[k]:
                    seen.add(k)
                    Q.append(k)
            
        return ans
                
        
        