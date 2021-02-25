#step 1: Get input and use right data structure
#Most probably sortiing may be used

name1="a_example.txt"
name2=""
name3=""
name4=""
name5=""
name6=""

name1out="a_out.txt"
name2out=""
name3out=""
name4out=""
name5out=""
name6out=""

inputfile=name1
outputfile=name1out


def output(Ans):
    with open(outputfile,'a') as fp:#Name of the file
        fp.write(Ans)
        #fp.write("2\n")


def find(fp):
    count=0 
    print(next(fp))#used to get next line Input
    Ans=[]
    for line in fp:
        count += 1
        print("Line{}: {}".format(count, line.strip()))
        output(line)
    print("Now")
    #print(len(Ans))


    #To print Ans
    #output(Ans)



    

with open(inputfile) as fp:#Name of the file
    find(fp)
	