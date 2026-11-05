jumlah = int(input("jumlah mahasiswa : "))

if jumlah < 5 or jumlah > 10:
    print("Jumlah mahasiswa harus 5 - 10!")
else:
    total = 0
    for i in range(1, jumlah + 1):
        nilai = float(input(f"Masukkan Nilai mahasiswa {i} : "))
        total += nilai

        if nilai >= 90:
            print("Nilai : A")
        elif nilai >= 80:
            print("Nilai : B")
        elif nilai >= 70:
            print("Nilai : C")
        elif nilai >= 60:
            print("Nilai : D")
        else:
            print("Nilai : E")

    rata = total / jumlah
    print(f"Nila rata - rata : {rata}")

    if rata >= 60:
        print("Keterangan : LULUS")
    else:
        print("Keterangan : TIDAK LULUS")1