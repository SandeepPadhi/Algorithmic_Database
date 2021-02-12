myMatrix = [[ [], [] ],
                 [ [] ],
                 [ [], [], []],
                 [ [] ],
                 [ [], [], []],
                 []]


def outerfill(myMatrix):
    strval=input("Enter your string")
    lenstr=len(strval)
    count=0
    def innerfill(matrix):
        nonlocal count
        print("matrix:{}".format(matrix))
        if len(matrix)==0:
            matrix.append(strval[count])
            count+=1
            count%=lenstr
            return
        for m in matrix:
            innerfill(m)

    innerfill(myMatrix)

outerfill(myMatrix)
print("Output:{}".format(myMatrix))


"""
Here,input is taken from user
Input:SandeepPadhi
Output:Output:[[['s'], ['a']], [['n']], [['d'], ['e'], ['e']], [['p']], [['s'], ['a'], ['n']], ['d']]

"""



