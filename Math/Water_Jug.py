"""
Date:22/02/2021

365. Water and Jug Problem - Leetcode - Medium

The following problems is solved using:
1)It seems that just by finding the gcd we can solve the problem
2.simple recursion and set for lookup.
"""
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z==0 or (x+y>=z and z%gcd(x,y)==0):
            return True
        return False
        
        #You can do following things to find out how is the condition when True condition is satisfied
        #Dollowing operations can be performed at any given time
        #completely fill X
        #completely fill Y
        #pour into Y from X
        #pour into X from Y
        #empty X
        #empty Y
        dp=set() #To avoid repetitions
        def find(X,Y):
            nonlocal dp
            if (X,Y) in dp:
                return False
            dp.add((X,Y))
            if X==z or Y==z or X+Y==z:
                return True
            
            #completely fill X           
            if find(x,Y):
                    return True
            
            #completely fill Y
            if find(X,y):
                    return True
            
            #pour into X from Y
            d=x-X
            pour=min(Y,d)
            if find(X+pour,Y-pour):
                    return True
            
            #pour into Y from X
            d=y-Y
            pour=min(X,d)
            if find(X-pour,Y+pour):
                    return True
        
            #empty X
            if find(0,Y):
                    return True
            
            #empty Y
            if find(X,0):
                    return True
        
            return False
        return find(0,0)
        