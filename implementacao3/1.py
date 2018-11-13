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

    m=np.shape(A)[1]
    if n != 2:
        raise NameError ('Número de equações diferente de dois')

    axes = plt.axes()
    x1Dots = [x0[0,0]]
    x2Dots = [x0[1,0]]
    x1Gap = [0.0, 0.0]
    x2Gap = [0.0, 0.0]
    plt.xlabel('x1')
    plt.ylabel('x2')
    
    #iteracoes  
    while (it < N):  
        it = it+1  
        #iteracao de Jacobi  
        for i in np.arange(n):  
            x[i] = b[i]  
            for j in np.concatenate((np.arange(0,i),np.arange(i+1,n))):  
                x[i] -= A[i,j]*x0[j]  
            x[i] /= A[i,i]

        #inserindo resultados para o grafico        
        x1Dots.append(x[0])
        x2Dots.append(x[1])

        #checando se os limites devem ser extendidos para x1
        if x[0] < x1Gap[0]:
            x1Gap[0] = x[0]
        elif x[0] > x1Gap[1]:
            x1Gap[1] = x[0]

        #checando se os limites devem ser extendidos para x2
        if x[1] < x2Gap[0]:
            x2Gap[0] = x[1]
        elif x[1] > x2Gap[1]:
            x2Gap[1] = x[1]

        
        #tolerancia  
        if (np.linalg.norm(x-x0,np.inf) < tol):
            #seta os dados do gráfico e retorna valores 
            for i in range(0, len(x1Dots) - 1):
                plt.arrow(x1Dots[i], x2Dots[i],     \
                         x1Dots[i+1] - x1Dots[i],   \
                         x2Dots[i+1] - x2Dots[i],   \
                         head_width=0, head_length=0, width=0.000001,\
                         fc='k', ec='k', length_includes_head = True)

            plt.xlim(x1Gap[0] - 0.5, x1Gap[1] + 0.5)     # seta os limites de x
            plt.ylim(x2Gap[0] - 0.5, x2Gap[1] + 0.5)     # seta os limites de y

            gx = np.arange(-15, 15, 0.001)
            plt.plot(gx, (b[0,0] - (A[0,0]*gx)) / A[0,1], gx, (b[1,0] - (A[1,0]*gx)) / A[1,1], x1Dots, x2Dots, 'bo')
            plt.show() 
            return x
        
        #prepara nova iteracao  
        x0 = np.copy(x)
        
    raise NameError('num. max. de iteracoes excedido.')


# Matriz a
A = np.array( [[1, 1],
               [1,-3]],
              dtype='double' )

# Matriz y
b = np.array( [[3],[-3]], dtype='double' )

# Tolerancia
tol = 0.001

# Iteracoes
N = 100

# aproximação inicial 0
x0 = np.array( [[0.0],[0.0]], dtype='double')

jacobi(A, b, x0, tol, N)
