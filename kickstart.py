
#True:Even
#False:Odd

def f(n,Oddeven):
    #if even:
    print("n:{}".format(n))

    lst=len(n)
    print("lst:{}".format(lst))
    if Oddeven:

        fst=int(n[0])
        org=fst
        if fst%2:
            fst-=1
        count=0

        if lst==1:
            while fst>=0:
                count+=1
                fst-=2
            print("last count:{}".format(count))
            return count


        if fst==org:
            fst-=2
        
        #while(fst>=0 and fst<org):
        while(True):
            count+=1
            fst-=2
            if fst<0:
                break
        print("even count:{}".format(count))
        if lst==1:
            return count
        ans=count*5**(lst-1)
        print("even ans:{}".format(ans))
        return ans+f(n[1:],not Oddeven)
    fst=int(n[0])
    print("fst:{}".format(fst))
    org=fst
    count=0
    


    if fst%2==0:
        fst-=1
    if lst==1:
        while fst>=0:
            count+=1
            fst-=2
        print("last count:{}".format(count))

        return count

    if fst==org:
        fst-=1
    while(True):
            count+=1
            fst-=2
            if fst<0:
                break
    
    print("count:{}".format(count))
    ans=count*5**(lst-1)
    print("ans:{}".format(ans))
   
    
    return ans+f(n[1:],not Oddeven)

def find():
    l,r=map(int,input().split())
    l=l-1
    l=[i for i in str(l)]
    r=[i for i in str(r)]

    rans=f(r,False)
    print("R:{}...{}".format(rans,r))
    print()

    lans=f(l,False)
    print("L:{}".format(lans,l))

    return rans-lans


T=int(input())
for t in range(T):
    print("Case #{}: {}".format(t+1,find()))


"""
3
5 15
120 125
779 783

  
Case #1: 6
Case #2: 3
Case #3: 2

  



"""