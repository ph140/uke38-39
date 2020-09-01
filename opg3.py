# Tar inn tre tall fra brukeren
a = abs(int(input("Tall1: ")))
b = abs(int(input("Tall2: ")))
c = abs(int(input("Tall3: ")))


def triple(a, b, c):
    # Endrer variablene til å være opphøyd i andre
    a = a**2
    b = b**2
    c = c**2

    # Sjekker om det er pytagorisk sammenheng mellom de, og returner True/False
    if a + b == c:
        return True
    elif a + c == b:
        return True
    elif b + c == a:
        return True
    else:
        return False


# Skriver ut resultatet basert på svaret fra funksjonen
if triple(a, b, c) == True:
    print("Det er riktig")
else:
    print("Det stemmer ikke")
