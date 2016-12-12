import mathplotlib.pyplot as plt
import numpy as np
x=np.linspace(-6,2,1000)
y=5-(4*x)-x**2
plt.plot(x,y,linewidth=3,color='blue')
plt.legend()
plt.title('$f(x)=5-4x-x^2$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.savefig('graficaA.png')
plt.show()
