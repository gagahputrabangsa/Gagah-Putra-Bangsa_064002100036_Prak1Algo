import math

x=input("Masukkan angka pertama : ")

p1=x.split(",")

y=input("Masukkan angka kedua : ")

p2=y.split(",")

jarak = math.sqrt( ((int(p1[0])-int(p2[0]))*2)+((int(p1[1])-int(p2[1]))*2) )

print ("Jarak antara ", x,"dan", y, "adalah", jarak)