"""
Date:31/01/2021
Find a number which appears once,other num appears thrice
"""
A=[12, 1, 12, 3, 12, 1, 1, 2, 3, 3]

#Soln 1
"""
ans=3*sum(set(A))-sum(A)
ans//=2
print(ans)
"""

#Soln2
result=0
for i in range(32):
    x=1<<i
    sm=0
    for a in A:
        if a&x:
            sm+=1
    if sm%3==1:
        result|=x
print(result)
            
        
    