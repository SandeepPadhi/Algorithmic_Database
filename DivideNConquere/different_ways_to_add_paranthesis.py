"""
Date:12/02/2021
241. Different Ways to Add Parentheses-Leetcode Medium

The following program is solved using Divide N conquere strategy

"""
class Solution:
    def diffWaysToCompute(self, Inp):
        Res=[]
        for i in range(len(Inp)):
            if Inp[i] in ('-','+','*'):
                A1=self.diffWaysToCompute(Inp[:i])
                A2=self.diffWaysToCompute(Inp[i+1:])
                for a1 in A1:
                    for a2 in A2:
                        if Inp[i]=='-':
                            Res.append(a1-a2)
                        elif Inp[i]=='+':
                            Res.append(a1+a2)
                        else:
                            Res.append(a1*a2)
        if len(Res)==0:
            Res.append(int(Inp))
        return Res
                            
        
        