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
            print("i:{}".format(i))
            i=lps[i-1]
        else:
            j+=1
print(lps)

text="joeuljjoeljojooeuljjoeljo"
i=0
j=0
while(i<len(text)):
    if text[i]==pat[j]:
        i+=1
        j+=1
    else:
        j=lps[j-1]
        if j==0:
            i+=1
    if j==len(pat):
        print("found at {}".format(i-j))
        j=lps[j-1]
    
    
    