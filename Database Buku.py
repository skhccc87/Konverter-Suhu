data_buku = []
while True:
    print("\nMasukkan Data Buku")
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan penulis buku: ")
    
    buku_baru = [judul,penulis]
    data_buku.append(buku_baru)

    print("\n","="*10,"Data Buku","="*10)
    for index,buku in enumerate(data_buku):
        print(f"{index+1}\t| {buku[0]}\t| {buku[1]}")

    print("\n","="*10)
    baru = input("Apa ada data baru? (y/n) :")
    if baru == "n":
        break

print("Program Selesai")

    
