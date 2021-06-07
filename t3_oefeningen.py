from math import pi

def oppervlakte_vierkant(zijde):
    if zijde < 0:
        return -1
    return zijde ** 2

def volume_kubus(zijde):
    resultaat = zijde ** 3
    if resultaat < 0:
        resultaat = 0
        return resultaat
    else:
        return resultaat

def omtrek_cirkel(r):
    if r <= 0:
        return -1
    resultaat = 2 * r * pi
    return resultaat


def oppervlakte_cirkel(r):
    if r <= 0:
        return -1
    resultaat = (r **2) * pi
    return resultaat

def volume_cilinder(r, h):
    if r <= 0:
        return -1
    if h <= 0:
        return -1
    resultaat = oppervlakte_cirkel(r) * h
    return resultaat

def bmi(gewicht, lengte):
    if gewicht <= 0:
        return -1
    elif lengte <= 0:
        return -1
    else:
        resultaat = gewicht /(lengte ** 2)
        return resultaat






