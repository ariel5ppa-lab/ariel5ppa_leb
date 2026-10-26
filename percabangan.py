# # input
# nilai = int(input("Masukkan Nilai: "))
# # proses
# if nilai >=80 and nilai<=100:
#     print("Anda Mendapatkan Nilai A")
# elif nilai >=70 and nilai <=80:
#     print ("Anda Mendapatkan Nilai B")
# elif nilai >=50 and nilai <=70:
#     print ("Anda Mendapatkan Nilai C")
# elif nilai >=30 and nilai >=50:
#     print ("Anda Mendapatkan Nilai D")
# elif nilai >=0 and nilai >=20:
#     print ("Anda Mendapatkan Nilai E")
# else:
#     print ("Data Tidak Valid")
# print("-----Latihan-----")
# # input

nama_barang = input("Masukkan nama barang: ")
harga_barang = int(input("Masukkan harga barang: "))

if nama_barang.lower() == "kulkas":
    diskon = 0.10 *harga_barang
elif nama_barang.lower() == "tv":
    diskon = 0.05 * harga_barang
elif nama_barang.lower() == "radio":
    diskon = 0
else:
    print("Nama barang tidak tersedia")
    diskon = 0

jumlah_bayar = harga_barang - diskon

# output
print("========================")
print("Nama barang :", nama_barang)
print("Harga barang:", harga_barang)
print("Diskon      :", diskon)
print("Jumlah bayar:", jumlah_bayar)
print("========================")