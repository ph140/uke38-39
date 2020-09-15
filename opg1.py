import math

radius = float(input("Radius: "))


def omkrets(r):
    omkrets = 2*math.pi*r  # beregner omkretsen
    omkrets = round(omkrets, 2)  # avrunder til to desimaler
    return omkrets


def areal(r):
    areal = math.pi * r**2  # beregner arealet
    areal = round(areal, 2)  # avrunder til 2 desimaler
    return areal


def volum(r):
    volum = (4*math.pi*r**3)/3  # beregner volumet
    volum = round(volum, 2)  # avrunder til to desimaler
    return volum


def skrivut(radius):
    # skriver ut verdien av alle funksjonene
    print(omkrets(radius))
    print(areal(radius))
    print(volum(radius))


skrivut(radius)
