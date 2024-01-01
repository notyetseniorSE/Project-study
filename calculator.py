print(10*"=")
print("Kalkulator Sederhana")
print(10*"=" + "\n")
angka_1=float(input("Masukkan angka 1 ="))
operator=input("operator(+-*=):")
angka_2=float(input("Masukkan angka 2 ="))
#percabangannya
if operator=="+":
  hasil= angka_1 + angka_2
  print(hasil)
elif operator=="-":
  hasil=angka_1-angka_2
  print(hasil)
elif operator=="x" or operator=="*":
  hasil=angka_1*angka_2
  print(hasil)
elif operator=="/":
  hasil= angka_1/angka_2