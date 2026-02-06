catatan = []

def tambah_catatan():
    # Meminta input dari pengguna
    mapel = input("Masukkan nama mapel: ")
    topik = input("Masukkan topik yang dipelajari: ")
    durasi = input("Masukkan durasi belajar (menit): ")
    
    # Membuat dictionary untuk menyimpan satu catatan
    catatan_baru = {
        "mapel": mapel,      # Nama mata pelajaran
        "topik": topik,      # Topik yang dipelajari
        "durasi": int(durasi) # Waktu dalam menit (diubah ke angka)
    }
    
    # Menambahkan catatan ke dalam list
    catatan.append(catatan_baru)
    
    # Menampilkan pesan konfirmasi
    print(f"✓ Catatan '{topik}' untuk {mapel} berhasil ditambahkan!")


def lihat_catatan():
    pass

def total_waktu():
    pass

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")
