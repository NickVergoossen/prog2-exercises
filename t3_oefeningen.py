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

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_oneven(number):
    if number % 1 == 0:
        return True
    else:
        return False

def is_palindroom():
    return 0

def pythagoras():
    return 0

def stats(punten):
    gemiddelde = sum(punten) / len(punten)
    maximum = max(punten)
    minimum = min(punten)
    nr = len(punten)
    return gemiddelde, maximum, minimum, nr

def volume_bol(straal):
    resultaat = 4/3 * 3.14 * straal**3
    if straal < 0:
        return -1
    else:
        return resultaat

def volume_donut():
    return 0






