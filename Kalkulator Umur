#Latihan Date and Time
import datetime as dt

hari = dt.date.today()
print(hari)
print(f"Hari ini adalah hari = {hari:%A}")
tanggal = dt.date(1987,5,30)
print(tanggal)
print(f"Tanggal ini adalah hari = {tanggal:%A}")

print("Silahkan masukkan tanggal, bulan, dan tahun lahir anda")
tanggal = int(input("Tanggal\t: "))
bulan = int(input("Bulan\t: "))
tahun = int(input("Tahun\t: "))
lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {lahir}")
print(f"Harinya adalah : {lahir:%A}")

umur_hari = hari - lahir
print(f"Umur anda adalah : {umur_hari}")
umur_tahun = umur_hari.days // 365
print(f"Umur anda adalah : {umur_tahun} tahun")
umur_sisa = (umur_hari.days % 365) // 30
print(f"Umur anda adalah : {umur_tahun} tahun, {umur_sisa} bulan")
umur_akhir = (umur_hari.days % 365) % 30
print(f"Umur anda adalah : {umur_tahun} tahun, {umur_sisa} bulan, {umur_akhir} hari")
