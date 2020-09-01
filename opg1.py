import math

radius = float(input("Radius: "))


def omkrets(r):
    o = 2*math.pi*r  # beregner omkretsen
    o = round(o, 2)  # avrunder til to desimaler
    return o


def areal(r):
    a = math.pi * r**2  # beregner arealeet
    a = round(a, 2)  # avrunder til 2 desimal
    return a


def volum(r):
    v = (4*math.pi*r**3)/3  # beregner volumet
    v = round(v, 2)  # avrunder til to desimaler
    return v


def skrivut(radius):
    # skriver ut verdien av alle funksjonene
    print(omkrets(radius))
    print(areal(radius))
    print(volum(radius))


skrivut(radius)
