
"""
Date:4/02/2021

955. Delete Columns to Make Sorted II - Leetcode Medium


The following program is solved using BFS.
The idea is:
1)We group indices into separate groups where the character at those strings and at that particular index must be 
lexicographically sorted.
2)We can it is not lexicographical sorted then we move into next index using same groups
3)If individual groups are lexicographically sorted,then we regroup those indices having similar characters having length greater then 1.
"""
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ind=0
        S=[[i for i in range(len(strs))]]
        count=0
        while(ind<len(strs[0])):
            done=False
            for s in S:
                prev=s[0]
                for i in s[1:]:
                    if strs[i][ind]<strs[prev][ind]:
                        done=True
                        break
                    prev=i
                if done:
                    break
            if done:
                count+=1
            else:
                #Regrouping indices
                T=[]
                for s in S:
                    left,right=0,0
                    while(right<len(s)):
                        while(right<len(s) and strs[s[right]][ind]==strs[s[left]][ind]):
                            right+=1
                        if right-left>1:
                            T.append(s[left:right])
                        left=right
                    
                S=T
            ind+=1
        
        return count
        
        