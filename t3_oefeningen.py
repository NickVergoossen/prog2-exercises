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




