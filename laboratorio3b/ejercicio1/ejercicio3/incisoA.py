import math
import matplotlib.pyplot as plt
import numpy as np

t=np.linspace(0,2*3.1416,100)
x=np.cos**3(t)
plt.plot(t,x,linewidth=3,color='black')
y=np.sin**3(t)
plt.plot(t,y,linewidth=3,color='blue')
plt.legend('XY')
plt.grid(True)
plt.title('funciones')
plt.xlabel('x')
plt.ylabel('x(t),y(t)')
plt.savefig('gr3a.png')
plt.show()
