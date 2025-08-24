pj= input ("Masukkan Nilai Penulisan Jurnal= ")
pb= input ("Masukkan Nilai Penulisan Buku= ")
pp= input ("Masukkan Nilai Penulisan Paper= ")
jumlah= int (pj)*3 + int (pb)*2 + int (pp)
print ("Hasil Kuota adalah = ", jumlah)
if jumlah  >7:
    print ("Anda Naik Pangkat")
elif jumlah <5:
    print ("Anda Tidak Naik Pangkat")
else :
    print ("Anda Naik Pangkat Bersyarat")