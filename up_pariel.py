print("=== sistem penilaian===")

jumlah = int(input("Masukkan jumlah mahasiswa: "))

data = []
lulus = 0
tidak_lulus = 0

for i in range(jumlah):
    print("\nMahasiswa ke-", i + 1)

    nama = input("Nama mahasiswa: ")
    nilai = int(input("Masukkan nilai: "))

    if nilai >= 85:
        kategori = "A (Sangat Baik)"
    elif nilai >= 75:
        kategori = "B (Baik)"
    elif nilai >= 60:
        kategori = "C (Cukup)"
    else:
        kategori = "D (Tidak Lulus)"

    if nilai >= 60:
        lulus += 1
    else:
        tidak_lulus += 1

    data.append([nama, nilai, kategori])

print("\n=== HASIL PENILAIAN ===")

for mahasiswa in data:
    print("Nama:", mahasiswa[0])
    print("Nilai:", mahasiswa[1])
    print("Kategori:", mahasiswa[2])
    print("----------------------")

print("Jumlah mahasiswa lulus:", lulus)
print("Jumlah mahasiswa tidak lulus:", tidak_lulus)
