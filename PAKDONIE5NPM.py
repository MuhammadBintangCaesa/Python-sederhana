... 
... # Fungsi untuk menghitung gaji bersih
... def hitung_gaji_bersih(gaji_pokok, tunjangan_keluarga, tunjangan_profesi, pajak):
...     gaji_bersih = gaji_pokok + tunjangan_keluarga + tunjangan_profesi - pajak
...     return gaji_bersih
... 
... # Input data pegawai
... for i in range(2):  # Diulang sebanyak 2 kali
...     no_pegawai = input("Masukkan nomor pegawai: ")
...     nama_pegawai = input("Masukkan nama pegawai: ")
...     gaji_pokok = float(input("Masukkan gaji pokok: "))
...     tunjangan_keluarga = float(input("Masukkan tunjangan keluarga: "))
...     tunjangan_profesi = float(input("Masukkan tunjangan profesi: "))
... 
...     # Menghitung total penghasilan
...     total_penghasilan = gaji_pokok + tunjangan_keluarga + tunjangan_profesi
... 
...     # Menghitung pajak
...     pajak = hitung_pajak(total_penghasilan)
... 
...     # Menghitung gaji bersih
...     gaji_bersih = hitung_gaji_bersih(gaji_pokok, tunjangan_keluarga, tunjangan_profesi, pajak)
... 
...     # Menampilkan hasil
...     print("\n===== Data Pegawai =====")
...     print("Nomor Pegawai:", no_pegawai)
...     print("Nama Pegawai:", nama_pegawai)
...     print("Gaji Bersih:", gaji_bersih)
