#data=input("Masukkan identitas:")
#print("Data=", data, "tipe data:", type(data))
import datetime
#hari_ini=datetime.date.today()
#print(f"Bulan= {hari_ini: %B }")
tgl= int(input("Tanggal lahir = "))
bln = int(input("Bulan lahir = "))
thn = int(input("Tahun lahir = "))
tgl_lahir = datetime.date(thn,bln,tgl)
print("Tgl lahir anda :", tgl_lahir)
print(f"Hari = {tgl_lahir: %A}")
set = [0,1,2,3,4,5]
#for i in set:
 #print(i)
for i in range(1,10):
 print(i)
text="""
ini adalah contoh dari penggunaan multi-line string
"""