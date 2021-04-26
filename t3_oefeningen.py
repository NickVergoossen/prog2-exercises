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
    resultaat = 2 * straal * 3.14
    return resultaat

def oppervlakte_cirkel(straal):
    if straal < 0:
        return -1
    return 2 * straal * 3.14

def volume_cilinder(straal, hoogte):
    return 0

def bmi(gewicht, lengte):
    if gewicht <= 0:
        return -1
    elif lengte <= 0:
        return -1
    else:
        resultaat = gewicht /(lengte ** 2)
        return resultaat




