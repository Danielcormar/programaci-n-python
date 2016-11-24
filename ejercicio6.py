peso=input()
altura=input()
def mic(peso,altura):
  return peso/(altura*altura)
  if mic<16.00:
    print "delgadez"
  elif mic<16.99 and mic>16:
    print "delgadez moderda"
  elif mic>17.00 and mic<18.49:
    print "delgadez leve"
  elif mic>18.50 and mic<24.99:
    print "normal"
  elif mic<=25:
    print "sobrepeso"
  elif mic<=30:
    print "sobrepeso"
  elif mic<=40:
  print "obesidad morbida"
