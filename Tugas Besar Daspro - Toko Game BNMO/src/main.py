import argparse
import os


def clear():
    os.system("cls")

def splituser():
    global tuser
    i=0
    pemisah=0
    tuser=[["" for i in range(6)] for j in range(panjangcsv(fileusers))]
    with open(fileusers,'r') as f:
        for line in f:
            for row in line:
                if pemisah==0:
                    if row==";":
                        pemisah+=1
                    else:
                        tuser[i][0]+=row
                elif pemisah==1:
                    if row==";":
                        pemisah+=1
                    else:
                        tuser[i][1]+=row
                elif pemisah==2:
                    if row==";":
                        pemisah+=1
                    else:
                        tuser[i][2]+=row
                elif pemisah==3:
                    if row==";":
                        pemisah+=1
                    else:
                        tuser[i][3]+=row
                elif pemisah==4:
                    if row==";":
                        pemisah+=1
                    else:
                        tuser[i][4]+=row
                elif pemisah==5:
                    if row==";":
                        pemisah+=1
                    else:
                        tuser[i][5]+=row
            else:
                i+=1
                pemisah=0

def splitgame():
    global tgame
    pemisah=0
    i=0
    tgame=[["" for i in range(6)] for i in range(panjangcsv(filegame))]
    with open(filegame,"r") as f:
        for line in f:
            for row in line:
                if pemisah==0:
                    if row==";":
                        pemisah+=1
                    else:
                        tgame[i][0]+=row
                elif pemisah==1:
                    if row==";":
                        pemisah+=1
                    else:
                        tgame[i][1]+=row
                elif pemisah==2:
                    if row==";":
                        pemisah+=1
                    else:
                        tgame[i][2]+=row
                elif pemisah==3:
                    if row==";":
                        pemisah+=1
                    else:
                        tgame[i][3]+=row
                elif pemisah==4:
                    if row==";":
                        pemisah+=1
                    else:
                        tgame[i][4]+=row
                elif pemisah==5:
                    if row==";":
                        pemisah+=1
                    else:
                        tgame[i][5]+=row
            else:
                i+=1
                pemisah=0

def splitkepemilikan():
    global tkepemilikan
    pemisah=0
    i=0
    tkepemilikan=[["" for i in range(2)] for j in range(panjangcsv(filekepemilikan))]
    with open(filekepemilikan,"r") as f:
        for line in f:
            for row in line:
                if pemisah==0:
                    if row==";":
                        pemisah+=1
                    else:
                        tkepemilikan[i][0]+=row
                elif pemisah==1:
                    if row==";":
                        pemisah+=1
                    else:
                        tkepemilikan[i][1]+=row
            else:
                pemisah=0
                i+=1

def splitriwayat():
    global triwayat
    pemisah=0
    i=0
    triwayat=[["" for i in range(5)] for j in range(panjangcsv(fileriwayat))]
    with open(fileriwayat,"r") as f:
        for line in f:
            for row in line:
                if pemisah==0:
                    if row==";":
                        pemisah+=1
                    else:
                        triwayat[i][0]+=row
                elif pemisah==1:
                    if row==";":
                        pemisah+=1
                    else:
                        triwayat[i][1]+=row
                elif pemisah==2:
                    if row==";":
                        pemisah+=1
                    else:
                        triwayat[i][2]+=row
                elif pemisah==3:
                    if row==";":
                        pemisah+=1
                    else:
                        triwayat[i][3]+=row
                elif pemisah==4:
                    if row==";":
                        pemisah+=1
                    else:
                        triwayat[i][4]+=row
            else:
                i+=1
                pemisah=0

def riwayat():
    global tpengguna
    global triwayat
    global admin
    global loginn
    if loginn:
        if admin==False:
            cek=0
            a=1
            for i in range(panjangarray(triwayat)):
                if triwayat[i][3]==tpengguna[0]:
                    if cek==0:
                        print("Daftar game :")
                    print(f"{a}. {triwayat[i][0]} | {triwayat[i][1]} | {triwayat[i][2]} | {triwayat[i][4]}",end="")
                    a+=1
                    cek+=1
            else:
                if cek==0:
                    print("Maaf kamu tidak punya riwayat pembelian game.")  
        else:
            print("Hanya user")
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain \"login\"")                

    
def buy_game():
    global tuser
    global tgame
    global tkepemilikan
    global tpengguna
    global admin
    global loginn
    if loginn:
        if admin==False:
            stok=0
            harga=0
            idgame=input("Masukkan ID Game: ")
            saldo=int(tpengguna[5])
            punya=False
            i=0
            
            for i in range(panjangarray(tkepemilikan)):
                if tkepemilikan[i][0]==idgame:
                    if int(tkepemilikan[i][1])==int(tpengguna[0]):
                        punya=True
                        break
            else:
                punya=False
                        
                    
            for i in range(panjangarray(tgame)):
                if tgame[i][0]==idgame:
                    stok=int(tgame[i][5])
                    harga=int(tgame[i][4])
                    i=i
                    break
            else:
                print("Game ID tidak ditemukan!")
                return False
            
            
            if saldo>harga and stok>0 and punya==False:
                print(f"Game \"{tgame[i][1]}\" berhasil dibeli!")
                nambahkepemilikan(tkepemilikan,idgame)
                tpengguna[5]=str(saldo-harga)
                tgame[i][5]=str(stok-1)+"\n"
                nambahriwayat(triwayat,idgame)
                for i in range(panjangarray(tuser)):
                    if tuser[i][0]==tpengguna[0]:
                        tuser[i][5]=tpengguna[5]
            
            elif punya==True:
                print("Anda sudah memiliki game tersebut!")
            elif saldo<harga:
                print("Saldo anda tidak cukup untuk membeli game tersebut")
            elif stok==0:
                print("Stok tersebut sedang habis!")
        else:
            print("Hanya user")
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain \"login\"")
        
def list_game():
    global tgame
    global tkepemilikan
    global tpengguna
    global admin
    global loginn
    if loginn:
        if admin==False:
            cek=0
            print("Daftar game: ")
            a=1
            for i in range(1,panjangarray(tkepemilikan)):
                if int(tkepemilikan[i][1])==int(tpengguna[0]):
                    for j in range(panjangarray(tgame)):
                        if tgame[j][0]==tkepemilikan[i][0]:
                            print(f"{a}. {tgame[j][0]} | {tgame[j][1]} | {tgame[j][2]} | {tgame[j][3]} | {tgame[j][4]}")
                            a+=1
                            cek+=1

                            break
                
                else:
                    continue
            else:
                if cek==0:
                    print("Maaf, kamu belum memiliki game.")
        else:
            print("Hanya user")
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain \"login\"")
def inventory():
    global tinventory
    global tpengguna
    global tgame
    iinventory=0
    for i in range(1,panjangarray(tkepemilikan)):
        if int(tkepemilikan[i][1])==int(tpengguna[0]):
            for j in range(panjangarray(tgame)):
                if tgame[j][0]==tkepemilikan[i][0]:
                    iinventory+=1
    tinventory=[["" for i in range(5)] for j in range(iinventory)]
    a=0
    for i in range(1,panjangarray(tkepemilikan)):
        if int(tkepemilikan[i][1])==int(tpengguna[0]):
            for j in range(panjangarray(tgame)):
                if tgame[j][0]==tkepemilikan[i][0]:
                    tinventory[a][0]=tgame[j][0]
                    tinventory[a][1]=tgame[j][1]
                    tinventory[a][2]=tgame[j][2]
                    tinventory[a][3]=tgame[j][3]
                    tinventory[a][4]=tgame[j][4]
                    a+=1

    
def search_my_game():
    global admin
    global loginn
    if loginn:
        if admin==False:
            idgame=input("Masukkan ID Game: ")
            tahun=input("Masukkan Tahun Rilis Game: ")
            print("Daftar game pada inventory yang memenuhi kriteria:")
            cek=0
            if idgame!="" and tahun!="":
                for i in range(panjangarray(tinventory)):
                    if tinventory[i][0]==idgame and tinventory[i][3]==tahun:
                        print(f"{tinventory[i][0]} | {tinventory[i][1]} | {tinventory[i][4]} | {tinventory[i][2]} | {tinventory[i][3]}")
                        cek+=1
                else:
                    if cek==0:
                        print("Tidak ada game yang memenuhi kriteria!")

            elif idgame!="" and tahun=="":
                for i in range(panjangarray(tinventory)):
                    if tinventory[i][0]==idgame:
                        print(f"{tinventory[i][0]} | {tinventory[i][1]} | {tinventory[i][4]} | {tinventory[i][2]} | {tinventory[i][3]}")
                        cek+=1
                else:
                    if cek==0:
                        print("Tidak ada game yang memenuhi kriteria!")
            elif idgame=="" and tahun!="":
                for i in range(panjangarray(tinventory)):
                    if tinventory[i][3]==tahun:
                        print(f"{tinventory[i][0]} | {tinventory[i][1]} | {tinventory[i][4]} | {tinventory[i][2]} | {tinventory[i][3]}")
                        cek+=1
                else:
                    if cek==0:
                        print("Tidak ada game yang memenuhi kriteria!")
            elif idgame=="" and tahun =="":
                for i in range(panjangarray(tinventory)):
                    print(f"{tinventory[i][0]} | {tinventory[i][1]} | {tinventory[i][4]} | {tinventory[i][2]} | {tinventory[i][3]}")
        else:
            print("Hanya user")
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain \"login\"")

    


def login():
    global admin
    global tpengguna
    global tinventory
    global loginn
    global tuser
    username=input("Masukkan username: ")
    password=input("Masukkan password: ")
    for i in range(panjangarray(tuser)):
        if tuser[i][1]==username and tuser[i][3]==password:
            print(f"Halo {tuser[i][2]} selamat datang di Binomo!")
            tpengguna=[tuser[i][0],tuser[i][1],tuser[i][2],tuser[i][3],tuser[i][4],tuser[i][5]]
            if tuser[i][4]=="admin":
                admin=True
            else:
                admin=False
            inventory()
            loginn=True
            return True
    else:
        print("Username atau password tidak ditemukan atau salah")
    

def register():
    global tuser
    global admin
    global loginn
    if loginn:
        if admin:
            nama=input("Masukkan nama : ")
            username=input("Masukkan username: ")
            password=input("Masukkan password: ")
            for i in range(panjangarray(tuser)):
                if tuser[i][1]==username:
                    print(f"Username {username} sudah terpakai, silahkan menggunakan username yang lain")
                    return True
            else:
                nambahuser(tuser,nama,username,password)
                print(f"Username {username} telah berhasil register ke dalam Binomo! ")
           
        else:
            print("Bukan admin")
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain \"login\"")
def panjangarray(array):
    panjang=0
    for i in array:
        panjang+=1
    return panjang

def panjangcsv(csv):
    indeks=0
    with open(csv,"r") as f:
        for line in f:
            indeks+=1
    return indeks

def nambahuser(tuserr,nama,username,password):
    global tuser
    tbaru=[["" for i in range(6)] for j in range(panjangarray(tuserr)+1)]

    for j in range(panjangarray(tuserr)+1):
        for i in range(6):
            if j==panjangarray(tuserr):
                tbaru[j][0]=panjangarray(tuserr)
                tbaru[j][1]=username
                tbaru[j][2]=nama
                tbaru[j][3]=password
                tbaru[j][4]="user"
                tbaru[j][5]="0\n"
            else:
                tbaru[j][i]=tuserr[j][i]
        
    tuser=tbaru
    return tbaru

def nambahkepemilikan(tuserr,idgame):
    global tkepemilikan
    global tpengguna
    tbaru=[["" for i in range(2)] for j in range(panjangarray(tuserr)+1)]
    for j in range(panjangarray(tuserr)+1):
        for i in range(2):
            if j==panjangarray(tuserr):
                tbaru[j][0]=idgame
                tbaru[j][1]=tpengguna[0]+"\n"
            else:
                tbaru[j][i]=tuserr[j][i]
    tkepemilikan=tbaru
    return tbaru

def nambahriwayat(tuserr,idgame):
    global triwayat
    global tpengguna
    global tgame
    tbaru=[["" for i in range(5)] for j in range(panjangarray(tuserr)+1)]
    for j in range(panjangarray(tuserr)+1):
        for i in range(5):
            if j==panjangarray(tuserr):
                tbaru[j][0]=idgame
                for k in range(panjangarray(tgame)):
                    if tgame[k][0]==idgame:
                        tbaru[j][1]=tgame[k][1]
                        tbaru[j][2]=tgame[k][2]
                        tbaru[j][3]=tpengguna[0]
                        tbaru[j][4]="2022\n"
            else:
                tbaru[j][i]=tuserr[j][i]
    triwayat=tbaru
    return tbaru
                

def tambah_game():
    global tgame
    global admin
    global loginn
    if loginn:
        if admin:
            namagame=input("Masukkan Nama Game: ")
            kategori=input("Masukkan Kategori: ")
            tahun=input("Masukkan Tahun Rilis: ")
            harga=input("Masukkan Harga Game: ")
            stok=input("Masukkan Stok Awal: ")
            while namagame=="" or kategori=="" or tahun=="" or harga=="" or stok=="":
                print("Mohon masukkan semua informasi mengenai game agar disimpan di BNMO")
                namagame=input("Masukkan Nama Game: ")
                kategori=input("Masukkan Kategori: ")
                tahun=input("Masukkan Tahun Rilis: ")
                harga=input("Masukkan Harga Game: ")
                stok=input("Masukkan Stok Awal: ")

            tbaru=[["" for i in range(6)] for j in range(panjangarray(tgame)+1)]

            for j in range(panjangarray(tgame)+1):
                for i in range(6):
                    if j==panjangarray(tgame):
                            
                        tbaru[j][1]=namagame
                        tbaru[j][2]=kategori
                        tbaru[j][3]=tahun
                        tbaru[j][4]=harga
                        tbaru[j][5]=stok +"\n"

                    else: 
                        tbaru[j][i]=tgame[j][i]
            
            tgame=tbaru
            print(f"Selamat berhasil menambahkan game {tbaru[j][1]}")
        else:
            print("Bukan admin")
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain \"login\"")


def ubah_game():
    global tgame
    global admin
    global loginn
    if loginn:
        if admin:
            idgame=input("Masukkan ID Game: ")
            namagame=input("Masukkan Nama Game: ")
            kategori=input("Masukkan Kategori: ")
            tahun=input("Masukkan Tahun Rilis: ")
            harga=input("Masukkan Harga: ")
            
            for j in range(panjangarray(tgame)):
                if tgame[j][0]==idgame:
                    if namagame=="":
                        namagame=tgame[j][1]
                    if kategori=="":
                        kategori=tgame[j][2]
                    if tahun=="":
                        tahun=tgame[j][3]
                    if harga=="":
                        harga=tgame[j][4]
                    
                    tgame[j][1]=namagame
                    tgame[j][2]=kategori
                    tgame[j][3]=tahun
                    tgame[j][4]=harga
                    return True
            else:
                print("Game ID tidak ditemukan!")
        else:
            print("Bukan admin")
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain \"login\"")
    

def ubah_stok():
    global admin
    global tgame
    global loginn
    if loginn:
        if admin:
            idgame=input("Masukkan ID Game: ")
            jumlah=int(input("Masukkan Jumlah: "))
            for j in range(panjangarray(tgame)):
                if tgame[j][0]==idgame:
                    total=int(jumlah)+int(tgame[j][5])

                    if total>0 and jumlah<0:
                        tgame[j][5]=str(total)+"\n"
                        print(f"Stok game {tgame[j][1]} berhasil dikurangi. Stok sekarang {tgame[j][5]}",end="")
                    elif total>0 and jumlah>0:
                        tgame[j][5]=str(total)+"\n"
                        print(f"Stok game {tgame[j][1]} berhasil ditambah. Stok sekarang {tgame[j][5]}",end="")
                    elif total<0:
                        print(f"Stok game {tgame[j][1]} gagal dikurangi karena stok kurang. Stok sekarang {tgame[j][5]}",end="")
                    return True
            else:
                print("Tidak ada game dengan ID tersebut!")
        else:
            print("Bukan admin")
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain \"login\"")
            


def urutan(skema):
    global turut
    global tgame
    turut= [["" for i in range(6)] for j in  range(panjangarray(tgame))]
    for j in range (panjangarray(tgame)):
        for i in range(6):
            turut[j][i]=tgame[j][i]
    if skema=="tahun-" or skema=="tahun+":
        for i in range(1,panjangarray(turut)):
            for j in range(i+1,panjangarray(turut)):
                if turut[i][3]<turut[j][3]:
                    turut[i],turut[j]=turut[j],turut[i]

    elif skema=="harga-" or skema=="harga+":
        for i in range(1,panjangarray(turut)):
            for j in range(i+1,panjangarray(turut)):
                if int(turut[i][4])<int(turut[j][4]):
                    turut[i],turut[j]=turut[j],turut[i]
    
    elif skema=="":
        for i in range(1,panjangarray(turut)):
            turut[i]=turut[i]

def list_game_toko():
    global loginn
    if loginn:
        skema=input("Skema sorting: ")
        urutan(skema)
        if skema=="harga+" or "harga-":
            if skema=="harga-":
                a=1
                for i in range(1,panjangarray(tgame)):
                    print(f"{a}. | {turut[i][0]} | {turut[i][1]} | {turut[i][4]} | {turut[i][2]} | {turut[i][3]} | {turut[i][5]}",end="")
                    a+=1
            elif skema=="harga+":
                a=1
                for i in range(panjangarray(tgame)-1,0,-1):
                    print(f"{a}. | {turut[i][0]} | {turut[i][1]} | {turut[i][4]} | {turut[i][2]} | {turut[i][3]} | {turut[i][5]}",end="")
                    a+=1
            elif skema=="tahun-":
                a=1
                for i in range(1,panjangarray(tgame)):
                    print(f"{a}. | {turut[i][0]} | {turut[i][1]} | {turut[i][4]} | {turut[i][2]} | {turut[i][3]} | {turut[i][5]}",end="")
                    a+=1
            elif skema=="tahun+":
                a=1
                for i in range(panjangarray(tgame)-1,0,-1):
                    print(f"{a}. | {turut[i][0]} | {turut[i][1]} | {turut[i][4]} | {turut[i][2]} | {turut[i][3]} | {turut[i][5]}",end="")
                    a+=1
            elif skema=="":
                a=1
                for i in range(1,panjangarray(tgame)):
                    print(f"{a}. | {tgame[i][0]} | {tgame[i][1]} | {tgame[i][4]} | {tgame[i][2]} | {tgame[i][3]} | {tgame[i][5]}",end="")
                    a+=1
            else:
                print("Skema sorting tidak valid!")
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain \"login\"")


def topup():
    global admin
    global tuser
    global loginn
    if loginn:
        if admin:
            username=input("Masukkan username: ")
            saldo=int(input("Masukkan saldo: "))
            a=0
            total=0
            for i in range(panjangarray(tuser)):
                if tuser[i][1]==username:
                    total=int(tuser[i][5]) + saldo
                    a=i
                    break
            else:
                print(f"Username {username} tidak ditemukan")
                return False
            
            if total<0:
                print("Masukan tidak valid")
            else:
                print(f"Top up berhasil. Saldo {username} menjadi {total}")
                tuser[a][5]=str(total)


        else:
            print("Bukan admin")
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain \"login\"")
    



def search_game_at_store():
    global tgame
    global loginn
    if loginn:
        idgame=input("Masukkan ID Game: ")
        nama=input("Masukkan Nama Game: ")
        harga=input("Masukkan Harga Game: ")
        kategori=input("Masukkan Kategori Game: ")
        tahun=input("Masukkan Tahun Rilis Game: ")
        cek=0
        a=1
        for i in range(1,panjangarray(tgame)):
            if tgame[i][0]==idgame or idgame=="":
                if tgame[i][1]==nama or nama=="":
                    if tgame[i][4]==harga or harga=="":
                        if tgame[i][2]==kategori or kategori=="":
                            if tgame[i][3]==tahun or tahun=="":
                                print(f"{a}. | {tgame[i][0]} | {tgame[i][1]} | {tgame[i][4]} | {tgame[i][2]} | {tgame[i][3]} | {tgame[i][5]}",end="")
                                cek+=1
                                a+=1
        else:
            if cek==0:
                print("Tidak ada game yang memenuhi kriteria")
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain \"login\"")
        
def help():
    global admin
    global loginn
    if loginn:
        if admin:
            print("1. register - untuk melakukan registrasi user baru")
            print("2. login - untuk melakukan login ke dalam sistem")
            print("3. tambah_game - untuk menambah game yang dijual pada toko")
            print("4. list_game_toko - untuk melihat list game yang dijual pada toko")
            print("5. ubah_game - mengubah isi game ")
            print("6. search_game_at_store - mencari game pada toko berdasarkan kriteria tertentu")
            print("7. topup - Menambahkan atau mengurangi saldo kepada user ")
            print("8. help - memberi panduan terhadap penggunaan program")
        else:
            print("1. login - untuk melakukan login ke dalam sistem")
            print("2. list_game_toko - untuk melihat list game yang dijual pada toko")
            print("3. buy_game - untuk membeli game yang tersedia di toko")
            print("4. search_my_game - untuk mencari game yang dimiliki user")
            print("5. search_game_at_store - mencari game pada toko berdasarkan kriteria tertentu")
            print("6. riwayat - melihat riwayat tahun pembelian game user")
            print("7. help - memberi panduan terhadap penggunaan program")
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain \"login\"")

def selanjutnya():
    next=input()
    clear()
    if next=="login":
        login()
    elif next=="exit":
        exitt()
    elif next=="register":
        register()
    elif next=="tambah_game":
        tambah_game()
    elif next=="ubah_game":
        ubah_game()
    elif next=="ubah_stok":
        ubah_stok()
    elif next=="list_game_toko":
        list_game_toko()
    elif next=="buy_game":
        buy_game()
    elif next=="list_game":
        list_game()
    elif next=="search_my_game":
        search_my_game()
    elif next=="topup":
        topup()
    elif next=="riwayat":
        riwayat()
    elif next=="search_game_at_store":
        search_game_at_store()
    elif next=="help":
        help()
    elif next=="save":
        save()
    


def save():
    global tuser
    global tgame
    global triwayat
    global tkepemilikan
    directory=input("Masukkan nama folder penyimpanan: ")
    parent_dir=os.getcwd()
    path=os.path.join(parent_dir,directory)
    os.makedirs(path,exist_ok=True)
    pathuser=path+"/users.csv"
    pathgame=path+"/game.csv"
    pathkepemilikan=path+"/kepemilikan.csv"
    pathriwayat=path+"/riwayat.csv"
    if os.path.exists(pathuser):
        os.remove(pathuser)
    if os.path.exists(pathgame):
        os.remove(pathgame)
    if os.path.exists(pathkepemilikan):
        os.remove(pathkepemilikan)
    if os.path.exists(pathriwayat):
        os.remove(pathriwayat)

    with open(pathuser,"w") as fuser:
        for j in range(panjangarray(tuser)):
            for i in range(6):
                if i!=5:
                    fuser.write(str(tuser[j][i]))
                    fuser.write(";")
                else:
                    fuser.write(str(tuser[j][i]))
    with open(pathgame,"w") as fgame:
        for j in range(panjangarray(tgame)):
            for i in range(6):
                if i!=5:
                    fgame.write(str(tgame[j][i]))
                    fgame.write(";")
                else:
                    fgame.write(str(tgame[j][i]))
    with open(pathkepemilikan,"w") as fkepemilikan:
        for j in range(panjangarray(tkepemilikan)):
            for i in range(2):
                if i!=1:
                    fkepemilikan.write(str(tkepemilikan[j][i]))
                    fkepemilikan.write(";")
                else:
                    fkepemilikan.write(str(tkepemilikan[j][i]))
    with open(pathriwayat,"w") as friwayat:
        for j in range(panjangarray(triwayat)):
            for i in range(5):
                if i!=4:
                    friwayat.write(str(triwayat[j][i]))
                    friwayat.write(";")
                else:
                    friwayat.write(str(triwayat[j][i]))
    
    print(f"Data telah disimpan pada folder {directory}")
    
def exitt():
    keluar=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while keluar!="n" and keluar!="N" and keluar!="y" and keluar!="Y":
        keluar=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if keluar=="n" or keluar=="N":
        clear()
        exit()
    else:
        save()
        exit()

def load():
    global filegame
    global filekepemilikan
    global fileriwayat
    global fileusers
    parser= argparse.ArgumentParser(usage="python program_binomo.py <nama_folder>")
    parser.add_argument("folder_csv")
    args=parser.parse_args()
    cwd=os.getcwd()
    filecsv=os.path.join(cwd,args.folder_csv)
    filegame=filecsv+r"\game.csv"
    filekepemilikan=filecsv+r"\kepemilikan.csv"
    fileriwayat=filecsv+r"\riwayat.csv"
    fileusers=filecsv+r"\users.csv"
    ada=False
    for roots,dirs,files in os.walk(format(cwd)):
        for dirr in dirs:
            if args.folder_csv==dirr:
                
                ada=True
                break
    if ada:
        print("Loading...")
        print("Selamat datang di antarmuka \"Binomo\"")
    else:
        if args.folder_csv=="":
            print("Tidak ada nama folder yang diberikan!")
            print("Usage: python program_binomo.py <nama_folder>")
        else:
            print(f"Folder {args.folder_csv} tidak ditemukan")
            exit()


load()
admin=False
loginn=False
splitgame()
splituser()
splitkepemilikan()
splitriwayat()

while True:
    selanjutnya()