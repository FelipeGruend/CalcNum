from __future__ import division
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt

xi = np.array([1872,1890,1900,1920,1940,1950,1960,1970,1980,1991,1996])
yi = np.array([9.9,14.3,17.4,30.6,41.2,51.9,70.2,93.1,119.0,146.2,157.1])  
V = np.array([xi**2,xi**1,xi**0]).transpose()  
a = ((np.linalg.inv((V.transpose()).dot(V))).dot(V.transpose())).dot(yi)


xx = np.linspace(-0.25,1.25)  
plt.plot(xi,yi,'ro',xx,np.polyval(a,xx),'b-')  
plt.grid();plt.show()
