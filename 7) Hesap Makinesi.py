while True:
    print("Hesap Makinesi")
    islem =str(input("İşlem Seçiniz: \n1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme\n5-Cikis\n")).lower()
    if islem=="Cikis" or islem=="5":
        print("Hesap Makinesi Kapatıldı.")
        break
    if islem not in ["1", "2", "3", "4"]:
        print("Geçersiz işlem! Lütfen 1-4 arası seçim yapın.")
        continue    
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: ")) 
    if islem == "1":
        print(f"Sonuç: {sayi1+sayi2}")
    elif islem == "2":
        print(f"Sonuç: {sayi1-sayi2}")    
    elif islem == "3":
        print(f"Sonuç: {sayi1*sayi2}")     
    elif islem == "4":
        if sayi2==0:
            print("Sıfıra bölme hatası!")
            continue
        else:
            print(f"Sonuç: {sayi1/sayi2}")
    else:
        print("Geçersiz işlem! Lütfen 1-5 arası seçim yapın.")      