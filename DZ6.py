def obrnuto(string):
    if len(string) == 0:
        return string
    else:
        return obrnuto(string[1:]) + string[0]


input = input("Unesite string: ")

print(obrnuto(input))
