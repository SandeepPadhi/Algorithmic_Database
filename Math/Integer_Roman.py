"""
Date:11/03/2021
Integer_To_Roman
The following program is solved using simple hashing and math
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        lookup={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        N=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        i=0
        Ans=""
        while(i<len(N) and num>=0):
            while(num-N[i]>=0):
                Ans+=lookup[N[i]]
                num-=N[i]
            i+=1
            
        return Ans
            
        