
class Solution:
    def find(self,T,C):
        count=1
        i=0
        sumval=0
        while(i<len(C)):
            if sumval+C[i]<=T:
                sumval+=C[i]

            else:
                sumval=C[i]
                count+=1
            i+=1

        return count    
            
            
    def paint(self, A, B, C):
        if A>=len(C):
            #print("maxC:{}".format(max(C)))
            return max(C)*B
        low=max(C)
        high=sum(C)
        mintime=sum(C)
        while(low<=high):
            T=(low+high)//2
            count=self.find(T,C)
            if count>A:
                low=T+1
            else:
                mintime=T
                high=T-1
        return (mintime*B)%10000003
   

A = 1
B = 1000000
C = [ 1000000,1000000 ]
print("sum of C:{}".format(sum(C)))
soln=Solution()
ans=soln.paint(A,B,C)
print("I returned")
print(ans)





"""

class Solution:
    def paint(self, A, B, C):
        if A>=len(C):
            #print("maxC:{}".format(max(C)))
            return max(C)*B
        #C.sort()
        for i in range(1,len(C)):
            C[i]+=C[i-1]
        low=min(C)
        high=sum(C)
        mintime=sum(C)
        partitionfinal=[]
        while(low<=high):
            currentmin=(low+high)//2
            #print(currentmin)
            sub=0
            lowinit=0
            highinit=len(C)-1
            count=0
            partitions=[]
            while lowinit<len(C):
                lowtemp=lowinit
                hightemp=highinit
                Cindex=-1
	            
                while(lowtemp<=hightemp):
                    midtemp=(lowtemp+hightemp)//2
                    if C[midtemp]-sub==currentmin:
                        Cindex=midtemp
                        lowtemp=midtemp+1
                        #break
                    if C[midtemp]-sub<currentmin:
                        Cindex=midtemp
                        lowtemp=midtemp+1
                    if C[midtemp]-sub>currentmin:
                        hightemp=midtemp-1
                if Cindex==-1:
                    print("cindex..!!")
                    count+=1
                    break
                sub=C[Cindex]
                partitions.append(Cindex)
                lowinit=Cindex+1
                count+=1
            print("count:{}".format(count))

	        
            if count<=A:
                #print("mintime")
                mintime=currentmin
                print(partitions)
                partitionfinal[:]=partitions[:]
                high=currentmin-1
            else:
                low=currentmin+1
            
            print("mintime:{}".format(mintime))
        print("partitionsfinal:{}".format(partitionfinal))
        if mintime==10000000:
            return sum(C)
        return mintime*B

A = 5
B = 10
C = [ 658, 786, 531, 47, 169, 397, 914 ]

print("sum of C:{}".format(sum(C)))
soln=Solution()
ans=soln.paint(A,B,C)
print(ans)
"""