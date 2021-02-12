"""
Date:5/02/2021
Following problem is solved using Hashing,sets and sorting

Link:https://practice.geeksforgeeks.org/problems/find-all-four-sum-numbers1732/1#
"""

#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required

#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required

def fourSum(arr, k):
    # code here
    Sum={}
    N=len(arr)
    for i in range(N):
        for j in range(i+1,N):
            s=arr[i]+arr[j]
            if s not in Sum:
                Sum[s]=[]
            Sum[s].append((i,j))
    R=set()
    for i in range(N):
        for j in range(i+1,N):
            s=arr[i]+arr[j]
            if k-s in Sum:
                a1=(i,j)
                for a2 in Sum[k-s]:
                    #print("a1:{},a2:{},set:{}".format(a1,a2,set(a1)-set(a2)))
                    if len(set(a1)-set(a2))<2:
                        p#rint("common")
                        continue
                    L=[arr[a1[0]],arr[a1[1]],arr[a2[0]],arr[a2[1]]]
                    L.sort()
                    #print("L:{}".format(L))
                    #print("Aeedddddddddddddddddddddddddddddddddddd")
                    R.add(tuple(L))
    R=list(R)
    R.sort()
    return R

                        

                    



#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Main


# } Driver Code Ends
#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ans=fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends