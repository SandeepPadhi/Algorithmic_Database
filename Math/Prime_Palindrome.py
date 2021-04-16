"""
Date:15/04/2021
866. Prime Palindrome - Leetcode Medium

All Odd Length Palindrome are multiples of 11,hence they cannot be prime numbers.

The following problem is solved using fermet's little theorem for primality testing
Important Ideas learnt:
1.)Fermet Little Theorem
2.)Modular Binary Exponentiation
3.)Getting Odd Palindrome of a number


"""
class Solution:
    def primePalindrome(self, N: int) -> int:
        import random
        
        if 8<=N<=11:
            return 11
        
        def getOddPalindrome(n):
            num=n
            n//=10
            while(n):
                res=n%10
                num=num*10+res
                n//=10
            return num
        
        #@lru_cache(None)
        def power(a,n,m):
            res=1
            while(n>0):
                if n%2:
                    res=res*a
                    res%=m
                    n-=1
                else:
                    a=(a**2)%m
                    n//=2
            return res%m
        
        def checkPrime(p):
            k=3
            for _ in range(k):
                #print("p-2:{}".format(p-2))
                a=random.randint(2,p-2)
                if power(a,p-1,p)!=1:
                    return False
            return True
        
        Prime=[2,3,5,7,11]
        
        #s=len(N)
        d=len(str(N))//2
        #print("d:{}".format(d))
        for i in range(max(2,10**(d)),10**5):
            
            p=getOddPalindrome(i)
            if p in Prime:
                if p>=N:
                    return p
                continue                
            
            if checkPrime(p):
                if p>=N:
                    return p