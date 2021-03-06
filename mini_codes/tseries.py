# -*- coding: utf-8 -*-
"""
Spyder Editor

"""


#%%


print ("shit, man")


import sympy as sy
import numpy as np
from sympy.functions import sin,cos
import matplotlib.pyplot as plt

plt.style.use("ggplot")

# Define x as a axis (variable), and the function to approximate
x = sy.Symbol('x')
f = sin(x)

# Factorial function
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)

# Taylor approximation at 'a' of the function, and series with 'n' terms
def taylor(function,a,n):
    p = 0
    for i in range(0, n+1):
        p = p + (function.diff(x,i).subs(x,a))/(factorial(i))*(x-a)**i
    return p


#%%

# Plot results
def plot():
    x_lims = [-5,5]
    x1 = np.linspace(x_lims[0],x_lims[1],800)
    y1 = []
    # Approximate up until 10 starting from 1 and using steps of 2
    for j in range(1,10):
        func = taylor(f,0,j)
        print('Taylor expansion at n='+str(j),func)
        for k in x1:
            y1.append(func.subs(x,k))
        plt.plot(x1,y1,label='order '+str(j))
        y1 = []
        
        
    # Plot the function to approximate (sine, in this case)
    plt.plot(x1,np.sin(x1),label='sin of x')
    plt.xlim(x_lims)
    plt.ylim([-5,5])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.title('Taylor series approximation')
    plt.show()

plot()