import re
string = input("Unesite string: ")
regex = "k.*([0-5]|[0-5]).*đ"
result = re.findall(regex, string)
if result:
    print("Podudaranje")
else:
    print("Nema podudaranja")
