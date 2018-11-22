import numpy as np
import CurveFit as cf
import matplotlib.pyplot as plt

# QUESTAO 1

# a) plota a dispersao dos dados-------------------------------------------------
xi = np.array([1872, 1890, 1900, 1920, 1940, 1950, 1960, 1970, 1980, 1991, 1996])

yi = np.array([9.9, 14.3, 17.4, 30.6, 41.2, 51.9, 70.2, 93.1, 119.0, 146.2, 157.1])

plt.plot(xi, yi, 'ro')
# ---------------------------------------------------------------------------------


# b) calcula a funcao quadrática e os resultados------------------------------------
resultsp, polynomial = cf.fitpolynomial(xi, yi, 2)

# Cria a linha da funcao e plota
xx = np.linspace(xi[0], xi[-1])
plt.plot(xx, np.polyval(polynomial,xx),'b-')
# -----------------------------------------------------------------------------------


# c) calcula a funcao exponencial(A e b) e os resultados ---------- -----------------
resultse, A, b = cf.fitexponencial(xi, yi)

# Cria a linha da funcao e plota usando a Ae^(b*x)
xx = np.linspace(xi[0], xi[-1])  
plt.plot(xx, A * np.exp(b*xx),'g-')

plt.grid();plt.show()
#-------------------------------------------------------------------------------------

# d) decide qual curva possui o melhor ajuste e plotaem vermelho -----------------------

v1 = cf.variancy(yi, resultsp)
v2 = cf.variancy(yi, resultse)

if (v1 <= v2):
    plt.plot(xx, A * np.exp(b*xx),'r-')
    plt.plot(xx, np.polyval(polynomial,xx),'b-')
else:
    plt.plot(xx, A * np.exp(b*xx),'b-')
    plt.plot(xx, np.polyval(polynomial,xx),'r-')

plt.plot(xi, yi, 'ro')

plt.grid();plt.show()

#--------------------------------------------------------------------------------------

x = np.array([2000, 2005, 2014])

polypredictions = cf.predictpolynomial(x, polynomial)

exponencialpredictions = cf.predictexponencial(x, A, b)

print (polypredictions)
print (exponencialpredictions)



# QUESTAO 2

# a) plota a dispersao dos dados-------------------------------------------------
xi = np.array([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

yi = np.array([0.029, 0.052, 0.079, 0.125, 0.181, 0.261, 0.425, 0.738, 1.130, 1.882, 1.812])

plt.plot(xi, yi, 'ro')
# ---------------------------------------------------------------------------------


# b) calcula a funcao quadrática e os resultados------------------------------------

results = []
polynomials = []

for i in range (3):
    r, p = cf.fitpolynomial(xi, yi, i+2)
    results.append(r)
    polynomials.append(p)

#-------------------------------------------------------------------------------------

# c) decide qual curva possui o melhor ajuste e plota em vermelho -----------------------

v = []

for i in range (3):
    v.append(cf.variancy(yi, results[i]))

index_min = np.argmin(v)

xx = np.linspace(xi[0], xi[-1])
plt.plot(xx, np.polyval(polynomials[index_min],xx),'b-')

plt.plot(xi, yi, 'ro',)

plt.grid();plt.show()

#--------------------------------------------------------------------------------------

x = np.array([20])

polypredictions = cf.predictpolynomial(x, polynomials[index_min])

print (polypredictions)
