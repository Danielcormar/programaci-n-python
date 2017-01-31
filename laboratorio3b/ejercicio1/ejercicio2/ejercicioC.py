
import math
import matplotlib.pyplot as plt
import numpy as np

t=np.linspace(0,4*m3.1416,100)
f=np.sin(3*t)*np.cos(2*t)
plt.plot(t,f,linewidth=2,color='black')

g=(1/2*np.cos(t))+(5/2*np.cos(5*t))
plt.plot(t,g,linewidth=2,color='blue')
plt.legend('fg')
plt.grid(True)
plt.title('funciones')
plt.xlabel('x')
plt.ylabel('f(t),g(t)')
plt.savefig('gr2c.png')
plt.show()
