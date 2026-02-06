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
    # Cek apakah ada data catatan
    if len(catatan) == 0:
        print("\n⚠️  Belum ada data catatan. Tambahkan catatan terlebih dahulu!")
    else:
        # Menghitung total waktu belajar
        total_menit = sum(item['durasi'] for item in catatan)
        
        # Konversi ke jam dan menit
        jam = total_menit // 60
        sisa_menit = total_menit % 60
        
        # Menampilkan total waktu dengan format rapi
        print("\n" + "="*60)
        print(" "*20 + "TOTAL WAKTU BELAJAR")
        print("="*60)
        
        print(f"\nTotal waktu belajar: {total_menit} menit")
        print(f"Atau: {jam} jam {sisa_menit} menit")
        
        # Menghitung total per mapel
        print("\n" + "-"*60)
        print("Breakdown per mapel:")
        print("-"*60)
        
        mapel_waktu = {}
        for item in catatan:
            if item['mapel'] in mapel_waktu:
                mapel_waktu[item['mapel']] += item['durasi']
            else:
                mapel_waktu[item['mapel']] = item['durasi']
        
        for mapel, waktu in mapel_waktu.items():
            jam_mapel = waktu // 60
            menit_mapel = waktu % 60
            print(f"  • {mapel}: {waktu} menit ({jam_mapel}j {menit_mapel}m)")

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

