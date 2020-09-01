a = abs(int(input("Tall1: ")))
b = abs(int(input("Tall2: ")))
c = abs(int(input("Tall3: ")))


def triple(a, b, c):
    a = a**2
    b = b**2
    c = c**2

    if a + b == c:
        return True
    elif a + c == b:
        return True
    elif b + c == a:
        return True
    else:
        return False


if triple(a, b, c) == True:
    print("Det er riktig")
else:
    print("Det stemmer ikke")
