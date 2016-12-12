#daniel Corona Marin
#ejercicio3
def ord(a,b,c):
    if a>b:
        if b>c:
            print c, b, a
        else:
            if a>b:
                print b, c, a
            else:
                print b, a, a
    else:
        if a>c:
            print c, a, b
        else:
            if b>c:
                print a, c, b
            else:
                print a,b,c
