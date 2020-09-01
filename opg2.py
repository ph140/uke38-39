navn = str(input("Navn: "))
alder = int(input("Alder: "))


class person():

    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder

    def ermyndig(cls):  # Sjekker aldere og sier om person kan kjøre eller ikke
        if cls.alder >= 18:
            return cls.navn + ", du er gammel nok til å kjøre."
        else:
            return cls.navn + ", du er dessverre for ung til å kjøre."


nyperson = person(navn, alder)

print(nyperson.ermyndig())
