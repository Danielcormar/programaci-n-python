import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-1,5,100)
y=2*(x**2)-(8*x)-11
plt.plot(x,y,linewidth=3,color='green')
plt.legend()
plt.title('g(x)=2x^2-8x-11')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid(True)
plt.savefig('graficaB.png')
plt.show()
