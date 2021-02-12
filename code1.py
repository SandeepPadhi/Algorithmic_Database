T=int(input())
     
def findresult():
        m=input().split(" ")
        l=int(m[0])
        r=int(m[1])
        diff=r-l+2
        small=l-diff
        large=r+diff
        if small<=0 or small<=2*diff:
            pass
        else:
            return "YES"
        if large>2*l:
            return "NO"
        return "YES"
for _ in range(T):
         print(findresult())