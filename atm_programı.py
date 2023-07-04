print("""*********
ATM
1.Bakiye Sorgulama 
2.Para Yatırma 
3.Para Çekme
bankadan çıkmak içi q'ya basınız
********
""")
bakiye = 1000
while True:
    islem = int(input("Yapacağınız işleminizi giriniz : "))

    if (islem== "q" ):
        print("Yine bekleriz")
        break
    elif (islem==1):
        print("Bakiyeniz {} tl'dir".format(bakiye))

    elif(islem==2):
        gelen_para = int(input("Yatırmak istediğiniz tutarı giriniz : "))
        bakiye+=gelen_para

    elif(islem==3):
        giden_para = int(input("Çekmek istediğiniz tutarı giriniz : "))
        if (bakiye<giden_para):
            print("Yetersiz bakiye")
            continue
        bakiye-=giden_para



