#Berangkat jam 08 : 52 : 45
Jam = int(8)
Menit = int(52)
Detik = int(45)
Detik_berangkat = (Jam*3600)+(Menit*60)+Detik
#Waktu Tempuh sampe Tujuan 5000 Detik
Waktu_tempuh = int(5000)
Total = Detik_berangkat + Waktu_tempuh
#pukul berapa tiba di tujuan
JamSampai = int(Total/3600)
Menitsampai = int((Total%3600)/60) 
Detiksampai = int(Total%60)
print("Tiba di tujuan pukul = ",JamSampai,":",Menitsampai,":",Detiksampai)