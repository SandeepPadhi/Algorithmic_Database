"""
Date:15/06/2021
The following program gives no of set bits at ith bit position from 1 to N inclusive.
"""
#N-number of consecutive number i.e 1-N , i:pos
def find(N,i):
    
    #N=1038373
    count=0
    #i=2
    if False:
        for n in range(1,N+1):
            if n&(1<<i):
                count+=1
        
    #print("count:{}".format(count))
    
    #mathematical approach
    dividend=(N+1)>>(i+1)
    v1=dividend*(2**i)
    rem=(N+1)%(2**(i+1))
    v2=rem-(1<<i)
    v2=v2 if v2>0 else 0
    ans=v1+v2
    print("count:{}".format(ans))
    print(ans>=N)
    return ans

print(find(10**9,2))