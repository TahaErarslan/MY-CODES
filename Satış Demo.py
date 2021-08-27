# -*- coding: utf-8 -*-
#19010011066 TAHA ERARSLAN


urunler=[]


def URUNEKLE(): #URUNEKLEME FONKSIYONU


    urun=[]
    urun_id=input("Ürün id numarasını giriniz : ")
    urun_cesidi1=input("Ürün çeşidini giriniz : ")
    urun_adi=input("Ürün adini giriniz : ")
    marka_adi=input("Ürün markasını giriniz : ")
    fiyat=input("Ürün fiyatini giriniz : ")
    son_kullanma=input("Son kullanma tarihini giriniz : ")       
    stok_miktari=input("Ürün stok miktari : ")
        
    urun.append(urun_id)
    urun.append(urun_cesidi1)
    urun.append(urun_adi)
    urun.append(marka_adi)
    urun.append(fiyat)
    urun.append(son_kullanma)
    urun.append(stok_miktari)
    urunler.append(urun)
        
    with open("19010011066.txt","a") as dosya:
        dosya.writelines("%s\n" % f for f in urunler)
        dosya.close()
    print("\n Ürün Başarıyla Eklendi \n")

def URUNARA(): #URUN ARAMA FONKSIYONU
    id_ara=input("Arayacağınız ürünün id sini giriniz : ")
    yer = []
    urun=[]
    with open('19010011066.txt', 'r') as dosya:
        for satir in dosya:
            suankiyer = satir[:-1]

            yer.append(suankiyer)
    for a in range(len(yer)):
        ayir=yer[a].split("'")
        
        if ayir[1]==id_ara:
           urun=yer.copy()
           print("Urun id,Ürün Çeşidi,Ürün Adi,Marka Adi,Fiyat,Son Kullanma Tarihi,Stok Adedi : \n",urun[a])
           break
    menu()    
def URUNARA2(): # URUN ARAMA FONKSIYONU 2
    isim_ara=input("Arayacağınız ürünün isimini giriniz : ")
    yer = []
    urun=[]
    with open('19010011066.txt', 'r') as dosya:
        for satir in dosya:
            suankiyer = satir[:-1]

            yer.append(suankiyer)
    for a in range(len(yer)):
        ayir=yer[a].split("'")
        
        if ayir[5]==isim_ara:
           urun=yer.copy()
           print("Urun id,Ürün Çeşidi,Ürün Adi,Marka Adi,Fiyat,Son Kullanma Tarihi,Stok Adedi : \n",urun[a])
           break
    menu()
def URUNSIL(): # URUN SILME FONKSIYONU
    id_ara=input("Sileceğiniz ürünün id sini giriniz : ")
    yer = []
    sil=[]
    with open('19010011066.txt', 'r') as dosya:
        for satir in dosya:
            suankiyer = satir[:-1]
            yer.append(suankiyer)
    
        for a in range(len(yer)):
            ayir=yer[a].split("'")       
    
            if ayir[1]==id_ara:
                sil=yer.copy()
                sil.pop(a)
    
    with open("19010011066.txt","w") as dosya:
        dosya.writelines("%s\n" % f for f in sil)
        dosya.close()
    menu()    
def URUNGUNCELLEME(): #URUN GUNCELLEME FONKSIYONU
    id_ara=input("Güncelleyeceğiniz ürünün id sini giriniz : ")
    yer = []
    urun=[]
    with open('19010011066.txt', 'r') as dosya:
        for satir in dosya:
            suankiyer = satir[:-1]
            yer.append(suankiyer)
    
        for a in range(len(yer)):
            ayir=yer[a].split("'")       
    
            if ayir[1]==id_ara:
                urun=yer.copy()
                urun.pop(a)
    with open("19010011066.txt","w") as dosya:
        dosya.writelines("%s\n" % f for f in urun)
        dosya.close() 

    URUNEKLE()

            
def STOKSORGULA(): #STOK SORGULAMA FONKSIYONU
    id_ara=input("Stok Sorgulayacağınız ürünün id sini giriniz : ")
    yer = []
    with open('19010011066.txt', 'r') as dosya:
        for satir in dosya:
            suankiyer = satir[:-1]
            yer.append(suankiyer)
    
        for a in range(len(yer)):
            ayir=yer[a].split("'")
            
            if ayir[1]==id_ara:
                print(f" Ürün id : {ayir[1]} , Ürün Adı : {ayir[5]} , Stok Adedi : {ayir[13]}")
                break
    menu()
def SATIS(): #SATIS SORGULAMA FONKSIYONU
    id_ara=input("Sattığınız ürünün id sini giriniz : ")
    yer = []
    toplam=0
    with open('19010011066.txt', 'r') as dosya:
        for satir in dosya:
            suankiyer = satir[:-1]

            yer.append(suankiyer)
    for a in range(len(yer)):
        ayir=yer[a].split("'")
        
        if ayir[1]==id_ara:
            fiyat=float(ayir[9])
            print(f"Ürün id : {ayir[1]} , Satış Fiyatı : {fiyat}")
            kd_v=int(input("KDV % sini giriniz : "))//100
            satis_adedi=int(input("Satış Adedini Giriniz : "))
            toplam_kdvsiz=satis_adedi*fiyat
            kdv = toplam_kdvsiz*kd_v
            toplam =  toplam_kdvsiz+kdv
            print(f"KDV'siz Toplam Satış Fiyati = {toplam_kdvsiz}")
            print(f"KDV'li Toplam Satış Fiyati = {toplam}\n")
            print ("Lütfen Ürünü Güncelleyiniz\n")
            URUNGUNCELLEME()
            break
    menu()
def HESAPMAKINESI():# HESAP MAKINESI FONKSIYONU

    def topla(sayi1,sayi2):
        return sayi1 + sayi2
    
    def cikar(sayi1,sayi2):
        return sayi1 - sayi2
    
    def carp(sayi1,sayi2):
        return sayi1 * sayi2
    
    def bol(sayi1,sayi2):
        return sayi1 / sayi2
    while True:   
        print("Operasyon:")
        print("1 : Topla")
        print("2 : Çıkar")
        print("3 : Çarp")
        print("4 : Böl")
        print("5 : Menu")
        secenek = input("Operasyon seçiminiz? : ")
        if secenek == '5':
            break 
        
        sayi1 = int(input("Birinci sayı? : "))
        sayi2 = int(input("İkinci sayı? : "))
        
        if secenek == '1':
            print("Toplam : " +str(topla(sayi1,sayi2)))
        elif secenek == '2':
            print("Çıkarma : " +str(cikar(sayi1,sayi2)))   
        elif secenek == '3':
            print("Çarpma : " +str(carp(sayi1,sayi2))) 
        elif secenek == '4':
            print("Bölme : " +str(bol(sayi1,sayi2)))
        else:
            print("Geçersiz seçenek")
    menu()
def menu():
    islem=int(input("""                 YAPACAGINIZ ISLEMI SECINIZ \n 
                    1 : URUN EKLE \n
                    2 : URUN ARA(id e göre)\n
                    3 : URUN ARA (Ürün Adina Göre)\n
                    4 : URUN SIL \n
                    5 : URUN GUNCELLE\n
                    6 : STOK SORGULA \n
                    7 : SATIS HESABI \n
                    8 : HESAP MAKINESI \n
                    9 : ÇIKIŞ \n""")) 
    
    if islem==1:
        islem=0
        URUNEKLE()
        menu()
    if islem==2:
        islem=0
        URUNARA()
    if islem==3:
        islem=0
        URUNARA2()
    if islem==4:
        islem=0
        URUNSIL()
    if islem==5:
        islem=0
        URUNGUNCELLEME()
    if islem==6:
        islem=0
        STOKSORGULA()
    if islem==7:
        islem=0
        SATIS()
    if islem==8:
        islem=0
        HESAPMAKINESI()
    if islem==9:
        exit
        


menu()   
    

