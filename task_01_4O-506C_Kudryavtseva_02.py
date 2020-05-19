import numpy as np
import matplotlib.pyplot as plt
import os

try: os.mkdir('results')
except OSError: pass
x = np.linspace(-5,5,1000)
y = -20 * np.exp(-0.2 * np.sqrt(0.5 * x**2)) - np.exp(0.5 *
                (np.cos(2 * np.pi * x) + 1)) + np.e + 20

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()
    
with open('results/task_01_4O-506C_Kudryavtseva_02.txt', 'w') as file:
    file.write('x\ty(x)\n')
    for i in range(0,1000):
        file.write(str(x[i])+'\t'+str(y[i])+'\n')          
        
    
