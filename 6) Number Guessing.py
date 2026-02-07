from random import randint
computer_guess=randint(1, 100)
while True:
    user_guess=int(input("1 ile 100 arasında bir sayı tahmin edin: "))
    if user_guess < computer_guess:
        print("Daha Yüksek bir sayı tahmin edin.")
        continue
    elif user_guess > computer_guess:
        print("Daha Düşük bir sayı tahmin edin.")
        continue
    else:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break        
