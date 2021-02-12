
"""
Date:28/11/2020
Name:Sandeep Padhi
MCS20006

"""



def outerChkMyMatrix(mat):
    i=0
    matres=mat.copy()
    def check_util(mat):
        idx=0
        nonlocal i,matres
        if not isinstance(mat[0],list):
            if len(mat)!=3:
                matres=mat
                return False
            for e in mat:
                if chr(97+i)==e:
                    i=(i+1)%11
                    continue
                matres=mat
                return False
            return True
        for m in mat:
            if len(m)==0:
                matres=m
                return False
            if not check_util(m):
                return False
        return True
    ans=check_util(mat)
    return ans,matres







myMatrix0 = ['a', 'b', 'c']

result, myMat = outerChkMyMatrix(myMatrix0)
print('/nThe result of chcking the matrix0:', result)
print('The returned matrix is: ', myMat)

myMatrix1 = ['a', 'b']

result, myMat = outerChkMyMatrix(myMatrix1)
print('/nThe result of chcking the matrix1:', result)
print('The returned matrix is: ', myMat)

myMatrix2 = [ ['a', 'b', 'c'] ] 

result, myMat = outerChkMyMatrix(myMatrix2)
print('The result of chcking the matrix2:', result)
print('The returned matrix is: ', myMat)
print()

myMatrix3 = [ ['a', 'b', 'c'], ['d', 'e', 'f'] ] 

result, myMat = outerChkMyMatrix(myMatrix3)
print('The result of chcking the matrix3:', result)
print('The returned matrix is: ', myMat)
print()

myMatrix4 = [[[['a', 'b', 'c']]], ['d', 'e', 'f'] ] 

result, myMat = outerChkMyMatrix(myMatrix4)
print('The result of chcking the matrix4:', result)
print('The returned matrix is: ', myMat)
print()

myMatrix5 = [[[['a', 'b', 'c']]], 
             [[['d', 'e', 'f']]], 
             ['g', 'h', 'i'], ['j', 'k', 'z'] ] 

result, myMat = outerChkMyMatrix(myMatrix5)
print('The result of chcking the matrix5:', result)
print('The returned matrix is: ', myMat)
print()

myMatrix6 = [[[['a', 'b', 'c']]], 
             [[['d', 'z', 'f']]], 
             ['g', 'h', 'i'], ['j', 'k', 'a'] ] 

result, myMat = outerChkMyMatrix(myMatrix6)
print('The result of chcking the matrix6:', result)
print('The returned matrix is: ', myMat)
print()

myMatrix7 = [[[['a', 'b', 'c']]], 
             [[['d', 'e', 'f']]], 
             ['g', 'z', 'i'], ['j', 'k', 'a'] ] 

result, myMat = outerChkMyMatrix(myMatrix7)
print('The result of chcking the matrix7:', result)
print('The returned matrix is: ', myMat)
print()

myMatrix8 = [[[['a', 'b', 'c']]], 
             [[['d', 'e', 'f']], ['g', 'h', 'i']], 
             ['j', 'k', 'a'], ['b', 'c', 'd']]

result, myMat = outerChkMyMatrix(myMatrix8)
print('The result of chcking the matrix8:', result)
print('The returned matrix is: ', myMat)
print()

myMatrix9 = [[[['a', 'b', 'c']]], 
             [[['d', 'e', 'f']], ['g', 'h', 'i']], 
             ['j', 'k', 'a'], ['b', 'c', 'd'],
             []]

result, myMat = outerChkMyMatrix(myMatrix9)
print('The result of chcking the matrix9:', result)
print('The returned matrix is: ', myMat)
print()

myMatrix10 = [[[['a', 'b', 'c']]], 
             [[['d', 'e', 'f']], ['g', 'h', 'i']], 
             ['j', 'k', 'a'], ['b', 'c', 'd'],
             ['e', 'g', 'h', 'i']]

result, myMat = outerChkMyMatrix(myMatrix10)
print('The result of chcking the matrix10:', result)
print('The returned matrix is: ', myMat)
print()

myMatrix11 = [[[['a', 'b', 'c']]], 
             [[['d', 'e', 'f']], [[[[[[[[['g', 'h', 'i']]]]]]]]],
             ['j', 'k', 'a']], 
             ['b', 'c', 'd'], ['e', 'f', 'g'],
             ['h', 'i', 'j']]

result, myMat = outerChkMyMatrix(myMatrix11)
print('/nThe result of chcking the matrix11:', result)
print('The returned matrix is: ', myMat)


