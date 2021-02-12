"""
Date:5/01/2021
The following program is solved using dynamic programming.
"""
#User function Template for python3

def maximizeTheCuts(n,x,y,z):
    lookup=[[-100000 for _ in range(n+1)]  for _ in range(3)]
    lookup[0][0],lookup[1][0],lookup[2][0]=0,0,0
    x,y,z=z,y,x
    for i in range(1,n+1):
        ncur=i
        for j,cut in enumerate((x,y,z)):
            if ncur>=cut:
                lookup[j][ncur]=1+max(lookup[k][ncur-cut] for k in range(3))

            #print("lookup:{}".format(lookup))
    ans=max(lookup[0][-1],lookup[1][-1],lookup[2][-1])
    if ans<=0:
        return 0
    return ans
        
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(maximizeTheCuts(n,x,y,z))
# } Driver Code Ends