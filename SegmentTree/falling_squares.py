"""
Date:23/04/2021
699. Falling Squares - Leetcode Hard

The following program is solved using segment Trees
"""
class SegmentNode:
    def __init__(self,low,high):
        self.low=low
        self.high=high
        self.left=None
        self.right=None
        self.maxheight=0


class Solution:     
    
    def build(self,left,right):
        low=self.coords[left]
        high=self.coords[right+1]
        root=SegmentNode(low,high)
        if left==right:
            return root
        mid=(left+right)//2
        root.left = self.build(left,mid)
        root.right = self.build(mid+1,right)
        return root
        
        
    def query(self,low,high,root):
        if not root:
            return 0
        if root.high<=low or root.low>=high:
            return 0
        
        if low<=root.low and root.high<=high:
            return root.maxheight
        
        ans=max(self.query(low,high,root.left),self.query(low,high,root.right))
        return ans

    def update(self,low,high,root,val):
        if not root:
            return
        if root.high<=low or root.low>=high:
            return
        if low<=root.low and root.high<=high:
            root.maxheight=val
        self.update(low,high,root.left,val)
        self.update(low,high,root.right,val)
        if root.left:
            root.maxheight=max(root.maxheight,root.left.maxheight)
        if root.right:
            root.maxheight=max(root.maxheight,root.right.maxheight)
            
        
        
    
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
		# coordinates compression
        coords=set()
        for left,side in positions:
            p1,p2=left,left+side
            coords.add(p1)
            coords.add(p2)
        self.coords=sorted(list(coords))
        #print("cords:{}".format(self.coords))
        root = self.build(0,len(coords)-2)
        #print("root.low:{} , root.right:{}".format(root.low,root.high))
        res=[]
        maxval=0
        for left,side in positions:
            p1,p2=left,left+side
            h=self.query(p1,p2,root)+side
            #print("p1:{} , p2:{}".format(p1,p2))
            #print("h:{}".format(h))
            maxval=max(maxval,h)
            res.append(maxval)
            self.update(p1,p2,root,h)
        #print("maxheight root:{}".format(root.maxheight))
        return res
        