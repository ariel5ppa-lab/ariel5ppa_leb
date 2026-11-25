nilaitugas =int(input("masukkan nilai tugas : "))
uts = int(input("masukkan nilai UTS : "))
uas = int(input("masukkan nilai UAS : "))
kehadiranmahasiswa = int(input("masukkan nilai kehadiran : "))

nilai_akhir = (20 / 100 * nilaitugas) + (30 / 100 * uts) + (50 / 100 * uas)
print(nilai akhir:,nilai_akhir)

if nilai_akhir >=85 and kehadiranmahasiswa >=90
and nilai_akhir % 2==0:
    status ="LULUS DENGAN PREDIKAT"
elif nilai_akhir >= 75 and kehadiranmahasiswa >=80
print ("status : LULUS")
    else:
        status = "BELUM LULUS"
print("status mahasiswa:",status)