import matplotlib.pyplot as plt
import numpy as np
import math as m
x=np.linspace(-1,5,100)
y=x*(m.e**(-2*c))
plt.plot(x,y,linewidth=3,color='black')
plt.legend()
plt.title('f(x)=xe^-2x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.savefig('graficaC.png')
plt.show()
