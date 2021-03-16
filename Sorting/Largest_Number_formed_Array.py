class Solution:
    def printLargest(self,arr):
	    # code here
	   from functools import cmp_to_key
	   arr = [ str(a) for a in arr]
	   
	   def compare(A,P):
	       AP=A+P
	       PA=P+A
	       if AP>PA:
	           return -1
	       elif AP<PA:
	           return 1
	       else:
	           return 0
	   
       arr.sort(key=cmp_to_key(compare))	   
	   return "".join(arr)