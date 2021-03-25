"""
Date:28/01/2021
Following program is for finding LCM in range:[L,R]
We use segment Tree with update operation with lazy operation
"""

S = [2, 8, 6, 9, 8, 6, 8, 2, 11,8,7] 
Tree=[1]*4*len(S)

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def build(node,start,end):
    
    global Tree
    if start==end:
        Tree[node]=S[start]
        return Tree[node]
    mid=(start+end)//2p
    l_lcm=build(node*2+1,start,mid)
    r_lcm=build(node*2+2,mid+1,end)
    Tree[node]=(l_lcm*r_lcm)//gcd(l_lcm,r_lcm)
    return Tree[node]

def update(node,val,pos,start,end):
    global Tree,S
    if start==end:
        Tree[node]=val
        S[start]=val
        print("start:{},pos:{}".format(start,pos))
        return
    mid=(start+end)//2
    if pos<=mid:
        update(2*node+1,val,pos,start,mid)
    else:
        update(2*node+2,val,pos,mid+1,end)
    l,r = Tree[2*node+1],Tree[2*node+2]
    Tree[node]=l*r//gcd(l,r)
    return

def query(node,start,end,L,R):
    if end<L or start>R:
        return 1
    if L<=start and end<=R:
        return Tree[node]
    mid=(start+end)//2
    l_lcm=query(2*node+1,start,mid,L,R)
    r_lcm=query(2*node+2,mid+1,end,L,R)
    return (l_lcm*r_lcm)//gcd(l_lcm,r_lcm)

print(build(0,0,len(S)-1))
print(query(0,0,len(S)-1,1,2))
print(update(0,7,1,0,len(S)-1))
print(S)
print(query(0,0,len(S)-1,1,2))

    