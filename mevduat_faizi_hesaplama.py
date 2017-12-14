print("-----------------------------------------------------\nMevduat Faizi Hesaplama Programi\n-----------------------------------------------------")

anapara = int(input("Lutfen Yatirmak Istediginiz Anaparanin miktarini yaziniz : "))
faizorani = float(input("Lutfen Mevduatinizin Yillik Faiz oranini yaziniz : "))
faizsuresi = input("Lutfen yatirmak istediginiz Mevduatin turunu yaziniz (Gunluk/Aylik/Yillik) : ")

if (faizsuresi == "Gunluk" or faizsuresi == "gunluk" ):
	gunsayisi = int(input("Lutfen Gunluk Mevduatinizin Gun sayisini seciniz (32/35) : "))
	brutfaiz = (anapara * faizorani) / 36500 * gunsayisi
	stopaj = brutfaiz * 0.15
	netfaiz = brutfaiz - stopaj
	print("{} Günlük brüt faiziniz {} TL, % 15 Vergi Stopaji {} TL, net faiziniz {} TL'dir.".format(gunsayisi,brutfaiz,stopaj,netfaiz))
elif(faizsuresi == "Aylik" or faizsuresi == "aylik"):
	aysayisi = int(input("Lutfen Aylik Mevduatinizin Ay sayisini seciniz : "))
	brutfaiz = (anapara * faizorani) / 1200 * aysayisi
	stopaj = brutfaiz * 0.15
	netfaiz = brutfaiz - stopaj
	print("{} Aylik brüt faiziniz {} TL, % 15 Vergi Stopaji {} TL, net faiziniz {} TL'dir.".format(aysayisi,brutfaiz,stopaj,netfaiz))
elif(faizsuresi == "Yillik" or faizsuresi == "yillik"):
	yilsayisi = int(input("Lutfen Yillik Mevduatinizin Yil sayisini seciniz : "))
	brutfaiz = (anapara * faizorani) / 100 * yilsayisi
	stopaj = brutfaiz * 0.15
	netfaiz = brutfaiz - stopaj
	print("{} Yillik brüt faiziniz {} TL, % 15 Vergi Stopaji {} TL, net faiziniz {} TL'dir.".format(yilsayisi,brutfaiz,stopaj,netfaiz))
else:
	print("Lutfen Gecerli Mevduat Turu yaziniz!")