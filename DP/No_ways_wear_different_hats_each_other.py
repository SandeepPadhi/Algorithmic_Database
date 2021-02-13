"""
Date:13/02/2021
The following program is solved using DP+Bitmasking
"""
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        N=len(hats)
        M=10**9 + 7
        hatslookup={}
        for person in range(len(hats)):
            for h in hats[person]:
                if h not in hatslookup:
                    hatslookup[h]=[]
                hatslookup[h].append(person)
                
        @lru_cache(None)
        def find(index,mask):
            if mask==0:
                return 1
            if index>40:
                return 0
            ans=find(index+1,mask)
            if index in hatslookup:
                for p in hatslookup[index]:
                    if mask&(1<<p):
                        ans+=find(index+1,mask^(1<<p))
            return ans
        return find(1,(1<<N)-1)%M



"""
Date:13/02/2021
The following program is recursive solution of the problem.But gives TLE.
"""
"""
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        hatslookup=set()
        
        @lru_cache(None)
        def find(index,mask):
            if index==len(hats):
                #print("mask:{}".format(mask))
                return 1
            ans=0
            for h in hats[index]:
                if h not in hatslookup:
                    hatslookup.add(h)
                    ans+=find(index+1,mask+"X"+str(h)+"X")
                    hatslookup.remove(h)
            #print("mask:{} ,val:{}".format(mask,ans))
            return ans
            
            
        Ans=find(0,"")
        return Ans

"""
        
