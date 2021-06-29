class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(A):
        
        Sudoku=[]
        for a in A:
            temp=[]
            for aa in a:
                if aa==0:
                    temp.append('.')
                    continue
                temp.append(str(aa))
            Sudoku.append(temp)

        #print("sudoku:{}".format(Sudoku))
        
        
                                    
        def trydigit(x,y,d,Sudoku):
            for i in range(9):
                if Sudoku[i][y]==str(d) or Sudoku[x][i]==str(d):
                    return False
            for i in range((x//3)*3,(x//3)*3+3):
                for j in range((y//3)*3,(y//3)*3+3):
                    if Sudoku[i][j]==str(d):
                        return False
            
        
            #print("okay")
            return True


        
        def find(Sudoku):
            #print("Sudoku find:{}".format(Sudoku))
            check=False
            for i in range(9):
                for j in range(9):
                    if Sudoku[i][j]=='.':
                        #print("i:{},j:{}".format(i,j))
                        #print("Sudoku find:{}".format(Sudoku))

                        for d in range(1,10):
                            if trydigit(i,j,d,Sudoku):
                                Sudoku[i][j]=str(d)
                                if find(Sudoku):
                                    return True
                                Sudoku[i][j]='.'
                        return False
            
            return True
            
        if find(Sudoku):
            print("Succes")
        else:
            print("Failed")
        #print(Sudoku)

        A=[]
        for sod in Sudoku:
            A.append("".join(sod))
        return A
        
        


