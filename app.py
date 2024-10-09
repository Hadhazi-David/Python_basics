import random
eszkozok = ["ko", "papir", "ollo"]
gepi_valasz = eszkozok[random.randint(0, 2)]
print("### Ko, Papir, Ollo ###")
# print(gepi_valasz)
bevitel = input("Valassz! ko/papir/ollo: ")
while not bevitel in eszkozok:
    print(">>> irjad normalisan <<<")
    bevitel = input("Valassz! ko/papir/ollo: ")

if bevitel == gepi_valasz:
    print("dontetlen!haha")
elif gepi_valasz == "ko":
    if bevitel == "papir":
        print("Grat, nyertel. Ez volt a gep valasza: ", gepi_valasz)
    else:
        print("SZAR VAGY, ez volt a gep valasza: ", gepi_valasz)
elif gepi_valasz == "papir":
    if bevitel == "ollo":
        print("Grat, nyertel. Ez volt a gep valasza: ", gepi_valasz)
    else:
        print("SZAR VAGY, ez volt a gep valasza: ", gepi_valasz)
elif gepi_valasz == "ollo":
    if bevitel == "ko":
        print("Grat, nyertel. Ez volt a gep valasza: ", gepi_valasz)
    else:
        print("SZAR VAGY, ez volt a gep valasza: ", gepi_valasz)
