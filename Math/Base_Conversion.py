"""
Date:17/06/2021
The following program is for conversion from decimal to given base and vice versa
"""

#conversion of num from Base:10 to Base:base 
def dec_to_base(num,base):
    ans=0
    i=0
    while(num):
        rem=num%base
        ans+=pow(10,i)*rem
        num//=base
        i+=1
    return ans

#conversion of number from Base:base to base:10
def base_to_decimal(num,base):
    ans=0
    i=0
    while(num):
        #ans*=10
        rem=num%10
        ans+=pow(base,i)*rem
        num//=10
        i+=1

    return ans
    
print(base_to_decimal(dec_to_base(1000,4),4))