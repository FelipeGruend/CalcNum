import numpy as np
import CurveFit as cf
import matplotlib.pyplot as plt

# a) pega os pontos
xi = np.array([1872, 1890, 1900, 1920, 1940, 1950, 1960, 1970, 1980, 1991, 1996])

yi = np.array([9.9, 14.3, 17.4, 30.6, 41.2, 51.9, 70.2, 93.1, 119.0, 146.2, 157.1])

cf.fitpolinomial(xi, yi, 2)

print ('ola')
