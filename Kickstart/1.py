
fp=open('inp.txt','r')
def find():
    N,K=map(int,next(fp).split())
    S=str(next(fp))[:1]
    print("N:{} , K:{}".format(N,K))
    print("S:{}".format(S))
    return 0

T=int(next(fp))
for i in range(1,T+1):
    Ans=find()
    print("Case #{}: {}".format(i,Ans))

fp.close()