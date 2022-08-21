#Berangkat jam 08 : 52 : 45
Jam = int(8)
Menit = int(52)
Detik = int(45)
Detik_berangkat = (Jam*3600)+(Menit*60)+Detik
#Tiba Tujuan jam 12 : 15 : 10
Jamtiba = int(12)
Menittiba = int(15)
Detiktiba = int(10)
Detik_tiba = (Jamtiba*3600)+(Menittiba*60)+Detiktiba
#berapa Jam menit detik dalam perjalanan
Total = Detik_tiba-Detik_berangkat
JamSampai = int(Total/3600)
Menitsampai = int((Total%3600)/60) 
Detiksampai = int(Total%60)
print("Berapa waktu yang dihabisikan dalam perjalanan = ", JamSampai,"Jam",Menitsampai,"Menit",Detiksampai,"Detik")