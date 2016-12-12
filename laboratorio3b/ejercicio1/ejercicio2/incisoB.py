import matplotlib.pyplot as plt
import numpy as np
import math
#primer ejercicio
x=np.linspace(0,2,100)
f=x*math.e**(-3*x)
plt.plot(x,f,linewidth=3,color='black')
#segundo ejercico
g=(math.e**(-3*x))*(1-3*x)
plt.plot(x,g,linewidth=3,color='red')
plt.legend('fg')
plt.grid(True)
plt.title('Funciones Exponenciales')
plt.xlabel('x')
plt.ylabel('f(x),g(x)')
plt.savefig('grafica2B.png')
plt.show()
