
metin = "Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini,bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
print(metin[:19])

liste = (["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"])
for i in liste:
    print(i)

sozluk = {"Elma" : "Ağaçta yetişen bir tür meyve" , "Salatalık" : "Fidan üzerinde büyüyen bir tür sebze" }
cevap = input("kelime:")
cevap = cevap.capitalize()
if cevap in sozluk:
    print(sozluk[cevap])
else:
    print("kelime yok")


