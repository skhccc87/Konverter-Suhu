print("====Rentang Angka====")
angka = float(input("Masukkan angka bernilai\nKurang dari 3\natau\nLebih dari 10 :\n"))
#periksa angka kurang dari 3
kurangdari = (angka < 3)
print('Kurang dari 3 =',kurangdari)
#periksa angka lebih dari 10
lebihdari = (angka > 10)
print('Lebih dari 10 =',lebihdari)

hasil = kurangdari or lebihdari
print('Angka yang anda masukkan =',hasil)

#kasus irisan angka -----3++++++10-----
print("====Irisan Angka====")
angka = float(input("Masukkan angka bernilai\nLebih dari 3\natau\nKurang dari 10 :\n"))
#periksa angka kurang dari 10
kurangdari = (angka < 10)
print('Kurang dari 10 =',kurangdari)
#periksa angka lebih dari 3
lebihdari = (angka > 3)
print('Lebih dari 3 =',lebihdari)

hasil = kurangdari and lebihdari
print('Angka yang anda masukkan =',hasil)

"""
tugas 1
----0++++5----8++++11----
"""
angka = float(input("Masukkan angka bernilai\nAntara 0 dan 5 atau\nAntara 8 dan 11 :\n"))
#periksa angka antara 0 dan 5
kurangdari = (angka < 5)
print('Kurang dari 5 =',kurangdari)
lebihdari = (angka > 0)
print('Lebih dari 0 =',lebihdari)
banding1 = kurangdari and lebihdari
#periksa angka antara 8 dan 11
kurangdari = (angka < 11)
print('Kurang dari 11 =',kurangdari)
lebihdari = (angka > 8)
print('Lebih dari 8 =',lebihdari)
banding2 = kurangdari and lebihdari

hasil = banding1 or banding2
print('Angka yang anda masukkan =',hasil)

"""
tugas 2
++++0----5++++8----11++++
"""
angka = float(input("Masukkan angka bernilai\nKurang dari 0 atau\nAntara 5 dan 8 atau\nLebih dari 11 :\n"))
#periksa angka kurang dari 0
kurangdari1 = (angka < 0)
print('Kurang dari 0 =',kurangdari1)
#periksa angka antara 5 dan 8
lebihdari1 = (angka > 5)
print('Lebih dari 5 =',lebihdari1)
kurangdari2 = (angka < 8)
print('Kurang dari 0 =',kurangdari2)
banding1 = kurangdari2 and lebihdari1
#periksa angka lebih dari 11
lebihdari2 = (angka > 11)
print('Lebih dari 11 =',lebihdari2)

hasil = kurangdari1 or banding1 or lebihdari2
print('Angka yang anda masukkan =',hasil)
