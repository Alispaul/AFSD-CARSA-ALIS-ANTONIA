meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

#print(studenti[0] + " a comandat " + comenzi[0])

for i, j in zip(studenti, comenzi):
    print(i + " a comandat " + j)

print(studenti)
print(tavi)
print(comenzi)
for i in range(len(studenti)):
    studenti.pop(0)
    print(studenti)
    tavi.pop()
    print(tavi)
    istoric_comenzi.append(comenzi[0])
    comenzi.pop(0)
    print(comenzi)

print(f"S-au comandat {istoric_comenzi.count("guias")} guias, {istoric_comenzi.count("ceafa")} ceafa, {istoric_comenzi.count("papanasi")} papanasi")
print("Mai sunt " + str(len(tavi)) + " tavi.")
print(meniu.count("ceafa"))
print(meniu.count("ceafa") - istoric_comenzi.count("ceafa"))
print(meniu.count("papanasi") - istoric_comenzi.count("papanasi"))
if (meniu.count("ceafa") - istoric_comenzi.count("ceafa")) > 0 :
    print("Mai este ceafa: ", True)
else:
    print("Mai este ceafa: ", False)

if (meniu.count("papanasi") - istoric_comenzi.count("papanasi")) > 0 :
    print("Mai sunt papanasi: ", True)
else:
    print("Mai sunt papanasi: ", False)

if meniu.count("guias") - istoric_comenzi.count("guias") > 0 :
    print("Mai este guias: ", True)
else:
    print("Mai este guias: ", False)

incasari_papanasi = (istoric_comenzi.count("papanasi") * preturi[0][1])
incasari_ceafa = (istoric_comenzi.count("ceafa") * preturi[1][1])
incasari_guias = (istoric_comenzi.count("guias") * preturi[2][1])

print(f"Cantina a incasat: {incasari_papanasi + incasari_ceafa + incasari_guias} lei.")

filtrare = list(filter(lambda preturi: preturi[1] <= 7, preturi))
print(f"Produse care costă cel mult 7 lei: {filtrare}")
