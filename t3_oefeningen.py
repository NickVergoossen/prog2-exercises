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

def omtrek_cirkel(straal):
    if straal <= 0:
        return -1
    resultaat = 2 * straal * 3.14
    return resultaat


def oppervlakte_cirkel(straal):
    if straal <= 0:
        return -1
    resultaat = 2 ** straal * 3.14
    return resultaat

def volume_cilinder(straal, hoogte):
    resultaat = 3.14 * straal ** 2 * hoogte
    if straal <= 0:
        return -1
    elif hoogte <= 0:
        return -1
    else:
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






