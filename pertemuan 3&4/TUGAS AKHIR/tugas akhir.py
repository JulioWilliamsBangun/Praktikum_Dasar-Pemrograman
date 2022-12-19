
'''
Tugas praktek 
Nama : Julio Williams
Nim : 2270211012
Tugas membuat aplikasi kasir menggunakan bahasa python
'''

#created by Julio Williams

'''
kasir pom bensin
program ini berfungsi untuk mencetak bon transaksi kasir pom bensin
program akan meminta memasukkan indentias pelanggan, kemudian akan menghitung biaya dari pembelian pelanggan tsb dan mencetak bon hasil pembelian tsb
'''

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

import time
tanggal = time.strftime(" %d-%m-%y %H:%M:%S ")
print(tanggal)

print(" Pom Estadio")
print(" Jalan raya Estadio Futsal blok j2 no 20 ")
print(" No. 08517778899 ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Jenis Bensin ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" 1. Shol super  : 5000 ")
print(" 2. CPower : 10000")
print(" 3. Pertamex : 15000")
print(" 4. Perlotol : 20000")
print(" 5. Eceran  : 25000")
print(" 6. diesel  : 30000")
print(" 7. Air mata bang iqbal: 50000")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

namaPelanggan=str(input(" Masukkan nama pelanggan : "))
ListMenu=str(input(" Masukkan angka sesuai dengan menu yang tersedia : "))
JumlahPesanan=int(input(" Masukkan jumlah pesanan : "))

if ListMenu == "1":
    namaMenu = " Shol super "
    hargaPerBarang=(5000)
    jumlah=(5000*JumlahPesanan)
    pajak=int(jumlah * 0.1)
    if JumlahPesanan >= 5:
        totaljumlah=int(jumlah+pajak)
    else: 
        totaljumlah=int(jumlah+pajak)

if ListMenu == "2":
    namaMenu = " CPower "
    hargaPerBarang=(10000)
    jumlah=(10000*JumlahPesanan)
    pajak=int(jumlah * 0.1)
    if JumlahPesanan >= 5:
        totaljumlah=int(jumlah+pajak)
    else:
        totaljumlah=int(jumlah+pajak)

if ListMenu == "3":
    namaMenu = " Pertamex "
    hargaPerBarang=(15000)
    jumlah=(15000*JumlahPesanan)
    pajak=int(jumlah * 0.1)
    if JumlahPesanan >= 5:
        totaljumlah=int(jumlah+pajak)
    else:
        totaljumlah=int(jumlah+pajak)

if ListMenu == "4":
    namaMenu = " Perlotol "
    hargaPerBarang=(20000)
    jumlah=(20000*JumlahPesanan)
    pajak=int(jumlah * 0.1)
    if JumlahPesanan >= 5:
        totaljumlah=int(jumlah+pajak)
    else:
        totaljumlah=int(jumlah+pajak)

if ListMenu == "5":
    namaMenu = " Eceran "
    hargaPerBarang=(25000)
    jumlah=(25000*JumlahPesanan)
    pajak=int(jumlah * 0.1)
    if JumlahPesanan >= 5:
        totaljumlah=int(jumlah+pajak)
    else:
        totaljumlah=int(jumlah+pajak)

if ListMenu == "6":
    namaMenu = " diesel "
    hargaPerBarang=(30000)
    jumlah=(30000*JumlahPesanan)
    pajak=int(jumlah * 0.1)
    if JumlahPesanan >= 5:
        totaljumlah=int(jumlah+pajak)
    else:
        totaljumlah=int(jumlah+pajak)
    
if ListMenu == "7":
    namaMenu = " Air mata bang iqbal "
    hargaPerBarang=(50000)
    jumlah=(50000*JumlahPesanan)
    pajak=int(jumlah * 0.1)
    if JumlahPesanan >= 5: 
        totaljumlah=int(jumlah+pajak)
    else:
        menu=input(" Maaf nomor yang anda pilih tidak ada di menu")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("       Struk Pembelian       ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Nama Pelanggan      :",namaPelanggan)
print(" Nama Menu           :",namaMenu)
print(" Jumlah Pesanan      :",JumlahPesanan)
print(" Harga Perbarang     :","Rp.",hargaPerBarang)
print(" Jumlah              :","Rp.",jumlah)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Total               :","Rp.",totaljumlah)
Bayar=int(input(" Dibayar             : Rp. "))
Kembalian= (Bayar-totaljumlah)
print(" Kembali             :","Rp.",Kembalian)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Terima kasih atas pesanan anda ")
print(" Harga Termasuk PPN ")
