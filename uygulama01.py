sorular = [ 'Seren 21 yaşındadır [D,Y]',\
            'Seren başak burcudur [D,Y]',\
            'Serenin umut adında bir kardeşi vardır [D,Y]',\
            'Seren ağustosta doğmuştur [D,Y]',\
            'Seren kitap okumayı sevmez [D,Y]',\
            'Seren ile kardeşi arasında 2 yaş var']
cevaplar = ['D','Y','D','D','Y','D']
puan = 0
#soru 1
cevap = input((sorular[0]))
if cevaplar[0] == cevap.upper() :
    print("Tebrikler,DOĞRU")
    puan += 1
else:
    print("Cevabınız YANLIŞ")
    puan -= 1
#soru 2
cevap = input((sorular[1]))
if cevaplar[1] == cevap.upper() :
    print("Tebrikler,DOĞRU")
    puan += 1
else:
    print("Cevabınız YANLIŞ")
    puan -= 1
#soru 3
cevap = input((sorular[2]))
if cevaplar[2] == cevap.upper() :
    print("Tebrikler,DOĞRU")
    puan += 1
else:
    print("Cevabınız YANLIŞ")
    puan -= 1
#soru 4
cevap = input((sorular[3]))
if cevaplar[3] == cevap.upper() :
    print("Tebrikler,DOĞRU")
    puan += 1
else:
    print("Cevabınız YANLIŞ")
    puan -= 1
#soru 5
cevap = input((sorular[4]))
if cevaplar[4] == cevap.upper() :
    print("Tebrikler,DOĞRU")
    puan += 1
else:
    print("Cevabınız YANLIŞ")
    puan -= 1
#soru 6
    cevap = input((sorular[5]))
    if cevaplar[5] == cevap.upper():
        print("Tebrikler,DOĞRU")
        puan += 1
    else:
        print("Cevabınız YANLIŞ")
        puan -=1
#test sonu
    print("TEST BİTTİ,PUAN:" +str(puan*25))


