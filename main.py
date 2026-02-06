catatan = [
    {
        "mapel": "Matematika",
        "topik": "Persamaan Kuadrat",
        "durasi": 45
    },
    {
        "mapel": "Fisika",
        "topik": "Kinematika",
        "durasi": 60
    }
]

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
    # Cek apakah ada data catatan
    if len(catatan) == 0:
        print("⚠️  Belum ada catatan belajar. Mulai tambahkan catatan Anda!")
    else:
        # Menampilkan semua catatan dengan format rapi
        print("\n" + "="*60)
        print(" "*20 + "DAFTAR CATATAN BELAJAR")
        print("="*60)
        
        # Loop untuk menampilkan setiap catatan
        for nomor, item in enumerate(catatan, 1):
            print(f"\n{nomor}. Mapel    : {item['mapel']}")
            print(f"   Topik    : {item['topik']}")
            print(f"   Durasi   : {item['durasi']} menit")
            print("-" * 60)
        
        print(f"\nTotal catatan: {len(catatan)}")

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
