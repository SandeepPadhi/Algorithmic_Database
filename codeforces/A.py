

def check(N,lookup,c1,c2):
    #print("c1:{} , c2:{}".format(c1,c2))
    N1=N.copy()
    for i in lookup[c1]:
        N[i]='('
    for i in lookup[c2]:
        N[i]=')'
    #print("N:{}".format(N))
    stack=[]
    for n in N:
        if len(stack)==0:
            if n==')':
                return False
            stack.append(n)
        elif stack[-1]=='(' and n==')':
            stack.pop()
        elif stack[-1]=='(' and n=='(':
            stack.append(n)
    if len(stack)==0:
        return True

    N1=N.copy()
    for i in lookup[c1]:
        N1[i]='('
    for i in lookup[c2]:
        N1[i]='('
    #print("N:{}".format(N1))
    stack=[]
    for n in N1:
        if len(stack)==0:
            if n==')':
                return False
            stack.append(n)
        elif stack[-1]=='(' and n==')':
            stack.pop()
        elif stack[-1]=='(' and n=='(':
            stack.append(n)
    if len(stack)==0:
        return True
    
    N1=N.copy()
    for i in lookup[c1]:
        N1[i]=')'
    for i in lookup[c2]:
        N1[i]=')'
    #print("N:{}".format(N1))
    stack=[]
    for n in N1:
        if len(stack)==0:
            if n==')':
                return False
            stack.append(n)
        elif stack[-1]=='(' and n==')':
            stack.pop()
        elif stack[-1]=='(' and n=='(':
            stack.append(n)
    if len(stack)==0:
        return True



    
    return False

def find():
    n=input()
    N=[c for c in n]
    lookup={'A':[],'B':[],'C':[]}
    for i in range(len(N)):
        lookup[N[i]].append(i)
    #Replace all occurance of i=0
    F=N[0]
    for i in lookup[N[0]]:
        N[i]='('
    if F=='A':
        if check(N.copy(),lookup,'B','C') or check(N.copy(),lookup,'C','B') :
            print("YES")
            return
    elif F=='B':
        if check(N.copy(),lookup,'A','C') or check(N.copy(),lookup,'C','A'):
            print("YES")
            return
    else:
        if check(N.copy(),lookup,'A','B') or check(N.copy(),lookup,'B','A'):
            print("YES")
            return
    print("NO")
        

t=int(input())
for _ in range(t):
    find()

"""
4
AABBAC
CACA
BBBBAC
ABCA

"""