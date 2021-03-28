"""
Date:28/03/2021
728. Self Dividing Numbers - Leetcode Easy

The following program is solved using loops

"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        Ans=[]
        for num in range(left,right+1):
            done=True
            temp=num

            while(num):
                n=num%10
                if n==0 or temp%n!=0:
                    done=False
                    break
                num=num//10
            if done:
                Ans.append(temp)
            
        return Ans
            
        