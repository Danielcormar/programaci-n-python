import math
x=input("ingrese la primera coordenada del primer lugar ")
x1=x*0.0174533
y=input("ingrese la segunda coordenada del primer lugar ")
y1=y*0.0174533
w=input("ingrese la primera coordenada del segundo lugar ")
w1=w*0.0174533
z=input("ingrese la segunda coordenada del segundo lugar ")
z1=z*0.0174533

distancia=6371.01*math.acos(math.sin(x1)*math.sin(w1)+math.cos(x1)*math.cos(w1)*math.cos(y1-z1))
print distancia, "kilometros"
