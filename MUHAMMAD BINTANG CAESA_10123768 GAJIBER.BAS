10 For i = 1 To 2
    20 Input "Masukkan NIP=", nip$(i)
    30 Input "Masukkan Nama Pegawai=", nama$(i)
    40 Input "Masukkan Gaji pokok=", gaji(i)
    50 Let tunkel(i) = gaji(i) * 50 / 100
    60 Let tunprof(i) = gaji(i) * 30 / 100
    70 Let gajikot(i) = gaji(i) + tunkel(i) + tunprof(i)
    80 Let pajak(i) = gajikot(i) * 5 / 100
    90 Let gajiber(i) = gajikot(i) - pajak(i)
    100 Print
110 Next i
120 For j = 1 To 2
    130 Print "NIP"; nip$(j)
    140 Print "Nama Pegawai="; nama$(j)
    150 Print Using "Gaji Pokok = #,"; gaji$(j)
    160 Print Using "Tunjangan Keluarga = #, "; tunkel(j)
    170 Print Using "Tunjangan profesi = #, "; tunprof(j)
    180 Print Using "Gaji kotor = #,"; gajikot(j)
    190 Print Using "Pajak = #,"; pajak(j)
    200 Print Using "Gaji Bersih =#,"; gajiber(j)
    210 Print
    220 Print
230 Next (j)
240 End
