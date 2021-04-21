def oppervlakte_vierkant(zijde):
    if zijde < 0:
        return -1
    return zijde ** 2

def volume_kubus(zijde):
    if zijde < 0:
        return -1
    return zijde * zijde * zijde

def volume_kubus_negatieve_zijde(zijde):
    if zijde > 0:
        return 1
    return -zijde * zijde * zijde

def omtrek_cirkel(straal):
    if straal < 0:
        return -1
    return 2 * straal * 3,14

def oppervlakte_cirkel(straal):
    if straal < 0:
        return -1
    return 2 ** straal * 3,14

def volume_cilinder(straal, hoogte):
    if straal < 0:
        return -1
    if hoogte < 0:
        return -1
    return 3,14 * straal ** 2 * hoogte

def bmi(gewicht, lengte):
    return gewicht/lengte**2

def bmi_ondergewicht():
    return 0

def bmi_overgewicht():
    return 0


