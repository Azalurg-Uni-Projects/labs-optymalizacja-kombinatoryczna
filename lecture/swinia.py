pole = 20
time = 1800
timeP = 3
j = {"t": 20, "a": 40}
z = {"t": 100, "a": 200}
zp = 10
t = {"z": 6, "j": 5, "t": 10}
tp = 250

for x in range(pole+1):
    poleZiemniaka = x
    poleJeczmienia = pole - x

    iloscZiemniaka = poleZiemniaka * z["a"]
    iloscJeczmienia = poleJeczmienia * j["a"]
    iloscTucznika = 0
    while iloscJeczmienia > 0 and iloscZiemniaka > 0:
        iloscZiemniaka -= t["z"]
        iloscJeczmienia -= t["j"]
        iloscTucznika += 1

    czas = poleJeczmienia * j["t"] + poleZiemniaka * z["t"] + iloscTucznika * t["t"]
    kasa = iloscZiemniaka * zp + iloscTucznika * tp
    if czas > time:
        kasa -= (czas - time) * timeP
    print("Pole ziemniaka: " + str(poleZiemniaka) + " Pole jeczmienia: " + str(poleJeczmienia) + " Czas: " + str(czas) + " Kasa: " + str(kasa))
