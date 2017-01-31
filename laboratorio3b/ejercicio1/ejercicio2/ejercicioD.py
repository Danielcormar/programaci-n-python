import math
import matplotlib.pyplot as plt
import numpy as np

t=np.linspace(0,2*3.1416,100)
x=(1+2*np.sin(t))*np.cos(t)
plt.plot(t,x,linewidth=3,color='black')

y=(1+2*np.sin(t))*np.sin(t)
plt.plot(t,y,linewidth=2,color='white')
plt.legend('XY')
plt.grid(True)
plt.title('funciones')
plt.xlabel('x')
plt.ylabel('X(t),Y(T)')
plt.savefig('gr2d.png')
plt.show()
