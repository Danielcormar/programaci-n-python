import math
import matplotlib.pyplot as plt
import numpy as np

t=np.linspace(-2*3.1416,2*3.1416,100)
x=t+2*np.sin(2*t)
plt.plot(t,x,linewidth=3,color='black')
y=t+2*np.cos(5*t)
plt.plot(t,y,linewidth=3,color='blue')
plt.legend('XY')
plt.grid(True)
plt.title('funciones')
plt.xlabel('x')
plt.ylabel('xt),y(t)')
plt.savefig('gr3b.png')
plt.show()
