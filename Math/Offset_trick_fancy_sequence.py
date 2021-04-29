"""
Date:27/04/2021
1622. Fancy Sequence - Leetcode Hard

The following problem is solved using maths logic..+ modular inverse multiplication.

The concept used are:
1)modular arithetic assumes normal rules of arithmetic under modular operation,so operations are lossless..
2)Whenver (N/D)%mod is to performed,then always do N*mulinv(D)%mod,so that ans is lossless ,as many information are lost using N/D and ans is in float whereas %operation under N/D should always give interger.

3)We use the offset technique.While inserting we modify the input by first subtracting by addition upto that point and then result val is divided by product to be multiplied,This modified value is stored in Seq list.

Hint:https://www.youtube.com/watch?v=Z0ymtF4dExU .. by erricto go to 39 mins

"""

class Fancy:

    def __init__(self):
        self.seq=[]
        self.add=0
        self.prod=1
        self.mod = 10**9 + 7
    def append(self, val: int) -> None:
        val=val-self.add
        
        mulinv=pow(self.prod,self.mod-2,self.mod)#Using fermet little theorem for primality test.
        
        val=val*mulinv #basically (val/prod)%mod
        self.seq.append(val%self.mod)
        

    def addAll(self, inc: int) -> None:
        self.add+=inc
        self.add%=self.mod
        

    def multAll(self, m: int) -> None:
        self.prod*=m
        self.prod%=self.mod
        self.add*=m
        self.add%=self.mod

    def getIndex(self, idx: int) -> int:
        if idx>=len(self.seq):
            return -1
        val=self.seq[idx]
        ans=val*self.prod + self.add
        return ans%self.mod
        

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)