n1= input ("Jumlah Tanda Tangan DOSEN= ")
n2= input ("Jumlah Tanda Tangan STAFF ADMINISTRASI= ")
n3= input ("Jumlah Tanda Tangan KAKAK KELAS= ")
jumlah= (int (n1) *50) + (int (n2) *30) + (int (n3) *10)
print ("Jumlah Point yang anda dapatkan adalah= ", jumlah)
if jumlah>300:
    print("Prestasi Mahasiswa PANDAI KOLABORASI")
elif jumlah<100:
    print ("Prestasi Mahasiswa KURANG KOLABORASI")
else:
    print ("Prestasi Mahasiswa CUKUP")
    