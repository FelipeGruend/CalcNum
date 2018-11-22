import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg

# Ajuste polinomial
def fitpolynomial(xi, yi, degree):
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

  # Cria uma lista e para cada valor em xi calcula o polinomio encontrado e adiciona a lista
  result = []
  for value in xi:
      result.append(np.polyval(a,value))

  return result, a


def fitexponencial(xi, yi):
  # Testa se existe quantidades iguais de valores x e y para os pontos
  if len(xi) != len(yi):
      raise NameError('Sizes of x and y coordinates does not fit')

  # cria a matriz com os valores e faz a transposta e cria a matris dos ln
  V = np.array([np.ones(len(xi)),xi]).transpose()  
  a = np.linalg.lstsq(V,np.log(yi))[0]  
  A = np.exp(a[0])  
  b = a[1]

  # Cria uma lista e para cada valor em xi calcula o polinomio encontrado e adiciona a lista usand
  # Ae^(b*x)
  result = []
  for value in xi:
      result.append(A * np.exp(b*value))

  return result, A, b


def variancy(x, fx):
  if len(x) != len(fx):
      raise NameError('Sizes of x and x1 does not fit')

  v = 0
  # Calcula o erro medio quadratico para cada ponto
  for i in range(len(x)):
      v = v + ((fx[i] - x[i])**2)

  return v

def predictpolynomial(x, polynomial):
  y = []
  y.append(np.polyval(polynomial, x))

  return y
  
def predictexponencial(x, A, b):
  y = []
  y.append(A * np.exp(b*x))

  return y
