import random
from os import system

tahmin = 0
rekortemp = ""
rekortemp2= ""
def clear(): #Ekran temizleme fonksiyonu
    system("cls")
def susle(diziAd): #Sayıyı bildiğimizde ekrana gelen yazının uzunluğu kadar '-' ekler
    uzunluk = 0
    for i in diziAd: uzunluk+=len(i)
    for i in range(uzunluk): print("-",end="")
    print("\n")
def susle2(metin): # Daha büyük veya daha küçük ifadelerinin uzunluğu kadar ?. TAHMİN ifadesinin sağına ve soluna uygun şekilde paylaştırarak '-' işareti ekler
    ortaCumle = str(tahmin) +". TAHMİN"
    total = ""
    yarimTire = (len(metin) - len(ortaCumle)) / 2
    for i in range(int(yarimTire)): total += "-"
    total += ortaCumle
    for i in range(int(yarimTire)): total+="-"
    if len(str(tahmin))%2 == 0: total+="-" 
    print("\n" +total + "\n\n" + metin)
def anyKey(yazdir): #Herhangi bir tuşla döngüden çıkmayı sağlayan fonksiyon
    while True:
        print(yazdir)
        anykey = input("""

Ana menüye dönmek için "Enter" tuşuna basınız! """)
        clear()
        menuLogo()
        system("color b")
        break
def logo(): #Logo yazdıran fonksiyon
    print("""
       o   o
        \_/
        ( Oo)                           \|/
        (_=-)  .===O-  ~~GÖKHAN TÜRK ~~ -O-
        /   _/U'                        /|\\
        ||  |_/
        ||
        {( ||
            | ))
            | ||
            (__\\\\ \n""")
def menuLogo(): #Menü logosunu yazdıran fonksiyon
    print("""
         ______   ______     __  __     __    __     __     __   __    
        /\__  _\ /\  __ \   /\ \_\ \   /\ \-./  \   /\ \   /\ \-.\ \        o   o
        \/_/\ \/ \ \  __ \  \ \  __ \  \ \ \-./\ \  \ \ \  \ \ \-.  \        \_/
           \ \_\  \ \_\ \_\  \ \_\ \_\  \ \_\ \ \_\  \ \_\  \ \_\\"\_ \      ( Oo)                           \|/
            \/_/   \/_/\/_/   \/_/\/_/   \/_/  \/_/   \/_/   \/_/ \/_/      (_=-)  .===O- ~~ GÖKHAN TÜRK ~~ -O-   
                                                                            /   _/U'                        /|\\
                                                                            ||  |_/ 
                                                                            ||  
         ______     __  __     __  __     __   __     __  __                {( || 
        /\  __ \   /\ \_\ \   /\ \/\ \   /\ "-.\ \   /\ \/\ \                 | ))               
        \ \ \/\ \  \ \____ \  \ \ \_\ \  \ \ \-.  \  \ \ \_\ \                | ||              
         \ \_____\  \/\_____\  \ \_____\  \ \_\\  \_\  \ \_____\               (__\\\\                
          \/_____/   \/_____/   \/_____/   \/_/ \/_/   \/_____/                 
                                                                                                                                                        
        """)
system("color b")
clear()
menuLogo() 
with open("Rekor.txt","r") as Rekor:    #Rekor değerini txt dosyasından rekortemp değişkenine atıyorum.
    for line in Rekor:
        rekortemp = line
Rekor.close()
with open("TerstenRekor.txt","r") as Rekor2:   #Tersten Rekor değerini txt dosyasından rekortemp2 değişkenine atıyorum.
    for line in Rekor2:
        rekortemp2 = line
Rekor2.close()

while True: #Ana menü döngüsü
    secenek = input("""
    Yeni Oyun : 1
    Rekorlar  : 2
    Yardım    : 3
    Çıkış     : q
    
    Giriniz   : """)
    if(secenek == "1"): #Yeni Oyunu başlatır.
        clear()
        logo()
        UretilenSayi = random.randint(0,1000)
        while True: #Oyun döngüsü.    
            tahmin += 1
            girdi = input("\nGizemli sayıyı Tahmin Edin :) = ")
            if girdi.isdigit() and girdi != "AEZAKMI" and 0 <= int(girdi) <= 1000 and girdi !="q":  #Sayının belirlediğim aralıkta ve tipte girilmesini sağlıyorum. Hile ve çıkış için girdi kontrolü yapıyorum.
                girilensayi = int(girdi)
                tahminstr = str(tahmin)
                if girilensayi == UretilenSayi: #Girilen sayının üretilen sayıya eşit olması durumu.
                    if tahmin < int(rekortemp):     #Rekor kontrolü ve txt dosyasının üzerine yazma.
                        system("color b")
                        with open("Rekor.txt", "w") as Rekor: 
                            Rekor.write(tahminstr)
                            rekortemp = tahminstr
                            sonuc = "Tebrikler rekor kırdınız :) | Tahmin: " + str(tahmin) + " Rekor: " + str(rekortemp) + " Tersten Rekor: " + str(rekortemp2)
                            print("\n")
                            susle(sonuc)
                            for i in range(10): print(sonuc,"\n") 
                            susle(sonuc)
                            tahmin = 0
                    elif tahmin > int(rekortemp2): #Tersten rekor kontrolü ve txt dosyasının üzerine yazma.
                        system("color d")
                        with open("TerstenRekor.txt","w") as Rekor2:
                            Rekor2.write(tahminstr)
                            rekortemp2 = tahminstr
                            print("\n")   
                            sonuc = "Eh bu da rekor sayılır ama tersten :) | Tahmin: " + str(tahmin) + " Rekor: " + str(rekortemp) + " Tersten Rekor: " + str(rekortemp2)
                            susle(sonuc)
                            for i in range(10): print(sonuc,"\n")     
                            susle(sonuc)
                            tahmin = 0
                    else:   #Her iki rekor da kırılmazsa gerçekleşecek durum.
                        system("color b")
                        sonuc = "Tebrikler! | Tahmin: " + str(tahmin) + " Rekor: " + str(rekortemp) + " Tersten Rekor: " + str(rekortemp2)
                        print("\n")
                        susle(sonuc)
                        for i in range(10): print(sonuc,"\n")       
                        susle(sonuc)
                        tahmin = 0
                    Rekor.close()
                    Rekor2.close()
                    anyKey("")
                    break #Sayı bulunduğu için oyun döngüsünden çıkılır. Ancak anyKey fonksiyonu ile çıkmadan önce girdi beklenir.
                elif girilensayi < UretilenSayi: #Girilen sayının üretilen sayıdan küçük olması durumu.
                    system("color a")
                    susle2("Daha büyük :)")
                elif girilensayi > UretilenSayi: #Girilen sayının üretilen sayıdan büyük olması durumu.
                    system("color c")
                    susle2("Daha küçük :)")
                else: break               
            elif girdi == "AEZAKMI":  #Hile kodu, üretilen sayıyı gösterir.
                system("color d")
                tahmin-=1
                print("\nHile yapmıyoruz değil mi :)) :",UretilenSayi)
            elif girdi == "q": #Oyun döngüsünden çıkış sağlar.
                tahmin = 0
                clear()
                menuLogo()
                system("color b")
                break
            else: #İstediğim değerlerin dışında bir girdi girilmesi hâlinde kullanıcıya verilecek uyarı.
                system("color 4")
                tahmin-=1
                print("\nSadece 0 ile 1000 arasında bir tam sayı girebilirsiniz!")
    elif(secenek == "2"): #Rekor listesi
        clear()
        logo()
        system("color a")
        anyKey("Rekor: " + str(rekortemp) + " Tersten Rekor: " + str(rekortemp2))
    elif(secenek == "3"): #Yardım bölümü
        clear()
        system("color 3")
        logo()
        anyKey("\n  -0 ile 1000 arasında sayı girişi yaparak gizemli sayıyı bulmaya çalışın.\n\n  -Oyun içindeyken, çıkmak için 'q' tuşuna basabilirsiniz.")
    elif(secenek == "q"): #Çıkış
        clear()
        print("Güle Güle!")
        break
    else:   #Hatalı giriş.
        clear()
        logo()
        system("color 4")
        anyKey("Hatalı Giriş!")