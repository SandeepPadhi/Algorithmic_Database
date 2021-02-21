class Solution:
    def printLargest(self,arr):
	    # code here
        def partition(low,high,arr):
            i=low-1
            P=arr[high]
            for j in range(low,high):
	            A=arr[j]
	            PA=P+A
	            AP=A+P
	            if PA>AP:
	                i+=1
	                arr[i],arr[j]=arr[j],arr[i]
            arr[i+1],arr[high]=arr[high],arr[i+1]
            return i+1
	            
	    
        def quicksort(low,high,arr):
            if low<high:
                p=partition(low,high,arr)
                quicksort(low,p-1,arr)
                quicksort(p+1,high,arr)
            
        
        quicksort(0,len(arr)-1,arr)
        arr.reverse()
        return "".join(arr)

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends