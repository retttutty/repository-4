catatan = []
mapel_favorit = []  # List baru untuk menyimpan mapel favorit

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

def tambah_favorit():
    # Cek apakah ada data catatan
    if len(catatan) == 0:
        print("\n⚠️  Belum ada catatan belajar. Tambahkan catatan terlebih dahulu!")
        return
    
    # Mengumpulkan semua mapel yang unik dari catatan
    mapel_list = []
    for item in catatan:
        if item['mapel'] not in mapel_list:
            mapel_list.append(item['mapel'])
    
    # Tampilkan pilihan mapel
    print("\n" + "="*60)
    print("PILIH MAPEL FAVORIT")
    print("="*60)
    for nomor, mapel in enumerate(mapel_list, 1):
        status = "★" if mapel in mapel_favorit else " "
        print(f"{nomor}. {status} {mapel}")
    
    # Meminta input dari pengguna
    try:
        pilihan = int(input("\nNomor mapel yang ingin ditambahkan ke favorit (0 untuk batal): "))
        
        if pilihan == 0:
            print("Dibatalkan.")
            return
        
        if 1 <= pilihan <= len(mapel_list):
            mapel_dipilih = mapel_list[pilihan - 1]
            
            if mapel_dipilih in mapel_favorit:
                mapel_favorit.remove(mapel_dipilih)
                print(f"✓ {mapel_dipilih} dihapus dari favorit!")
            else:
                mapel_favorit.append(mapel_dipilih)
                print(f"✓ {mapel_dipilih} ditambahkan ke favorit!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("⚠️  Input harus berupa angka!")

def lihat_favorit():
    # Cek apakah ada mapel favorit
    if len(mapel_favorit) == 0:
        print("\n⚠️  Belum ada mapel favorit. Tambahkan mapel ke favorit terlebih dahulu!")
    else:
        # Menampilkan mapel favorit dengan statistik
        print("\n" + "="*60)
        print(" "*15 + "MAPEL FAVORIT & STATISTIK")
        print("="*60)
        
        for nomor, mapel_fav in enumerate(mapel_favorit, 1):
            # Hitung waktu belajar untuk mapel favorit
            waktu_mapel = sum(item['durasi'] for item in catatan if item['mapel'] == mapel_fav)
            jam_mapel = waktu_mapel // 60
            menit_mapel = waktu_mapel % 60
            
            # Hitung jumlah topik
            jumlah_topik = len([item for item in catatan if item['mapel'] == mapel_fav])
            
            print(f"\n{nomor}. ★ {mapel_fav}")
            print(f"   Total waktu : {waktu_mapel} menit ({jam_mapel}j {menit_mapel}m)")
            print(f"   Jumlah topik: {jumlah_topik} topik")
            print("-" * 60)

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("5. Kelola mapel favorit")
    print("6. Lihat mapel favorit")
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
    elif pilihan == "5":
        tambah_favorit()
    elif pilihan == "6":
        lihat_favorit()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")

