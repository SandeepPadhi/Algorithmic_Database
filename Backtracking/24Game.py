"""
Date:12/04/2021
679. 24 Game - Leetcode Hard

The following problem is solved using recursion
"""
class Solution:
    
    def judgePoint24(self, nums: List[int]) -> bool:
        
        def find(nums):
            #print("nums:{}".format(nums))
            if len(nums)==1:
                if abs(nums[0]-24)<0.01:
                    return True
            
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    vals=[]
                    a,b=nums[i],nums[j]
                    vals.append(a+b)
                    vals.append(a-b)
                    vals.append(b-a)
                    vals.append(a*b)
                    if a==0 or b==0:
                        vals.append(0)
                    else:
                        vals.append(a/b)
                        vals.append(b/a)
                    Arr=[]
                    for k in range(len(nums)):
                        if k!=i and k!=j:
                            Arr.append(nums[k])
                    for v in vals:
                        Arr.append(v)
                        if find(Arr):
                            return True
                        Arr.pop()
            return False
                
        if find(nums):
            return True
        
        return False

"""
   def judgePoint24(self, nums: List[int]) -> bool:
        #self.combination.append(2)
        def operation(a,op,b):
            if op=='*':
                return a*b
            elif op=='/':
                if b==0:
                    return -1
                return a/b
            elif op=='+':
                return a+b
            else:
                return a-b
            
        def find(A):
            #print(A)
            if len(A)==3:
                num=operation(A[0],A[1],A[2])
                if abs(num-24)<0.01:
                    return True
                return False
            i=0
            while(i+2<len(A)):
                num=operation(A[i],A[i+1],A[i+2])
                if find(A[:i] + [num] + A[i+3:]):
                    return True
                i=i+2
            return False
            
        combination=set()
        def findComb(A,ind):#This code is used to find all possible combinations
            nonlocal combination
            if ind==len(A):
                arr=tuple(a for a in A)
                combination.add(arr)
                return 
            for i in range(ind,len(A)):
                A[i],A[ind]=A[ind],A[i]
                findComb(A,ind+1)
                A[i],A[ind]=A[ind],A[i]
        
        
        findComb(nums,0)
        Arr=[0]*7
        for op1 in ('*','/','+','-'):
            for op2 in ('*','/','+','-'):
                for op3 in ('*','/','+','-'):
                    for comb in combination:
                        #print(comb)
                        Arr[0],Arr[1],Arr[2],Arr[3],Arr[4],Arr[5],Arr[6]=comb[0],op1,comb[1],op2,comb[2],op3,comb[3]
                        A=[a for a in Arr]
                        if find(A):
                            return True
        return False
            

"""