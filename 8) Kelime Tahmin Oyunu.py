import random

# Kelime listesi
kelimeler = ["python", "bilgisayar", "programlama", "oyun", "klavye"]

# Rastgele kelime seç
gizli_kelime = random.choice(kelimeler)

# Oyuncu için boş gösterim
tahmin_durumu = ["_"] * len(gizli_kelime)

# Kalan hak
can = 6

print("Kelime Tahmin Oyununa Hoş Geldin!")
print(" ".join(tahmin_durumu))

while can > 0 and "_" in tahmin_durumu:
    tahmin = input("Bir harf tahmin et: ").lower()
    
    if tahmin in gizli_kelime:
        print("Doğru!")
        for i, harf in enumerate(gizli_kelime):
            if harf == tahmin:
                tahmin_durumu[i] = tahmin
    else:
        can -= 1
        print(f"Yanlış! Kalan can: {can}")
    
    print(" ".join(tahmin_durumu))

# Oyun sonu
if "_" not in tahmin_durumu:
    print("🎉 Tebrikler! Kelimeyi buldun:", gizli_kelime)
else:
    print("😢 Kaybettin! Kelime:", gizli_kelime, "idi.")