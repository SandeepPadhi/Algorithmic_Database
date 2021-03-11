"""
Date:11/03/2021
986. Interval List Intersections - Leetcode Medium

The following problem is solved using simple loops and logic.

"""
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i,j=0,0
        Ans=[]
        while(i<len(firstList) and j<len(secondList)):
            if firstList[i][0]<=secondList[j][0]<=firstList[i][1]:
                l=secondList[j][0]
                r=min(secondList[j][1],firstList[i][1])
                Ans.append([l,r])
                if firstList[i][1]<secondList[j][1]:
                    i+=1
                else:
                    j+=1
                
            elif secondList[j][0]<=firstList[i][0]<=secondList[j][1]:
                l=firstList[i][0]
                r=min(firstList[i][1],secondList[j][1])
                Ans.append([l,r])
                if firstList[i][1]<secondList[j][1]:
                    i+=1
                else:
                    j+=1
            elif firstList[i][1]<secondList[j][0]:
                i+=1
            elif secondList[j][0]<firstList[i][1]:
                j+=1
                
        return Ans
                
                
                
                
            