import matplotlib.pyplot as plt
import numpy as np

bins=100
c1 = 0.39+0.6*1j
x1 = np.linspace(-2,2,bins)


c2= 0.21
x2 = np.linspace(-2,2,bins)

def MADEL(x,c,ite):  
    n = (len(x))
    out = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            m = 0
            c = complex(x[i],x[j])
            z = 0
            for k in range(ite):
                z = z*z + c
                m += 1
                if (abs(z)>4):
                    break
            out[i,j] = m
    return (out)


def MADELEXP(x,c,ite):  
    n = (len(x))
    out = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            m = 0
            c = complex(x[i],x[j])
            z = 0
            for k in range(ite):
                z =(np.exp(z))*(z**3) + c
                m += 1
                if (abs(z)>4):
                    break
            out[i,j] = m
    return (out)


plt.figure(1)
b1 = JULIA(x1,c1,bins)
plt.imshow(b1,cmap="jet")


plt.figure(2)
b2 = JULIAEXP(x2,c2,bins)
plt.imshow(b2,cmap="jet")

    



