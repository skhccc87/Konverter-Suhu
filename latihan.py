print("PROGRAM KONVERSI TEMPERATUR")
print("====CELCIUS====")
cel = float(input('Masukkan suhu dalam celcius : '))
print("Suhu Celcius adalah",cel,"celcius")
ream = (4/5) * cel
print("Suhu Reamur adalah",ream,"reamur")
fah = ((9/5) * cel) + 32
print("Suhu Fahrenheit adalah",fah,"fahrenheit")
kel = cel + 273
print("Suhu Kelvin adalah",kel,"kelvin")

print("====REAMUR====")
ream = float(input('Masukkan suhu dalam reamur : '))
print("Suhu Reamur adalah",ream,"reamur")
cel = (5/4) * ream
print("Suhu Celcius adalah",cel,"celcius")
fah = ((9/4) * ream) + 32
print("Suhu Fahrenheit adalah",fah,"fahrenheit")
kel = cel + 273
print("Suhu Kelvin adalah",kel,"kelvin")

"""
tugas 1 konversi fahrenheit
"""
print("====FAHRENHEIT====")
fah = float(input('Masukkan suhu dalam fahrenheit : '))
print("Suhu Fahrenheit adalah",fah,"fahrenheit")
cel = (5/9) * (fah-32)
print("Suhu Celcius adalah",cel,"celcius")
ream = (4/9) * (fah-32)
print("Suhu Reamur adalah",ream,"reamur")
kel = cel + 273
print("Suhu Kelvin adalah",kel,"kelvin")

"""
tugas 2 koversi kelvin
"""
print("====KELVIN====")
kel = float(input('Masukkan suhu dalam kelvin : '))
print("Suhu Kelvin adalah",kel,"kelvin")
cel = kel - 273
print("Suhu Celcius adalah",cel,"celcius")
ream = (4/5) * (kel-273)
print("Suhu Reamur adalah",ream,"reamur")
fah = ((9/5) * cel) + 32
print("Suhu Fahrenheit adalah",fah,"fahrenheit")
