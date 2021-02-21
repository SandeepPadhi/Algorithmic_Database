"""
Date:16/02/2021
The following problem is solved using Stack.
Link:https://practice.geeksforgeeks.org/problems/find-largest-word-in-dictionary2430/1#
"""

class Solution:
    def findLongestWord (ob, S, d):
        # code here 
        Ans=""
        D=d
        for d in D:
            s=[i for i in S]

            flag=0
            for d1 in d:
                while(len(s) and s[0]!=d1):
                    s.pop(0)
                if len(s)==0:
                    flag=1
                    break
            if flag==0:
                if len(d)>len(Ans):
                    Ans=d
                elif len(d)==len(Ans) and d<Ans:
                    Ans=d
        return Ans
                
