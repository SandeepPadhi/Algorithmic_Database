
S={chr(97+i):chr(97+i)+"12" for i in range(0,26)}
C={chr(65+i):chr(65+i)+"12" for i in range(0,26)}
N={str(i):str(i)+"12" for i in range(0,26)}

SCN={"small1":S,"caps1":C,"nums1":N}

hw1Dict={ scn:{ scn1:SCN[scn1] for scn1 in ("small1","caps1","nums1")}  for scn in {"small","caps","nums"}} 

#Following will print Dictionary
print(hw1Dict)


#Answers 
print(hw1Dict['small']['small1']['a'])
print(hw1Dict['caps']['caps1']['A'])
print(hw1Dict['nums']['nums1']['0'])
print(hw1Dict['small']['small1']['z'])
print(hw1Dict['caps']['caps1']['Z'])
print(hw1Dict['nums']['nums1']['9'])

