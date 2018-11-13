from __future__ import division  
import numpy as np  
from numpy import linalg
import matplotlib.pyplot as plt
 
def jacobi(A,b,x0,tol,N):  
    #preliminares  
    A = A.astype('double')  
    b = b.astype('double')  
    x0 = x0.astype('double')  
 
    n=np.shape(A)[0]  
    x = np.zeros(n)  
    it = 0  
    #iteracoes  
    while (it < N):  
        it = it+1  
        #iteracao de Jacobi  
        for i in np.arange(n):  
            x[i] = b[i]  
            for j in np.concatenate((np.arange(0,i),np.arange(i+1,n))):  
                x[i] -= A[i,j]*x0[j]  
            x[i] /= A[i,i]  
        #tolerancia  
        if (np.linalg.norm(x-x0,np.inf) < tol):  
            return x  
        #prepara nova iteracao  
        x0 = np.copy(x)
        print(x0)
    raise NameError('num. max. de iteracoes excedido.')


A = np.array( [[1, 1],
               [1,-3]],
              dtype='double' )

b = np.array( [[3],[-3]], dtype='double' )

tol = 0.001
N = 100

x0 = np.array( [[0.0],[0.0]], dtype='double')

jacobi(A, b, x0, tol, N)
