import math

def Karatsuba(x,y):
    if x<10 or y<10:
        return x*y
    """
    n=max(len(str(x)),len(str(y)))
    m=math.floor(n/2)
    xh=math.floor(x/10**m)
    xl=x%10**m
    yh=math.floor(y/10**m)
    yl=y%10**m
    s1=karatsuba(xh,yh)
    s2=karatsuba(yh,yl)
    s3=karatsuba(xh+xl,yh+yl)
    s4=(s3-s2)-s1
    result = s1*(10**(2*m)) + s4*(10**m) + s2
    return result
    """
    n = max(len(str(x)),len(str(y)))
    m = math.floor(n/2)

    xh=math.floor(x/10**m)
    xl=x%10**m
    yh=math.floor(y/10**m)
    yl=y%10**m

    s1=Karatsuba(xh,yh)
    s2=Karatsuba(xl,yl)
    s3=Karatsuba(xh+xl,yh+yl)
    s4=(s3-s2)-s1
    result =s1*10**(2*m) + s4*10**m + s2
    return result


result=Karatsuba(3243,2342)
print(result)

