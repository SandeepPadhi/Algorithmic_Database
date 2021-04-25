"""
Date:25/04/2021
1840. Maximum Building Height

The following program is solved using greedy way.
Here,we use the technique of two-pass adjustment i.e by going forward onces and backward onces to put the numbers in its right place.

"""
class Solution:
    def maxBuilding(self, n: int, res: List[List[int]]) -> int:
        if len(res)==0:
            return n-1
        
        res.append([1,0])
        res.sort()
        for i in range(1,len(res)):
            id1,h1=res[i-1][0],res[i-1][1]
            id2,h2=res[i][0],res[i][1]
            d=id2-id1
            res[i][1]=min(res[i][1],res[i-1][1]+d)
        
        #print("here")
        #print("len of res:{}".format(len(res)))
        
        for i in range(len(res)-2,-1,-1):
            id1,h1=res[i][0],res[i][1]
            id2,h2=res[i+1][0],res[i+1][1]
            d=id2-id1
            res[i][1]=min(res[i][1],res[i+1][1]+d)
        ans=0
        for i in range(len(res)):
            id1,h1=res[i-1][0],res[i-1][1]
            id2,h2=res[i][0],res[i][1]
            d=id2-id1
            hdiff=abs(h1-h2)
            remain=d-hdiff
            ans=max(ans,max(h1,h2)+remain//2)

            
        
        
        
        
        
        return max(ans,res[-1][1]+n-res[-1][0])