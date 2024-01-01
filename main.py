a = 9
b = 5
c= a | b
#print('\n======OR======')
#print('nilai :' , a,', binary :',format(a,'08b'))
#print('nilai :' , b,', binary :',format(b,'08b'))
#print('nilai :' , c,', binary :',format(c,'08b'))

data_int = int(input("hitung sampai ="))

angka=0

while True:
    angka+= 1
    print(f"count = {angka}")
    if angka==data_int:
     print("nice!")
     break
      