"""
Date:11/04/2021
Google Codejam-Round 1A
Append Sort
The following problem is solved using Maths + Logic
"""


T=int(input())


for t in range(1,T+1):
    N=int(input())
    A=list(map(int,input().split()))
    a=A[0]
    i=1
    cnt=0
    #print(a,end=" ")
    while(i<N):
        b=A[i]
        if a<b:
            a=b
            #print(a,end=" ")
            i+=1
            continue
        sa=str(a)
        sb=str(b)
        la=len(sa)
        lb=len(sb)
        if la==lb:
            cnt+=1
            b*=10
            a=b
        else:
            k=la-lb
            if b*(10**k)>a:
                b*=(10**k)
                cnt+=k
                a=b
            elif b*(10**k)+(10**k)-1<=a:
                #print("Yes")
                b*=10**(k+1)
                a=b
                cnt+=(k+1)
            else:
                cnt+=k
                b=b*(10**k)+int(str(a)[len(str(b)):])+1
                a=b
        #print(a,end=" ")
        i+=1
    
    #print(a)
    #print(A)
    #print()
    print("Case #{}: {}".format(t,cnt))
    