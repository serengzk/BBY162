sorular = [\
    'Fatih Sultan Mehmet’in babası kimdir?',\
    'Magna Carta hangi ülkenin kralıyla yapılmış bir sözleşmedir?',\
    'Hangisi tarihteki Türk devletlerinden biri değildir?',\
    'Kıbrıs Barış harekatı hangi tarihte gerçekleşmiştir?',\
    'Hangi ülke Asya kıtasındadır?'
]
cevaplar = ['A','B','A','C','C']
cevapA = [\
    'II. Murat',\
    'ispanya',\
    'Emevi Devleti',\
    '1970',\
    'Madagaskar'
    ]
cevapB = [\
    'Yıldırım Beyazıt',\
    'İngiltere',\
    'Hun İmparatorluğu',\
    '1972',\
    'Peru',
]
cevapC = [\
    'I. Mehmet',\
    'Fransa',\
    'Avar Kağanlığı',\
    '1974',\
    'Singapur'
]
puan = 0
for i in range(len(sorular)):
    print("Soru " + str(i + 1) + ":" + sorular[i])
    print("A) " + cevapA[i] )
    print("B) " + cevapB[i] )
    print("C) " + cevapC[i] )
    cevap = input("cevabınızı giriniz: ")
    if cevaplar[i] == cevap.upper():
        puan +=1
print("TEBRİKLER")
print("ALDIĞINIZ NOT: " +str(int((puan/len(sorular))*100)))
