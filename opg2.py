# Tar inn input fra brukeren.
navn = str(input("Navn: "))
alder = int(input("Alder: "))


class person():
    # Oppretter en klasse som tar navn og alder.
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder

    def ermyndig(cls):  # Sjekker alder og om personen kan kjøre eller ikke.
        if cls.alder >= 18:
            return cls.navn + ", du er gammel nok til å kjøre."
        else:
            return cls.navn + ", du er dessverre for ung til å kjøre."


nyperson = person(navn, alder)  # lager ny person med input fra tidligere

print(nyperson.ermyndig())
