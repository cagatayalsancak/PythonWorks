print("-----------------------------------------------------\nMevduat Faizi Hesaplama Programi\n-----------------------------------------------------")

anaPara = int(input("Lutfen Yatirmak Istediginiz Anaparanin miktarini yaziniz : "))
faizOrani = float(input("Lutfen Mevduatinizin Yillik Faiz oranini yaziniz : "))
mevduatTuru = input("Lutfen yatirmak istediginiz Mevduatin turunu yaziniz (Gunluk/Aylik/Yillik) : ")
def faizHesapla(anaPara, faizOrani, mevduatTuru, mevduatSuresi, mevduatTS):
	brutFaiz = (anaPara * faizOrani) / mevduatTS * mevduatSuresi
	stopaj = brutFaiz * 0.15
	netFaiz = brutFaiz - stopaj
	return brutFaiz, stopaj, netFaiz, mevduatSuresi
	
if (faizsuresi == "Gunluk" or faizsuresi == "gunluk" ):
	mevduatSuresi = int(input("Lutfen Gunluk Mevduatinizin Gun sayisini seciniz (32/35) : "))
	mevduatTS = 36500
	faizHesapla(anaPara, faizOrani, mevduatTuru, mevduatSuresi, mevduatTS)
	print("{} Günlük brüt faiziniz {} TL, % 15 Vergi Stopaji {} TL, net faiziniz {} TL'dir.".format(gunsayisi,brutfaiz,stopaj,netfaiz))
elif(faizsuresi == "Aylik" or faizsuresi == "aylik"):
	mevduatSuresi = int(input("Lutfen Aylik Mevduatinizin Ay sayisini seciniz : "))
	mevduatTS = 1200
	faizHesapla(anaPara, faizOrani, mevduatTuru, mevduatSuresi, mevduatTS)
	print("{} Aylik brüt faiziniz {} TL, % 15 Vergi Stopaji {} TL, net faiziniz {} TL'dir.".format(aysayisi,brutfaiz,stopaj,netfaiz))
elif(faizsuresi == "Yillik" or faizsuresi == "yillik"):
	mevduatSuresi = int(input("Lutfen Yillik Mevduatinizin Yil sayisini seciniz : "))
	mevduatTS = 100
	faizHesapla(anaPara, faizOrani, mevduatTuru, mevduatSuresi, mevduatTS)
	print("{} Yillik brüt faiziniz {} TL, % 15 Vergi Stopaji {} TL, net faiziniz {} TL'dir.".format(yilsayisi,brutfaiz,stopaj,netfaiz))
else:
	print("Lutfen Gecerli Mevduat Turu yaziniz!")
