
def find():
    n,U,R,D,L=map(int,input().split())
    if any(m>n for m in (U,R,D,L)):
        print("NO")
        return
    UA,RA,DA,LA=U,R,D,L
    
    if DA==n:
        RA-=1
        LA-=1
    if RA==n:
        UA-=1
        DA-=1
    if LA==n:
        UA-=1
        DA-=1
    if UA==n:
        RA-=1
        LA-=1
        
    if any(m<0 for m in (UA,RA,DA,LA) ):
        print("NO")
        return
    
    if UA<=n-2:
        UA=0
    if RA<=n-2:
        RA=0
    if DA<=n-2:
        DA=0
    if LA<=n-2:
        LA=0
    
    if any(m<0 for m in (UA,RA,DA,LA) ):
        print("NO")
        return
        
    print("YES")        
        


t=int(input())
for _ in range(t):
    find()