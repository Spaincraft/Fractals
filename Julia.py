import matplotlib.pyplot as plt #Import Matplotlib.pyplot
import numpy as np #Import Numpy

bins=120 #Number of iterations

#Example of know JULIA conjunts
c1 =  0 #First complex number
c2 = -0.39+0.6*1j #Second complex number
c3 =  0.0 +0.8*1j #Third complex number
c4 =  0.19 +0.4*1j #Fourth complex number

x = np.linspace(-2,2,bins)  #Linear space


def JULIA(x,c,ite):  #x:linear space ,c:complex number,ite =Number of iterations
    n = (len(x))  
    out = np.zeros((n,n)) #Array to save the calculateD data
    for i in range(n):
        for j in range(n):
            m = 0   #Counter (Initial value)
            z = complex(x[i],x[j]) #Initial value of z
            for k in range(ite):
                z = z*z + c  #Iteration of z
                m += 1  #Counter 
                if (abs(z)>4): #Condition to ensure convergence.
                    break
            out[i,j] = m  #Final data of the iterations
    return (out)


#Example
b1 = JULIA(x,c1,bins)
b2 = JULIA(x,c2,bins)
b3 = JULIA(x,c3,bins)
b4 = JULIA(x,c4,bins)

#Plot of the Example
fig,(ax1,ax2,ax3,ax4) =plt.subplots(1,4,figsize=(10,10),sharey=(True))
ax1.imshow(b1,cmap="jet")
ax2.imshow(b2,cmap="jet")
ax3.imshow(b3,cmap="jet")
ax4.imshow(b4,cmap="jet")

    


