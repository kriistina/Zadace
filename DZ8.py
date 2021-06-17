ime = input("Unesite ime: ")

lambda ime: "Dobrodosao " + ime

def pozdrav(ime):
    return "Pozdrav " + ime

def treca(pozdrav):
    return pozdrav(ime)

print(treca(pozdrav))
