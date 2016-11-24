# -*- coding: <encoding name> -*-
def viaje3(segs):
    dias=segs/86400
    hor=segs/36000
    minu=((segs-(hor*3600))/60)
    ss=segs-((hor*3600)+(minu*60))
    print dias
    print hor
    print minu
    print ss
