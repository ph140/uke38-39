# Tar inn tre tall fra brukeren
a = abs(int(input("Tall1: ")))
b = abs(float(input("Tall2: ")))
c = abs(float(input("Tall3: ")))


def triple(a, b, c):
    # Endrer variablene til kvadratet av seg selv
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
