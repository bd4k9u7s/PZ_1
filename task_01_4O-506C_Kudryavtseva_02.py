import numpy as np
import matplotlib.pyplot as plt
import os

if not os.path.exists('results'):
    os.mkdir('results')
    
x = np.linspace(-5,5,1000)
y = -20 * np.exp(-0.2 * np.sqrt(0.5 * x**2)) - np.exp(0.5 *
                (np.cos(2 * np.pi * x) + 1)) + np.e + 20

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()

p = os.path.join(os.getcwd(),'results','task_01_4O-506C_Kudryavtseva_02.txt')
    
with open(p, 'w') as file:
    file.write('x{0:4}y(x)\n'.format(' '))
    for i in range(0,1000):
        file.write('{0}{1:4}{2}\n'.format(str(x[i]),' ',str(y[i])))
       
        
    
