#input nama mahasiswa
nama = input("Masukkan nama mahasiswa:").strip().capitalize()

#Menentukan target nilai
if nama =="Andi":
    target =70
elif nama =="Budi":
    target =75
elif nama =="Citra":
    target =80
else:
    print("Nama mahasiswa tidak terdaftar!")
    exit()

print("\nNama Mahasiswa :", nama)
print("Target Nilai :", target)

#proses ujian
percobaan = 1
lulus = False

while percobaan <= 3 and not lulus:
    print("\nPercobaan ke-", percobaan)
    nilai = int(input("Masukkan nilai ujian:"))

    if nilai >=target:
        print("Selamat, kamu berhasil mencapai target!")
        lulus = True

    else:
        print("Nilai belum mencapai target.")

        if percobaan < 3:
            print("Silahkan mengikuti remed:")
        else:
            print("Kesempatan ujian sudah habis.")

        percobaan += 1

#Hasil akhir
print("\n==== HASIL AKHIR ====")
if lulus:
    print(nama, "DINYATAKAN LULUS!")
else:
    print(nama, "DINYATAKAN TIDAK LULUS")