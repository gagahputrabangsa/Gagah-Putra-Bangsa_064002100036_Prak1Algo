#Mengubah huruf dengan menggunakan perintah upper()
print ("Mengubah Huruf Kecil menjadi Kapital")
print("silahkan masukan huruf yang ingin diubah")
a=input()
#perintah input() untuk memasukan string
print("Menjadi= ", a.upper())
print("===========================================")

#mengembalikan kode bilangan unicode dari sebuah karakter string dengan perinta ord()
print("Mencari Unicode dari sebuah String")
print("silahkan masukan huruf yang ingin diketahui")
b=input()
#perintah input() untuk memasukan string 
print("Unicodenya adalah= ", ord(b))
print("=============================================")

#membuat operasi hitung aritmatika sederhana

# fungsi penjumlahan(add)
def add(x, y):
   return x + y
# fungsi pengurangan(substract)
def subtract(x, y):
   return x - y
# fungsi perkalian(multiply)
def multiply(x, y):
   return x * y
# fungsi pembagian(divide)
def divide(x, y):
   return x / y
#fungsi def() itu untuk dipanggil nantinya
# menu operasi
print("Pilih Operasi.")
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
# Meminta input dari user
choice = input("Mau yang mana (1/2/3/4): ")
nomer1 = int(input("Masukkan bilangan pertama: "))
nomer2 = int(input("Masukkan bilangan kedua: "))
if choice == '1':
   print(nomer1,"+",nomer2,"=", add(nomer1,nomer2))
elif choice == '2':
   print(nomer1,"-",nomer2,"=", subtract(nomer1,nomer2))
elif choice == '3':
   print(nomer1,"*",nomer2,"=", multiply(nomer1,nomer2))
elif choice == '4':
   print(nomer1,"/",nomer2,"=", divide(nomer1,nomer2))
else:
    #perintah elese() akan berjalan ketika kita salah memasukan keyword
   print("Input salah, coba lagi ya!")
print("Sekian dari saya, terimakasih")
print("Nama : Gagah Putra Bangsa")
print("Nik: 064002100036")