import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg

# Ajuste polinomial
def fitpolinomial(xi, yi, degree):
  # Testa se existe quantidades iguais de valores x e y para os pontos
  if len(xi) != len(yi):
      raise NameError('Sizes of x and y coordinates does not fit')

  # Cria uma matriz tendo os valores de x elevados de 0 ate o grau desejado
  V = []
  for i in range (degree + 1):
      V.append(xi ** (degree - i))

  # Calcula a transposta da matris V e faz realiza as operações nas matrizes
  V = np.array(V).transpose()
  a = ((np.linalg.inv((V.transpose()).dot(V))).dot(V.transpose())).dot(yi)

# Cria a linha da funcao e plota
  xx = np.linspace(xi[0], xi[-1])
  plt.plot(xi,yi,'ro',xx,np.polyval(a,xx),'b-')  
  plt.grid();plt.show()

  # Cria uma lista e para cada valor em xi calcula o polinomio encontrado e adiciona a lista
  results = []
  for value in xi:
      results.append(np.polyval(a,value))

  return results


def fitexponencial(xi, yi):
  # Testa se existe quantidades iguais de valores x e y para os pontos
  if len(xi) != len(yi):
      raise NameError('Sizes of x and y coordinates does not fit')

  # cria a matriz com os valores e faz a transposta e cria a matris dos ln
  V = np.array([np.ones(len(xi)),xi]).transpose()  
  a = np.linalg.lstsq(V,np.log(yi))[0]  
  A = np.exp(a[0])  
  b = a[1]

  # Cria a linha da funcao e plota usando a Ae^(b*x)
  xx = np.linspace(xi[0], xi[-1])  
  plt.plot(xi,yi,'ro',xx, A * np.exp(b*xx),'g-')  
  plt.grid();plt.show()

  # Cria uma lista e para cada valor em xi calcula o polinomio encontrado e adiciona a lista usando
  # Ae^(b*x)
  results = []
  for value in xi:
      results.append(A * np.exp(b*value))

  return results

  
def variancy(x, x1):
  if len(x) != len(x1):
      raise NameError('Sizes of x and x1 does not fit')

  v = 0
  # Calcula o erro medio quadratico para cada ponto
  for i in range(len(x)):
      v = v + ((x1[i] - x[i])**2)

  return v
