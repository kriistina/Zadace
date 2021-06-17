from csv import reader

with open('rezultati.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    rezultati = list(map(tuple, csv_reader))
    print(rezultati)

novi_rezultati = []

for ime, prezime, bodovi in rezultati:
    novi_rezultati.append((prezime, ime, bodovi))
novi_rezultati.sort()

brojOcjena = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0}

for prezime, ime, bodovi in novi_rezultati:
    if int(bodovi) < 50:
        brojOcjena['1'] += 1
    elif int(bodovi) < 65:
        brojOcjena['2'] += 1
    elif int(bodovi) < 80:
        brojOcjena['3'] += 1
    elif int(bodovi) < 90:
        brojOcjena['4'] += 1
    elif int(bodovi) < 100:
        brojOcjena['5'] += 1
