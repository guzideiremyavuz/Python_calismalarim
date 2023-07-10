def not_hesaplama (satır):
    satır= satır[:-1]
    liste = satır.split(",")

    isim = liste[0]

    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not >= 90):

        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + "----->" + harf + "\n"

def kalan(satır):
    satır = satır[:-1]
    liste = satır.split(",")

    isim = liste[0]

    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (4 / 10)

    if (son_not <= 54 ):

        harf = "FF"
        print("kaldın :(")




def gecen (satır):
    satır = satır[:-1]
    liste = satır.split(",")

    isim = liste[0]

    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (4 / 10)

    if (son_not >= 90):

        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"





with open ("dosya.txt","r", encoding="utf-8") as file :

    eklenecekler = []

    for i in file :
        eklenecekler.append(not_hesaplama(i))

with open ("notlar.txt","w",encoding="utf-8") as file2:

    for i in eklenecekler :
        file2.write(i)


with open ("dosya.txt","r",encoding="utf-8") as file3:

    kalanlar = []

    for i in file3 :
        kalanlar.append(kalan(i))

with open ("kalanlar.txt","w",encoding="utf-8") as file4:

    for i in kalanlar :
        file4.write(i)


with open ("dosya.txt","r",encoding="utf-8") as file5:

    gecenler =[]

    for i in file5 :
        gecenler.append(gecen(i))

with open("gecenler.txt","w",encoding="utf-8") as file6:

    for i in gecenler:
        file6.write(i)