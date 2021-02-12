"""
Date:1/01/2021
Link:https://www.geeksforgeeks.org/add-two-bit-strings/
"""


str1 = '1100011'
str2 = '10'
if len(str1)>len(str2):
    s='0'*(len(str1)-len(str2))
    str2=s+str2
elif len(str2)>len(str1):
    s='0'*(len(str1)-len(str2))
    str1=s+str2
print("s1:{}".format(str1))
print("s2:{}".format(str2))
c=0
ansstr=''
for i in range(len(str1)-1,-1,-1):
    a=int(str1[i])
    b=int(str2[i])
    s=a^b^c
    c=(a&b)|(b&c)|(c&a)
    print("s:{},c:{}".format(s,c))
    ansstr=str(s)+ansstr
print(ansstr)
    