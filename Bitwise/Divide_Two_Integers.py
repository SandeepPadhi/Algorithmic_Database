class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
               
        sign = (dividend>0 and divisor>0) or (dividend<0 and divisor<0)

        dividend , divisor = abs(dividend),abs(divisor)
        low,high = 1,dividend
        ans = dividend
        if divisor>dividend:
            return 0
        
        def find(Q,Divisor):
            S=0
            i=0
            while(Q):
                if Q&1:
                    S+=Divisor<<i
                i+=1
                Q>>=1
            return S
        
        while(low<=high):
            mid = (low + high)//2
            val = find(mid,divisor)
            if val>dividend:
                high = mid - 1
            else:
                ans= mid
                low = mid + 1
        MAX=2**31
        if (not sign and ans>MAX) or (sign and ans>(MAX -1)) :
            ans = MAX - 1
           
            
        return ans if sign else -ans