# AIKIEA INVENTORY PROGRAM V.1.0 

#data admin inventory
admin_username = "admin"
admin_password = "admin1234"


# Define Database Barang dalam bentuk List yang berisi dictionary
database_barang = [
    {"kode": "BRG001", "nama": "Kursi", "kategori": "Furniture", "stok": 100},
    {"kode": "BRG002", "nama": "Meja", "kategori": "Furniture", "stok": 50},
    {"kode": "BRG003", "nama": "Lampu", "kategori": "Elektronik", "stok": 150},
    {"kode": "BRG004", "nama" : "Sofa", "kategori" : "Furniture", "stok":100},
    {"kode": "BRG005", "nama" : "Televisi", "kategori" : "Elektronik", "stok":20},
    {"kode" : "BRG006", "nama" : "AC ", "kategori" : "Elektronik", "stok" : 45},
    {"kode" : "BRG007", "nama" : "Lemari", "kategori" : "Furniture", "stok" : 20},
]

#define variable untuk menyimpan data transaksi atau aktivitas perubahan di sistem
transaksi_log = []


#function login ke sistem informasi inventory 
def login() : 
    print("SISTEM INFORMASI INVENTORY PT AIKIEA")
    print("\nSelamat datang di Sistem Informasi Inventory PT AIKIEA ")
    print("\nPastikan anda login dengan username dan password yang benar sebagai admin.")
    print("\n=============LOGIN ADMIN============")
    percobaan = 0
    #Perulangan dengan while untuk cek percobaan sebanyak 3 kali  
    while percobaan < 3 :
        username = input("Username : ")
        password = input("Password : ")

        if username == admin_username and password == admin_password : 
            print("Login Berhasil!")
            return True
        else : 
            percobaan += 1 
            print(f"username atau password salah. Anda telah mencoba {percobaan} kali." )
            if percobaan <3 : 
                print("Coba lagi!")
            else : 
                print("Anda telah mencoba 3 kali. Akses ditolak!")
                return False


#function untuk menampilkan menu 1 Menampilkan Data Inventory
def tampilkan_data_barang():
    print("------------------------------DAFTAR INVENTORY AIKIEA-------------------------------------")
    print("\n| Index\t | Kode Barang\t    | Nama Barang\t| Kategori Barang\t | Stok Barang\t  |")
    for i in range(len(database_barang)):
        print(
            f"| {i} \t | {database_barang[i]['kode']} \t    | {database_barang[i]['nama']}\t        | {database_barang[i]['kategori']}\t         | {database_barang[i]['stok']} \t          |"
        )


#function untuk menampilkan menu 2 lihat detail barang
def lihat_detail_barang():
    tampilkan_data_barang()
    try:
        index_to_view = int(input("Masukkan index barang untuk melihat detail barang: "))
        if 0 <= index_to_view < len(database_barang):
            barang = database_barang[index_to_view]
            print("\nDetail Barang:")
            print(f"Kode Barang   : {barang['kode']}")
            print(f"Nama Barang   : {barang['nama']}")
            print(f"Kategori      : {barang['kategori']}")
            print(f"Stok Tersedia : {barang['stok']}")
        else:
            print("Index tidak valid.")
    except Exception as e:
        print(e)
        print("Input tidak sesuai, harus berupa angka.")


#function untuk menampilkan menu 3 Tambah Barang
def tambah_barang():
    kode_baru = input("Masukkan kode barang baru: ")
    #cek apakah kode barang yang diinput sama dengan kode barang yang tersimpan di database
    for barang in database_barang:
        if barang["kode"] == kode_baru : 
            print(f"Kode barang '{kode_baru}' sudah ada")
            jumlah_tambah = int(input(f"Masukkan jumlah stok tambahan untuk kode barang '{barang['kode']}': "))
            # Jika kode barang sudah ada, maka akan otomatis menjalankan logic code di bawah untuk menambahkan stock atas kode barang tersebut
            barang["stok"] += jumlah_tambah
            transaksi_log.append(f"Transaksi tambah stock : {jumlah_tambah} untuk barang {barang['nama']} dengan kode barang {barang['kode']}.")
            print(f"Stok kode barang '{barang['kode']}' dengan nama barang '{barang['nama']}'berhasil diperbarui.")
            return

    nama_baru = input("Masukkan nama barang baru: ")
    #cek apakah nama barang yang diinput sama dengan nama barang yang tersimpan di database
    for barang in database_barang:
        if barang["nama"] == nama_baru:
            print(f"Nama barang '{nama_baru}' sudah ada.")
            jumlah_tambah = int(input(f"Masukkan jumlah stok tambahan untuk barang '{barang['nama']}': "))
            # Jika nama barang sudah ada, maka akan otomatis menjalankan logic code di bawah untuk menambahkan stock atas barang tersebut
            barang["stok"] += jumlah_tambah
            transaksi_log.append(f"Transaksi tambah stock : {jumlah_tambah} untuk barang {barang['nama']} dengan kode barang {barang['kode']}.")
            print(f"Stok barang '{barang['nama']}' dengan kode barang '{barang['kode']}' berhasil diperbarui.")
            return

    kategori_baru = input("Masukkan kategori barang: ")
    stok_baru = int(input("Masukkan jumlah stok awal: "))
    database_barang.append({
        "kode": kode_baru,
        "nama": nama_baru,
        "kategori": kategori_baru,
        "stok": stok_baru,
    })
    transaksi_log.append(f'Transaksi Tambah Barang dengan detail sebagai berikut \n Kode barang : {kode_baru} \n Nama barang : {nama_baru} \n Kategori : {kategori_baru} \n Stock : {stok_baru}')
    print(f"Barang '{nama_baru}' berhasil ditambahkan ke inventory.")


#Function untuk menampilkan menu 4 hapus barang
def hapus_barang():
    tampilkan_data_barang()
    try:
        index_to_delete = int(input("Masukkan index barang yang ingin dihapus: "))
        if 0 <= index_to_delete < len(database_barang):
            barang_dihapus = database_barang.pop(index_to_delete)
            transaksi_log.append(f"Transaksi Hapus Barang dengan detail sebagai berikut \n Kode barang : {barang_dihapus["kode"]} \n Nama barang : {barang_dihapus["nama"]} \n Kategori : {barang_dihapus["kategori"]} \n Stock : {barang_dihapus["stok"]}.")
            print(f"Barang '{barang_dihapus['nama']}' berhasil dihapus.")
        else:
            print("Index tidak valid.")
    except Exception as e :
        print(e)
        print("Input harus berupa angka.")


#Function untuk menampilkan menu 5 update stock 
def update_stok_barang():
    tampilkan_data_barang()
    try:
        index_to_update = int(input("Masukkan index barang yang ingin diperbarui: "))
        if 0 <= index_to_update < len(database_barang):
            barang = database_barang[index_to_update]
            print(f"Barang yang akan diperbarui: {barang['nama']}")
            stok_baru = int(input(f"Masukkan jumlah stok baru (stok saat ini: {barang['stok']}): "))
            perubahan = stok_baru - barang["stok"]
            barang["stok"] = stok_baru
            transaksi_log.append(f"Transaski update stock barang dengan detail sebagai berikut \n {perubahan} untuk barang {barang["nama"]} ({barang["kode"]}), Stok Baru: {stok_baru}")
            print(f"Stok barang '{barang['nama']}' berhasil diperbarui menjadi {stok_baru}.")
        else:
            print("Index tidak valid.")
    except Exception as e :
        print(e)
        print("Input harus berupa angka.")

#Function untuk melihat transaksi log
def lihat_transaksi_log():
    if transaksi_log:
        print("\nTransaksi Log:")
        for log in transaksi_log:
            print(log)
    else:
        print("Tidak ada transaksi yang tercatat.")


#Function yang berguna untuk menampilkan Halaman Utama pada Inventory Program
def main_menu():
    menu = 0
    while menu != 7:
        print("\nSelamat datang di Sistem Informasi Inventory PT AIKIEA")
        print("Berikut Menu yang ingin dijalankan :")
        print("1. Daftar Barang ")
        print("2. Lihat Detail Barang")
        print("3. Tambah Barang")
        print("4. Update Stok Barang")
        print("5. Hapus Barang")
        print("6. Log Transaksi")
        print("7. Logout")

        try:
            menu = int(input("Pilih menu dengan memasukkan angka 1-6 : "))
            if menu == 1:
                tampilkan_data_barang()
            elif menu == 2:
                lihat_detail_barang()
            elif menu == 3:
                tambah_barang()
            elif menu == 4:
                update_stok_barang()
            elif menu == 5:
                hapus_barang()
            elif menu == 6 :
                lihat_transaksi_log()
            elif menu == 7:
                print("Terima kasih telah menggunakan Sistem Inventory.")
            else:
                print("Pilihan tidak valid.")
        except Exception as e:
            print(e)
            print("Input harus berupa angka.")


#Menjalankan program utama Sistem Informasi Inventory
if login() : 
    main_menu()

