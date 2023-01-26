# Here's a python version of
# https://www.mathworks.com/matlabcentral/fileexchange/71696-good-point-array-or-good-point-set-or-good 
import numpy as np
import math

def Goodnodes(M,N):
    tem1=np.dot(np.arange(1,M+1).reshape(M,1),np.ones(N).reshape(1,N))
    Ind=np.arange(1,N+1)
    pr=-1
    flag=1
    for i in range(2*N+3,100*N):
        if(flag):
            for j in range(2, i):
                if i % j == 0:
                    flag=0
                    break
            if(flag):
                pr=i
                break
            flag=1
    tem2=2*math.pi*Ind/pr;           
    tem2=2*np.cos(tem2).reshape(1,N)
    tem2=np.dot(np.ones(M).reshape(M,1),tem2)
    result=tem1*tem2
    result=result%1
    # print(result)
    return result


print(Goodnodes(100,2))