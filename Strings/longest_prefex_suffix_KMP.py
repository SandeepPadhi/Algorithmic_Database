pat="joeuljjoeljo"
lps=[0]*len(pat)
j=1
i=0
while(j<len(pat)):
    if pat[i]==pat[j]:
        lps[j]=i+1
        i+=1
        j+=1
    else:
        if i!=0:
            i=lps[i-1]
        else:
            j+=1
print("lps:{}".format(lps[-1]))

        
    