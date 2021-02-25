import numpy as np
npEmpDataDef=np.dtype([('id','i4'),('name','a64'),('age','u1'),('height','u1')])
numEmp=5
npEmpArr=np.zeros(numEmp,dtype=npEmpDataDef)
npName=['san']*numEmp
def assignEmpName(npEmpArr):
    for i in range(numEmp):
        npEmpArr[i]['name']=npName[i]
def assignEmpID(npEmpArr):
    for i in range(numEmp):
        npEmpArr[i]['id']=i
def assignEmpAge(npEmpArr):
    for i in range(numEmp):
        npEmpArr[i]['age']=np.random.randint(20, high=60)
def assignEmpHeight(npEmpArr): 
    for i in range(numEmp):
        npEmpArr[i]['height']=np.random.randint(120, high=160)
        
def findAvgs(npEmpArr):
    import time 
    st=time.process_time_ns()
    avg,height=np.average(npEmpArr['age']),np.average(npEmpArr['age'])
    et=time.process_time_ns()
    print("Numpy time:{}".format(et-st))
    return et-st

def findavgsPy(npEmpArr):
    import time 
    st=time.process_time_ns()
    s=0
    for i in range(numEmp):
        s+=npEmpArr[i]['age']
    avg=s/numEmp
    s=0
    for i in range(numEmp):
        s+=npEmpArr[i]['height']
    height=s/numEmp
    et=time.process_time_ns()
    print("Python time:{}".format(et-st))
    return et-st


    


import time 

for n in range(5,500,50):
    numEmp=n
    npEmpArr=np.zeros(numEmp,dtype=npEmpDataDef)
    npName=['san']*numEmp

    #st=time.process_time_ns()
    assignEmpName(npEmpArr)
    assignEmpID(npEmpArr)
    assignEmpAge(npEmpArr)
    assignEmpHeight(npEmpArr)
    t1=findAvgs(npEmpArr)
    t2=findavgsPy(npEmpArr)
    print("numpy/python :{}".format(t2/t1))+
    print("numEmp:{}".format(numEmp))
    print("")

"""
◦ id: Max ID value ranging from 1 to 232
◦ name: Max length of 64 characters (single byte ASCII chars)
◦ age: Ranging from 20 to 60
◦ height: Ranging from 150 to 180 – in centimeter units

"""