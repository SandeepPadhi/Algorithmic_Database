"""
Date:12/04/2021
315. Count of Smaller Numbers After Self - Leetcode Hard

The following problem is solved using binary search
"""
class Node:
    def __init__(self,v):
        self.left=None
        self.right=None
        self.freq=1
        self.val=v
        self.count=1


class Solution:
    
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        Root=Node(nums[-1])
        count=[0]
        
        def find(root,num,count):
            #print("count:{}".format(count))
            #print("rootval:{} , num:{} , count:{}".format(root.val,num,count))
            root.count+=1
            if root.val==num:
                root.freq+=1
                ans=count
                if root.left:
                    return ans+root.left.count
                return ans
            
            if num<root.val:
                if root.left==None:
                    node=Node(num)
                    root.left=node
                    return count
                else:
                    return find(root.left,num,count)
            else:
                if root.right==None:
                    node=Node(num)
                    root.right=node
                    count+=root.freq
                    if root.left:
                        count+=root.left.count
                    return count
                else:
                    count=count+root.freq
                    if root.left:
                        count+=root.left.count
                    return find(root.right,num,count)
                    
                   
        
        
        for i in range(len(nums)-2,-1,-1):
            ans=find(Root,nums[i],0)
            #print("num:{},ans:{}".format(nums[i],ans))
            count.append(ans)
        count.reverse()
        return count
            
        
        
        
        
        
        
        
        
        
        
        """
        count=[0]
        Sorted=[nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            ans=bisect.bisect_left(Sorted,nums[i])
            count.append(ans)
            Sorted.insert(ans,nums[i])
        
        count.reverse()
        return count
        """