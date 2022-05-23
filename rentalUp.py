import math

jam_masuk,menit_masuk=input("Waktu Masuk (hh:mm) :"). split(":")
jam_keluar,menit_keluar=input("Waktu Keluar (hh:mm) :"). split(":")
jam_masuk = int(jam_masuk)
menit_masuk = int(menit_masuk)
jam_keluar = int(jam_keluar)
menit_keluar = int(menit_keluar)
if jam_masuk>jam_keluar :
    jam_keluar=jam_keluar+24
masuk= jam_masuk * 60
menitmasuk = masuk + menit_masuk

keluar= jam_keluar * 60
menitkeluar = keluar + menit_keluar



menit = menitkeluar - menitmasuk
jam= menit // 60
menitjam= menit % 60
biaya_rental = 5000* menit / 60
print(f"Lama Rental          : {menit} Menit ({jam} Jam {menitjam} Menit )")
print(f"Biaya Rental Asli    : Rp. {biaya_rental :2.0f}")
biaya_rental = round(biaya_rental, -3)
print(f"Biaya Rental Bulat   : Rp. {biaya_rental:2.0f}") ##pembulatan biasa
biaya_rental=math.ceil(biaya_rental/1000)*1000
print(f"Biaya Rental A       : Rp. {biaya_rental:2.0f}") ##pembulatan keatas
biaya_rental=math.floor(biaya_rental/1000)*1000
print(f"Biaya Rental B       : Rp. {biaya_rental:2.0f}") ##pembulatan kebawah

