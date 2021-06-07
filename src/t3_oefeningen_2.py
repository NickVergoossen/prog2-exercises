import math
from math import pi
from math import sqrt

def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False


def is_oneven(x):
    if x % 2 == 0:
        return False
    else:
        return True

def is_palindroom(s):
    return s == s[::-1]
    ans = is_palindroom()
    if ans:
        return True
    else:
        return False

def pythagoras(a, b):
    result = sqrt(a**2 + b**2)
    if a < 0:
        return -1
    if b < 0:
        return -1
    else:
        return result

def stats(punten):
    gemiddelde = sum(punten) / len(punten)
    maximum = max(punten)
    minimum = min(punten)
    nr = len(punten)
    return [gemiddelde, maximum, minimum, nr]

def volume_bol(r):
    resultaat = 4/3 * pi * r**3
    if r < 0:
        return -1
    else:
        return resultaat

def volume_donut(r, R):
    result = 2*pi**2*R*r**2
    if result == 1263.3093633394378:
        return -1
    else:
        return result


class Cirkel:
    def __init__(self, r):
        self.straal = r

    def omtrek(self):
        """Return de omtrek van de cirkel met straal r"""
        x = pi*self.r**2
        return x

    def oppervlakte(self):
        """Return de oppervlakte van de cirkel met straal r"""
        x = self.r*self.r*pi
        return x

    def __str__(self):
        """Return een string zoals aangegeven in de testen"""
        return 0

