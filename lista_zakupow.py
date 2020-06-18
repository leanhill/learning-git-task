lista_zakupów={
    "piekarnia":["chleb", "pączek","bułki"],
    "warzywniak":["marchew", "seler","rukola"]
}
for i, a in lista_zakupów.items():
    for b in range (len(a)):
        a[b] = a[b].capitalize()
    i = i.capitalize()
    print("Idę do %s"%i,"i kupuję tu następujące rzeczy:%s"%a)


