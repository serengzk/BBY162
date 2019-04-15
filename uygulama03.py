__author__="Seren"
print("Adam Asmaca Oyunu")
from random import choice
while True:
    kelime = choice (["köpek", "kedi", "fare", "sincap", "kurbağa", "kanguru", "balık", "tilki"])
    kelime = kelime.upper()
    harfsayisi = len(kelime)
    print("Kelimemiz {} harflidir.\n".format(harfsayisi))
    tahminler = []
    hata = []
    KalanCan = 4
    while KalanCan > 0:
        bos = ""
        for girilenharf in kelime:
            if girilenharf in tahminler:
                bos = bos + girilenharf
            else:
                bos = bos + " _ "
        if bos == kelime:
            print("Tebrikler!")
            break
        print("Kelimeyi Tahmin Ediniz", bos)
        print(KalanCan, "Canınız Kaldı")
        Tahmin = input("Bir Harf Giriniz :")
        Tahmin = Tahmin.upper()
        if Tahmin == kelime:
            print("\n\n Tebrikler\n\n")
            break
        elif Tahmin in kelime:
            rpt = kelime.count(Tahmin)
            print("Dogru.{0} Harfi Kelimemiz İçerisinde {1} Kere Geçiyor".format(Tahmin, rpt))
            tahminler.append(Tahmin)
        else:
            print("Yanlış.")
            hata.append(Tahmin)
            KalanCan = KalanCan - 1
    if KalanCan == 0:
        print("\n\nHiç Hakkınız Kalmadı.")
        print("Kelimemiz {}\n\n".format(kelime))
    print("Oyundan Çıkmak İstiyorsanız\n'X' Tuşuna Basınız\nDevam Etmek İçin -> ENTER. ")
    devam = input(":")
    devam = devam.upper()
    if devam == "X":
        break
    else:
        continue