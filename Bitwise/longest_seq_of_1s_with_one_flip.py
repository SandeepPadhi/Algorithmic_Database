"""
Date:2/01/2021
Following problem is solved using DP+bit masking
Link:https://www.geeksforgeeks.org/find-longest-sequence-1s-binary-representation-one-flip/
"""
n=1775
print("n:{}".format(bin(n)))
k=-1
i=0
maxsize=0
valsize=[0]*32
while(i<32):
  #iterating over zero
   while(i<32 and not n&(1<<i)):
       i+=1
   j=i
   if j>=32:
       break
   while(i<32 and n&(1<<i)):
       i+=1
   k=i-1
   valsize[k]=valsize[j]=k-j+1
maxval=1
for i in range(1,31):
    maxval=max(maxval,1+valsize[i-1]+valsize[i+1])
print("maxval:{}".format(maxval))