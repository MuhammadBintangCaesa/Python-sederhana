for i in range(2) :
    NIP = int(input("NIP : "))
    namaP = input("Nama : ")
    gPokok = int(input("Masukkan Gaji Pokok : "))
    tKeluarga = gPokok * 50/100
    tProfesi = gPokok * 70/100
    gKotor= gPokok + tKeluarga + tProfesi
    pajak= gKotor* 5/100
    gBersi= gKotor - pajak
    print("Total Tunjangan Keluarga anda :",tKeluarga)
    print("Total Tunjangan Profesi anda: ", tProfesi)
    print ("Pajak 5%: ",pajak)
    print ("Gaji Kotor: ", gKotor)
    print ("Gaji Bersih: ",gBersi)
    print()
    print()