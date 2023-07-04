class Hayvan():

    def __init__(self,Tür,Ömrü,Üreme_gelişme_şekli,):
        self.Tür= Tür
        self.Ömrü= Ömrü
        self.Üreme_gelişme_şekli= Üreme_gelişme_şekli



    def Bilgileri_göster(self):

        print("""Hayvanın Özellikleri\nÇok Hücrelilerdir\nÖkaryotik Hücre Yapısı\nÖzel Dokular\nEşeyli üreme\nBir Blastula Gelişim Aşaması\nHareket Kabiliyeti\nHeterotrofi (Yiyecekleri Yutma Yeteneği)\nGelişmiş Sinir Sistemleri""")


        print("Tür : {}\nÖmrü : {}\nÜreme gelişme şekli : {}".format(self.Tür,self.Ömrü,self.Üreme_gelişme_şekli))


class Köpek(Hayvan):
    pass

class Kuş(Hayvan):
    pass

class At(Hayvan):
    pass

secilen_hayvan = Hayvan()


while True:

    secilen_hayvan= input("Köpek/Kuş/At birini seçiniz : ")






        







