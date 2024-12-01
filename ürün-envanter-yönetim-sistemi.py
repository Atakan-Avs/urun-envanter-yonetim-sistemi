urunler={}
def urun_ekle():
    urun_adi=input("lütfen eklemek istediğiniz ürün ismini giriniz:")
    urun_fiyatı=input("lütfen eklediğiniz ürünün fiyatını giriniz:")
    urun_stok=int(input("lütfen ürünün stok adedini giriniz:"))
    urun_kategori=input("ürün kategorisini giriniz:")

    urunler[urun_adi]={"fiyat":urun_fiyatı,"stok":urun_stok,"kategori":urun_kategori}

    print(f"{urun_adi} adlı ürün eklendi")

def urun_guncelle():
    while True:
        urun_adi=input("lütfen güncellemek istediğiniz ürünün adını giriniz:")
        if urun_adi not in urunler:
            print("girilen isimde ürün bulunamadı")
        else:
            break
    print("1.Ürün fiyatını güncelle")
    print("2.Ürün stok durumunu güncelle")

    secim=input("lütfen seçiminizi yapınız:(1-2)")

    if secim=="1":
        yeni_fiyat=input("lütfen ismini girdiğiniz ürünün yeni fiyatını giriniz:")
        urunler[urun_adi]["fiyat"]=yeni_fiyat
        print(f"{urun_adi} ürününün fiyatı {yeni_fiyat} tl olarak güncellendi")
    elif secim=="2":
        yeni_stok=int(input("lütfen ismini girdiğiniz ürünün yeni stok adedini giriniz:"))
        urunler[urun_adi]["stok"]=yeni_stok
        print(f"{urun_adi} ürününün stok miktarı {yeni_stok} olarak güncellendi")
    else:
        print("girdiğiniz isimde bir ürün bulunamadı")

def urun_sil():
    urun_adi=input("lütfen silmek istediğiniz ürünün ismini giriniz:")
    if urun_adi in urunler:
        del urunler[urun_adi]
        print(f"{urun_adi} isimli ürün silindi")
    else:
        print("girdiğiniz isimde ürün bulunamadı")

def urunleri_listele():
    if not urunler:
        print("rafta herhangi bir ürün bulunamadı")
    else:
        for urun_adi, bilgiler in urunler.items():
            print(f"Ürün:{urun_adi}")
            print(f"Fiyat:{bilgiler['fiyat']}")
            print(f"Ürün stoğu:{bilgiler['stok']}")
            print(f"Kategori:{bilgiler['kategori']}")

while True:
    print("1.Ürün ekleme:")
    print("2.Ürün güncelleme")
    print("3.Ürün silme")
    print("4.Ürün listeleme")
    print("5.Çıkış")

    secim=input("lütfen seçiminizi yapınız:(1-5)")

    if secim=="1":
        urun_ekle()
    elif secim=="2":
        urun_guncelle()
    elif secim=="3":
        urun_sil()
    elif secim=="4":
        urunleri_listele()
    elif secim=="5":
        print("Çıkış yapılıyor..")
    else:
        print("Geçersiz seçim")   