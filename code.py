import math

def result():
        n=int(input())
        s=input()
        lens=n
        xorstr=1
        val=0
        for i in range(lens):
            val=val+xorstr<<i
        xorstr=val
        m=int(s,base=2)
        #m=bin(m)

       # print(m)
        #For zero at the late
        count=0
        i=0
        check=True
        binarycheck=1
        while(i<lens):
            if check:
                check=False
                if m&binarycheck:
                    i=i+1
                    binarycheck<<=1
                    continue
                count=count+1
                m=m^xorstr
                i=i+1
                binarycheck<<=1
                continue
            check=True
            if m&binarycheck:
                count=count+1
                m=m^xorstr
                i=i+1
                binarycheck<<=1
                continue
            i=i+1
            binarycheck<<=1

        maxcount=count+1
        count=0
        check=False
        i=0
        binarycheck=1
        while(i<lens):
            if check:
                check=False
                if m&binarycheck:
                    binarycheck=binarycheck<<i
                    i=i+1
                    binarycheck<<=1
                    continue
                count=count+1
                m=m^xorstr
                i=i+1
                binarycheck<<=1
                continue
            check=True
            if m&i:
                count=count+1
                m=m^xorstr
                i=i+1
                binarycheck<<=1
                continue
            i=i+1
            binarycheck<<=1

        mincount=min(maxcount,count+1)
        return mincount     


T=int(input())
for _ in range(T):
    print(result())