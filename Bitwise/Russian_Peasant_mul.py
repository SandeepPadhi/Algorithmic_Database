"""
Date:1/02/2021
The following program is multiplying two numbers a8b without using * operator.
It is called Russian Peasant Algorithm

Link:https://www.geeksforgeeks.org/russian-peasant-multiply-two-numbers-using-bitwise-operators/
"""
a=12
b=4
ans=0
while(b>0):
    if b&1:
        ans+=a
    a<<=1
    b>>=1
print(ans)






