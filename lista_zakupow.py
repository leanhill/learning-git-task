lista_zakupów={
    "piekarnia":["chleb", "pączek","bułki"],
    "warzywniak":["marchew", "seler","rukola"]
}
for i, a in lista_zakupów.items():
    for b in range (len(a)):
        a[b] = a[b].capitalize()
    i = i.capitalize()
    print("Idę do %s"%i,"i kupuję tu następujące rzeczy:%s"%a)
sum = sum([len(a) for i, a in lista_zakupów.items()])
print("W sumie kupuję %s"%sum, "produktów")
input("Oceń program w skali 1-10")
# Zakończono projekt