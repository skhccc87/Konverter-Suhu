print(10*"=")
print("Kalkulator Sederhana")
print(10*"="+"\n")

angka1 = float(input("Masukkan angka 1 = "))
operator = input("Operator (+,-,x,/) = ")
angka2 = float(input("Masukkan angka 2 = "))

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "x" or operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    hasil = angka1 / angka2
else:
    print("Tolong masukkan yang benar")

print(f"Hasilnya adalah = {hasil}")
print("Akhir dari program")
