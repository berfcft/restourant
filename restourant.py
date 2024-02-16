masalar = dict()
for a in range(20):
    masalar[a] = 0
def hesap_ekle():
        masano = int(input("Hesap Eklemek İstediğiniz Masayı Giriniz: "))
        bakiye = masalar[masano]
        eklenecek_ücret = float(input("Eklenecek Ücret : "))
        güncel_bakiye = bakiye + eklenecek_ücret
        masalar[masano] = güncel_bakiye
        print("Hesap başarıyla eklendi")
def hesap_ödeme():
    masano = int(input("Hesap Eklemek İstediğiniz Masayı Giriniz: "))
    bakiye = masalar[masano]
    print("Masa {}'in hesabı : {} Tl'dir.".format(masano,bakiye))
    masalar[masano] = 0
    print("Hesap Ödendi.")
def dosya_kontrol(dosya_adi):
    try:
        dosya = open(dosya_adi,"r",encoding="utf-8")
        veri = dosya.read()
        veri =veri.split("\n")
        veri.pop()
        dosya.close()
        for a in enumerate(veri):
            masalar[a[0]] = float(a[1])
    except FileNotFoundError:
        dosya = open(dosya_adi,"w",encoding="utf-8")
        dosya.close()
        print("Kayıt dosyası oluşturuldu.")
def dosya_güncelle(dosya_adi):
        dosya = open(dosya_adi,"w",encoding="utf-8")
        for a in range(20):
             bakiye = masalar[a]
             bakiye = str(bakiye)
             dosya.write(bakiye+"\n")
        dosya.close()
def ana_islemler():
    dosya_kontrol("bakiye.txt")
    while True:
        print("""
              
           Berfin ÇİFTÇİ Restourant Uygulaması
        1)Masaları Görüntüle
        2)Hesap Ekle
        3)Hesap Öde
        Q)Çıkış 
                                     
""")
        secim = input("Yapılacak işlemi giriniz : ")
        if secim =="1":
            for a in range(20):
                print("Masa {} için hesap : {}".format(a,masalar[a]))
        elif secim =="2":
            hesap_ekle()
        elif secim =="3":
            hesap_ödeme()
        elif secim =="Q" or secim =="q":
            print("Çıkış yapılıyor...")
            quit()
        else:
            print("Hatalı seçim yaptınız.")
        dosya_güncelle("bakiye.txt")
        input("Ana menüye dönmek için enter'a basınız.")    
ana_islemler()