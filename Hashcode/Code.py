#step 1: Get input and use right data structure
#Most probably sortiing may be used

name1="a.txt"
name2="b.txt"
name3="c.txt"
name4="d.txt"
name5="e.txt"
name6="f.txt"

name1out="a_out.txt"
name2out="b_out.txt"
name3out="c_out.txt"
name4out="d_out.txt"
name5out="e_out.txt"
name6out="f_out.txt"

inputfile=name4
outputfile=name4out


def output(Ans):
    with open(outputfile,'a') as fp:#Name of the file
        fp.write(Ans)
        #fp.write("2\n")


def find(fp):
    count=0 
    #print(next(fp))#used to get next line Input
    Ans=[]
    #for line in fp:
    line=next(fp)
    D,I,S,V,F=map(int,line.split())
    #print("D:{} , I:{} , V:{} , S:{} ,F:{}".format(D,I,V,S,F))

    #We also have to name intersections


    i=0
    Streets={}
    interstreet={}
    intersignal={}
    signal={}
    Roadfreq={}
    while(i<S):
        line=next(fp)
        #print("line:{}".format(line))
        B,E,name,l=line.split()
        if int(E) not in signal:
            signal[int(E)]=[]
        interstreet[(B,E)]=(name,int(l))
        #interstreet[E]=(name,int(l))
        signal[int(E)].append(name)
        intersignal[name]={}
        Roadfreq[name]=0
        Streets[name]={"start":B,"end":E,"L":int(l)}
        i+=1
    #print("Streets:{}".format(Streets))
    #print("SIGNAL:{}".format(signal))
    i=0
    Cars={}
    while(i<V):
        line=next(fp)
        Vinp=line.split()
        #print("Vinp:{}".format(Vinp))
        Roadfreq[Vinp[1]]+=1
        j=2
        p=int(Vinp[0])
        path=[]
        s,e=Streets[Vinp[1]]["start"],Streets[Vinp[1]]["end"]
        path.append(s)
        path.append(e)
        t=0
        while(j<=p):
            s,e=Streets[Vinp[j]]["start"],Streets[Vinp[j]]["end"]
            Roadfreq[Vinp[j]]+=1
            t+=Streets[interstreet[(s,e)][0]]["L"]
            path.append(e)
            j+=1
        Cars[i]={"P":int(Vinp[0]),"sp":Vinp[1:],"path":path,"T":t}
        i+=1
    
    #print("Streets:{}\n\n".format(Streets))
    #print("Cars:{}\n\n".format(Cars))
    #print("interstreet:{}\n\n".format(interstreet))
    #print("Roadfreq:{}".format(Roadfreq))
    #print("signal:{}".format(signal))

    
    #We will implement Schedule
    with open(outputfile,'a') as fp:
        #A
        fp.write(str(I)+"\n")
        i=0
        while(i<I):
            fp.write(str(i)+"\n")
            prior=[]
            #print("i:{}".format(i))
            for s in signal[i]:
                prior.append((-Roadfreq[s],s,i))
            prior.sort()
            #print("prior:{}".format(prior))
            fp.write(str(len(prior))+'\n')
            l=len(prior)

            for freq,name,inter in prior:
                #print("l:{}".format(l))
                #if -freq>500:
                fp.write(name+" "+str(10)+"\n")
                l-=1
            i+=1




    



    print("Now")

    
    #print(len(Ans))


    #To print Ans
    #output(Ans)



    

with open(inputfile) as fp:#Name of the file
    find(fp)
	