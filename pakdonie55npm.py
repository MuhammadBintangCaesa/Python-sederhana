Python 3.12.0 (v3.12.0:fb18b02c8, Oct  2 2023, 9:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def hitung_pajak(total_penghasilan):
...     return total_penghasilan * 0.05
... 
... def hitung_gaji_bersih(gaji_pokok, tunjangan_keluarga, tunjangan_profesi):
...     total_penghasilan = gaji_pokok + tunjangan_keluarga + tunjangan_profesi
...     pajak = hitung_pajak(total_penghasilan)
...     gaji_bersih = total_penghasilan - pajak
...     return gaji_bersih
... 
... for _ in range(2):  # Perulangan 2 kali
...     # Input data pegawai
...     no_induk = input("Masukkan nomor induk pegawai: ")
...     nama_pegawai = input("Masukkan nama pegawai: ")
...     gaji_pokok = float(input("Masukkan gaji pokok: "))
...     tunjangan_keluarga = float(input("Masukkan tunjangan keluarga: "))
...     tunjangan_profesi = float(input("Masukkan tunjangan profesi: "))
... 
...     # Hitung pajak dan total gaji bersih
...     gaji_bersih = hitung_gaji_bersih(gaji_pokok, tunjangan_keluarga, tunjangan_profesi)
... 
...     # Output hasil
...     print("\nHasil perhitungan untuk", nama_pegawai)
...     print("No. Induk Pegawai:", no_induk)
...     print("Nama Pegawai:", nama_pegawai)
...     print("Gaji Bersih:", gaji_bersih)
