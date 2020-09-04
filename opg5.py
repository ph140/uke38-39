tall = int(input("Tall: "))  # Tar inn input

if tall == 2:
    print("Primtall")


for i in range(2, tall):
    # Itererer gjennom alle tallene fra 2 til "tall"
    # og sjekker om "tall" er delelig på noen av de.
    if tall % i == 0:
        print("Ikke primtall")
        break
    elif tall == i+1:
        print("Primtall")
        break
