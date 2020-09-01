x = int(input("Tall: "))
original = x
minliste = []


while x > 1:
    x = int(x)
    for i in range(2, x+1):
        if x % i == 0:
            x = int(x/i)
            minliste.append(int(i))
            break
        elif x/i == 1:
            break


print(minliste)

if minliste[0] == original:
    print("Primatall")
