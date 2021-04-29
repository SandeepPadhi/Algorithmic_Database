"""
Date:29/04/2021
1224. Maximum Equal Frequency - leetcode hard

The following problem is solved using maintain frequency of frequencies of the numbers in the array.These are updated in real time
"""
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        ans=0
        freq=Counter()
        freq_freq=Counter()
        for i in range(len(nums)):
            num=nums[i]
            freq_freq[freq[num]]-=1
            if freq_freq[freq[num]]<=0:
                del freq_freq[freq[num]]
            freq[num]+=1
            freq_freq[freq[num]]+=1
            #print(freq_freq)
            flag=False
            if len(freq_freq)==1:
                itr = iter(freq_freq.items())
                itr=next(itr)
                #print(itr)
                if itr[0]==1:
                    flag=True
                if itr[1]==1:
                    flag=True
            elif len(freq_freq)==2:
                itr=iter(freq_freq.items())
                p=next(itr)
                q=next(itr)
                #print("p:{},q:{}".format(p,q))
                if (p[0]==1 and p[1]==1) or (q[0]==1 and q[1]==1):
                    flag=True
                if (p[0]==q[0]+1 and p[1]==1) or (q[0]==p[0]+1 and q[1]==1):
                    flag=True
            if flag:
                ans=i+1
                    
                      
        
        return ans