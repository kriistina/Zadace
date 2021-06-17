def parni(n):
    a = 2

    while a < n:
        yield a
        a += 2

def neparni(n):
    a = 1

    while a < n:
        yield a
        a += 2


broj = int(input("Unesite parametar: "))

print("Parni:")
for i in parni(broj):
    print(i)
    
print(30*"*")

print("Neparni:")
for i in neparni(broj):
    print(i)
