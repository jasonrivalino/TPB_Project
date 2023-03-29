#ProgramMesinATM
#Menejelaskan cara kerja dari mesin ATM

#KAMUS
#pin1,pin2=array
#money1,money2,money3=int
#trans=str
#dec=str
#reck=int
#name=str

#ALGORITMA
print("DATA BANK SEBELUM KEGIATAN TRANSAKSI") #pengguna bank memiliki data awal dari bank pusat
pin1=[0 for pin in range (0,6)] #data awal berupa pin 6 angka
print("Pin kosong:", pin1)
for pin in range (0,6):
    pin1[pin]=int(input("Masukkan angka pin ke-"+str(pin+1)+": "))
print("Pin awal yang anda miliki:",pin1)
money1=int(input("Masukkan jumlah saldo yang dimiliki dari bank: ")) #data awal berupa uang saldo yang dimiliki sebelumnya
print()
print("MULAI MELAKUKAN TRANSAKSI DI BANK") #sudah masuk pada proses transaksi di bank
pin2=[0 for pin in range (0,6)] 
print("Masukkan pin sebelum memulai kegiatan transaksi:", pin2) #mulai memasukkan pin sesuai dengan pin yang ditentukan pada awal
for pin in range (0,6):
    pin2[pin]=int(input("Masukkan angka pin ke-"+str(pin+1)+": "))
print("Pin yang dimasukkan:", pin2)
for pin in range (0,2): #range digunakan untuk membatasi perulangan yaitu hanya sebanyak 3x saja
    if pin2!=pin1: #jika pin yang dimasukkan tidak sama akan ada kondisi perulangan
        print("Pin yang anda masukkan salah, silahkan coba ulang") #mengulang mencoba memasukkan pin
        pin2=[0 for pin in range (0,6)]
        print("Masukkan pin sebelum memulai kegiatan transaksi:", pin2)
        for pin in range (0,6):
            pin2[pin]=int(input("Masukkan angka pin ke-"+str(pin+1)+": "))
        print("Pin yang dimasukkan:", pin2)
while pin2!=pin1: #jika sudah lebih dari 3x maka kartu akan diblokir 
    print("KARTU ANDA TELAH DIBLOKIR")
print()
print("Jenis-jenis transaksi:") #jika pin benar maka dilanjutkan dengan kondisonal transaksi
print("A) Mengambil uang dari rekening") #kondisi pertama mengambil uang
print("B) Melakukan transfer ke rekening lain") #kondisi kedua melakukan transfer
print("C) Melakukan pengecekan terhadap saldo") #kondisi ketiga mengecek saldo
trans=str(input("Ingin melakukan transaksi apa (Pilih A,B,C saja): "))
while trans!="A" and trans!="B" and trans!="C": 
    print("ERROR")
if trans == "A": #jika dipilih proses transaksi pertama (mengambil uang)
    money2=int(input("Masukkan jumlah uang yang ingin diambil: ")) #proses memasukkan jumlah uang yang ingin diambil
    dec=str(input("Apakah sudah benar?? ")) #memastikan apakah nilai uang yang dimasukkan sudah benar
    while dec=="TIDAK" or money2>money1 or money2%50000!=0: #disini uang yang bisa diambil hanya yang kelipatan 50000 saja
        if dec=="IYA" and money2>money1: #kondisi jika input uang sudah benar tetapi uang yang diambil melebihi saldo
            print("Maaf, saldo anda tidak mencukupi")
        elif dec=="IYA" and money2%50000!=0:#kondisi jika input uang sudah benar tetapi uang yang diambil bukan kelipatan 50000
            print("Maaf,uang yang anda masukkan tidak terdefinisi")
        money2=int(input("Masukkan jumlah uang yang ingin diambil: ")) #mengulangi memasukkan jumlah uang
        dec=str(input("Apakah sudah benar?? ")) #memastikan apakah nilai uang yang dimasukkan sudah benar
    while dec!="IYA" and dec!="TIDAK":
        print("ERROR")
    if dec=="IYA" and money1>=money2: #jika nilai uang yang dimasukkan sudah benar dan lebih kecil daripada saldo yang ada
        print("Mencetak uang sebesar",money2,"rupiah") #proses transaksi bisa dilakukan
        money1=money1-money2 #proses pengurangan uang pada saldo
        print("Sisa uang anda tinggal",money1,"rupiah") #sisa uang yang ada setelah transaksi
    else:    
        print("ERROR")
elif trans == "B": #jika dipilih proses transaksi kedua (melakukan transfer)
    reck=int(input("Masukkan nomor rekening yang dituju: ")) #memasukkan nomor rekening yang dituju
    name=str(input("Masukkan nama pemilik rekening: ")) #memasukkan nama pemilik rekening
    dec=str(input("Apakah sudah benar?? ")) #memastikan bahwa nomor dan nama pemilik rekening sudah benar
    while dec=="TIDAK" or reck<1000000000 or reck>9999999999: #nomor rekening hanya terdiri dari 10 angka saja
        if reck<1000000000 or reck>9999999999: #jika input no rekening lebih dari 10 angka
            print("Nomor rekening tidak terdefinisi")
        reck=int(input("Masukkan nomor rekening yang dituju: ")) #jika masih salah maka mengulangi proses input no rekening
        name=str(input("Masukkan nama pemilik rekening: ")) #memasukkan nama pemilik rekening
        dec=str(input("Apakah sudah benar?? ")) #memastikan bahwa nomor dan nama pemilik rekening sudah benar
    while dec!="IYA" and dec!="TIDAK": 
        print("ERROR")
    if dec=="IYA": #jika sudah benar maka masuk pada proses input jumlah uang yang ingin ditransfer
        money3=int(input("Masukkan nominal uang yang ingin ditransfer: ")) #memasukkan jumlah uang
        dec=input("Apakah sudah benar?? ") #memastikan apakah jumlah uang yang dimasukkan sudah benar
        while dec=="TIDAK"or money3>money1: #kondisional jika belum benar atau nilai uang yang dimasukkan melebihi saldo yang ada
            if dec=="IYA" and money3>money1: #jika nilai uang melebihi saldo
                print("Maaf, saldo anda tidak mencukupi")
            money3=int(input("Masukkan nominal uang yang ingin ditransfer: ")) #mengulangi proses input nilai uang
            dec=str(input("Apakah sudah benar?? ")) #memastikan apakah jumlah uang yang dimasukkan sudah benar
        while dec!="IYA" and dec!="TIDAK": 
            print("ERROR")
        if dec== "IYA" and money1>=money3:#jika nilai uang yang dimasukkan sudah benar dan lebih kecil daripada saldo
            print("Uang sejumlah",money3,"berhasil ditransfer kepada",name, "dengan nomor rekening",reck) #mencetak nilai uang yang ditransfer, nama penerima, dan nomor rekeningnya
            money1=money1-money3 #proses pengurangan uang pada saldo
            print("Sisa uang anda tinggal",money1,"rupiah") #sisa uang yang ada setelah transaksi
elif trans == "C": #jika dipilih proses transaksi ketiga (melakukan pengecekan saldo)
    print("Saldo anda tersisa",money1,"rupiah") #pengecekan saldo berdasarkan saldo awal (bisa berubah jika melakukan proses transaksi)
print()
final=str(input("Ingin melakukan transaksi lagi: ")) #kondisional ingin melakukan transaksi lagi atau tidak

while final == "IYA": #jika ingin melakukan transaksi lagi maka kembali ke kondisi awal (menginput pin lagi)
    pin2=[0 for pin in range (0,6)]
    print("Masukkan pin sebelum memulai kegiatan transaksi:", pin2)
    for pin in range (0,6):
        pin2[pin]=int(input("Masukkan angka pin ke-"+str(pin+1)+": "))
    print("Pin yang dimasukkan:", pin2)
    for pin in range (0,2):
        if pin2!=pin1:
            print("Pin yang anda masukkan salah, silahkan coba ulang")
            pin2=[0 for pin in range (0,6)]
            print("Masukkan pin sebelum memulai kegiatan transaksi:", pin2)
            for pin in range (0,6):
                pin2[pin]=int(input("Masukkan angka pin ke-"+str(pin+1)+": "))
            print("Pin yang dimasukkan:", pin2)
    while pin2!=pin1:
        print("KARTU ANDA TELAH DIBLOKIR")
    print()
    print("Jenis-jenis transaksi:")
    print("A) Mengambil uang dari rekening")
    print("B) Melakukan transfer ke rekening lain")
    print("C) Melakukan pengecekan terhadap saldo")
    trans=str(input("Ingin melakukan transaksi apa (Pilih A,B,C saja): "))
    while trans!="A" and trans!="B" and trans!="C":
        print("ERROR")
    if trans == "A":
        money2=int(input("Masukkan jumlah uang yang ingin diambil: "))
        dec=str(input("Apakah sudah benar?? "))
        while dec=="TIDAK" or money2>money1 or money2%50000!=0:
            if dec=="IYA" and money2>money1:
                print("Maaf, saldo anda tidak mencukupi")
            elif dec=="IYA" and money2%50000!=0:
                print("Maaf, uang yang anda masukkan tidak terdefinisi")
            money2=int(input("Masukkan jumlah uang yang ingin diambil: "))
            dec=str(input("Apakah sudah benar?? "))
        while dec!="IYA" and dec!="TIDAK":
            print("ERROR")
        if dec=="IYA" and money1>=money2:
            print("Mencetak uang sebesar",money2,"rupiah")
            money1=money1-money2
            print("Sisa uang anda tinggal",money1,"rupiah")
        else:    
            print("ERROR")
    elif trans == "B":
        reck=int(input("Masukkan nomor rekening yang dituju: "))
        name=str(input("Masukkan nama pemilik rekening: "))
        dec=str(input("Apakah sudah benar?? "))
        while dec=="TIDAK" or reck<1000000000 or reck>9999999999:
            if reck<1000000000 or reck>9999999999:
                print("NO REKENING TIDAK TERDEFINISI")
            reck=int(input("Masukkan nomor rekening yang dituju: "))
            name=str(input("Masukkan nama pemilik rekening: "))
            dec=str(input("Apakah sudah benar?? "))
        while dec!="IYA" and dec!="TIDAK":
            print("ERROR")
        if dec== "IYA":
            money3=int(input("Masukkan nominal uang yang ingin ditransfer: "))
            dec=input("Apakah sudah benar?? ")
            while dec=="TIDAK"or money3>money1:
                if dec=="IYA" and money3>money1:
                    print("Maaf, saldo anda tidak mencukupi")
                money3=int(input("Masukkan nominal uang yang ingin ditransfer: "))
                dec=str(input("Apakah sudah benar?? "))
            while dec!="IYA" and dec!="TIDAK":
                print("ERROR")
            if dec== "IYA" and money1>=money3:
                print("Uang sejumlah", money3, "berhasil ditransfer kepada",name, "dengan nomor rekening", reck)
                money1=money1-money3
                print("Sisa uang anda tinggal",money1,"rupiah")
    elif trans == "C":
        print("Saldo anda tersisa", money1, "rupiah")
    print()
    final=str(input("Ingin melakukan transaksi lagi: "))
if final == "TIDAK": #jika tidak, maka proses transaksi sudah berhenti
    print("Transaksi anda sudah selesai, silahkan mengambil kartu anda, terima kasih")
while final!="IYA" and final!="TIDAK":
    print("ERROR")