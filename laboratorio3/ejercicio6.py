#Daniel Corona Marin
#ejercicio 6
x=input("ingrese la edad de su perro ")
if x<0:
    print "la edad es negativa, no existe"
else:
    if x<=2:
        e=x*10.5
        print e
    else:
        e=((x-2)*4)+21
        print e
