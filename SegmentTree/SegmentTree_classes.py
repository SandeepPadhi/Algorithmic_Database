
"""
Date:24/04/2021
The following problem finds out folowing:
Given an array Arr and L and R,find out whether there is any barrier in between or not.

We have solved the problem using Segment Tree .
"""
class Solution:
    def __init__(self, nums):
        
        self.maxsize=1000000000
        self.S=[False]*4*len(nums)
        self.nums=nums
    
        
        #Below function can also be used as update function by removing comments.
    def build(self,segpos,left,right):
            if left==right:
                self.S[segpos]=self.nums[left]
                return 
            mid=(left+right)//2
            #if pos<=mid:
            self.build(2*segpos,left,mid)
            #else:
            self.build(2*segpos+1,mid+1,right)
            self.S[segpos]=self.S[2*segpos]|self.S[2*segpos+1]
        
        
    def query(self,segpos,segleft,segright,left,right):
            if left>right:
                return False
            if segleft==left and segright==right:
                return self.S[segpos]
            
            segmid=(segleft+segright)//2
            v1=self.query(2*segpos,segleft,segmid,left,min(segmid,right))
            v2=self.query(2*segpos+1,segmid+1,segright,max(segmid+1,left),right)
            return v1|v2
    
    def update(self,segpos,segleft,segright,pos):
        if segleft==segright:
            self.S[segpos]=not self.S[segpos]
            return
        mid=(segleft+segright)//2
        if pos<=mid:
            self.update(segpos*2,segleft,mid,pos)
        else:
            self.update(segpos*2 + 1 ,mid+1,segright,pos)
        self.S[segpos]=self.S[segpos] | self.S[2*segpos+1]
        
        

N=10
Arr=[False]*N
Arr[4]=True

        
Seg=Solution(Arr)
Seg.build(1,0,N-1)
print("done")
ans=Seg.query(1,0,N-1,2,3)
print(ans)
Seg.update(1,0,N-1,8)
ans=Seg.query(1,0,N-1,5,6)
print(ans)

Seg.update(1,0,N-1,6)

ans=Seg.query(1,0,N-1,5,6)
print(ans)

                  





"""
#True False Segment Tree

N=10
Arr=[False]*N
Arr[4]=True
S=[False]*4*N

def build(S,pos,start,end):
    
    if start==end:
        S[pos]=Arr[start]
        print("yes")
        return
    mid=(start+end)//2
    build(S,2*pos,start,mid)
    build(S,2*pos+1,mid+1,end)
    S[pos]=S[2*pos]|S[2*pos+1]

def query(S,pos,L,R,start,end):
    print("pos:{} , start:{} , end:{},L:{},R:{}".format(pos,start,end,L,R))
    if L>R:
        return False
    if L==start and R==end:
        return S[pos]
    mid=(start+end)//2
    S1=query(S,2*pos,L,min(mid,R),start,mid)
    S2=query(S,2*pos+1,max(mid+1,L),R,mid+1,end)
    return S1|S2
    
    
    
pos=1
start=0
end=len(Arr)-1
build(S,pos,start,end)
print(S)
print(query(S,1,2,4,0,N-1))


#True False Segment Tree

N=10
Arr=[False]*N
Arr[4]=True
S=[False]*4*N

def build(S,pos,start,end):
    
    if start==end:
        S[pos]=Arr[start]
        print("yes")
        return
    mid=(start+end)//2
    build(S,2*pos,start,mid)
    build(S,2*pos+1,mid+1,end)
    S[pos]=S[2*pos]|S[2*pos+1]

def query(S,pos,L,R,start,end):
    print("pos:{} , start:{} , end:{},L:{},R:{}".format(pos,start,end,L,R))
    if L>R:
        return False
    if L==start and R==end:
        return S[pos]
    mid=(start+end)//2
    S1=query(S,2*pos,L,min(mid,R),start,mid)
    S2=query(S,2*pos+1,max(mid+1,L),R,mid+1,end)
    return S1|S2
    
    
    
pos=1
start=0
end=len(Arr)-1
build(S,pos,start,end)
print(S)
print(query(S,1,2,4,0,N-1))


"""