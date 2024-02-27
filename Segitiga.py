#latihan membuat segitiga
sisi = int(input("Masukkan sisi = "))

#1. for
print("Awal Segitiga FOR")
count = 1 #dummy variable
for i in range(sisi):
    print("*"*count)
    count += 1
print("Akhir Segitiga FOR")

#2. while
print("Awal Segitiga WHILE")
count = 1
while True:
    print("*"*count)
    count += 1
    if count > sisi:
        break
print("Akhir Segitiga WHILE")

#3. ganjil aja
print("Awal Segitiga GANJIL")
count = 1
while True:
    if (count%2):
        print("*"*count)
        count += 1
    else:
        count += 1
        continue        
    if count > sisi:
        break
print("Akhir Segitiga GANJIL")

#4. sama sisi
print("Awal Segitiga Sama Sisi")
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print(" "*spasi,"*"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue        
    if count > sisi:
        break
print("Akhir Segitiga Sama Sisi")

#5. ketupat
print("Awal Ketupat")
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print(" "*spasi,"*"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue        
    if count > sisi:
        count -= 1
        spasi += 1
        break
while True:
    #print(count,",",spasi)
    if (count%2):
        print(" "*spasi,"*"*count)
        spasi += 1
        count -= 1
    else:
        count -= 1
        continue
    if count < 0:
        break
print("Akhir Ketupat")


