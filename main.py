from datetime import datetime, timedelta
import json
import os

catatan = []
mapel_favorit = []  # List untuk menyimpan mapel favorit
target_harian = {"tanggal": "", "target": 0}  # Dictionary untuk menyimpan target harian
NAMA_FILE = "study_log_data.json"  # Nama file untuk menyimpan data

def tambah_catatan():
    # Meminta input dari pengguna
    mapel = input("Masukkan nama mapel: ")
    topik = input("Masukkan topik yang dipelajari: ")
    durasi = input("Masukkan durasi belajar (menit): ")
    
    # Membuat dictionary untuk menyimpan satu catatan
    catatan_baru = {
        "mapel": mapel,      # Nama mata pelajaran
        "topik": topik,      # Topik yang dipelajari
        "durasi": int(durasi), # Waktu dalam menit (diubah ke angka)
        "tanggal": datetime.now().strftime("%Y-%m-%d") # Tanggal hari ini
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

def ringkasan_mingguan():
    # Cek apakah ada data catatan
    if len(catatan) == 0:
        print("\n⚠️  Belum ada catatan belajar. Tambahkan catatan terlebih dahulu!")
        return
    
    # Dapatkan tanggal hari ini dan awal minggu (Senin)
    hari_ini = datetime.now().date()
    awal_minggu = hari_ini - timedelta(days=hari_ini.weekday())
    akhir_minggu = awal_minggu + timedelta(days=6)
    
    # Filter catatan minggu ini
    catatan_minggu = []
    for item in catatan:
        tanggal_catatan = datetime.strptime(item['tanggal'], "%Y-%m-%d").date()
        if awal_minggu <= tanggal_catatan <= akhir_minggu:
            catatan_minggu.append(item)
    
    # Jika tidak ada catatan minggu ini
    if len(catatan_minggu) == 0:
        print(f"\n⚠️  Belum ada catatan belajar minggu ini ({awal_minggu} - {akhir_minggu})")
        return
    
    # Tampilkan ringkasan mingguan
    print("\n" + "="*60)
    print(" "*15 + "RINGKASAN BELAJAR MINGGUAN")
    print("="*60)
    print(f"Periode: {awal_minggu} sampai {akhir_minggu}")
    
    # Hitung total waktu minggu ini
    total_menit_minggu = sum(item['durasi'] for item in catatan_minggu)
    jam_minggu = total_menit_minggu // 60
    menit_minggu = total_menit_minggu % 60
    
    print(f"\nTotal waktu belajar: {total_menit_minggu} menit ({jam_minggu}j {menit_minggu}m)")
    
    # Breakdown per hari
    print("\n" + "-"*60)
    print("Breakdown per hari:")
    print("-"*60)
    
    nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    
    for i in range(7):
        tanggal = awal_minggu + timedelta(days=i)
        waktu_hari = sum(item['durasi'] for item in catatan_minggu if datetime.strptime(item['tanggal'], "%Y-%m-%d").date() == tanggal)
        
        if waktu_hari > 0:
            jam_hari = waktu_hari // 60
            menit_hari = waktu_hari % 60
            print(f"  {nama_hari[i]} ({tanggal}): {waktu_hari} menit ({jam_hari}j {menit_hari}m)")
        else:
            print(f"  {nama_hari[i]} ({tanggal}): - (tidak ada belajar)")
    
    # Breakdown per mapel minggu ini
    print("\n" + "-"*60)
    print("Breakdown per mapel:")
    print("-"*60)
    
    mapel_waktu = {}
    for item in catatan_minggu:
        if item['mapel'] in mapel_waktu:
            mapel_waktu[item['mapel']] += item['durasi']
        else:
            mapel_waktu[item['mapel']] = item['durasi']
    
    for mapel, waktu in mapel_waktu.items():
        jam_mapel = waktu // 60
        menit_mapel = waktu % 60
        print(f"  • {mapel}: {waktu} menit ({jam_mapel}j {menit_mapel}m)")

def filter_per_mapel():
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
    print("PILIH MAPEL UNTUK DIFILTER")
    print("="*60)
    for nomor, mapel in enumerate(mapel_list, 1):
        jumlah_catatan = len([item for item in catatan if item['mapel'] == mapel])
        print(f"{nomor}. {mapel} ({jumlah_catatan} catatan)")
    
    # Meminta input dari pengguna
    try:
        pilihan = int(input("\nNomor mapel yang ingin difilter (0 untuk batal): "))
        
        if pilihan == 0:
            print("Dibatalkan.")
            return
        
        if 1 <= pilihan <= len(mapel_list):
            mapel_dipilih = mapel_list[pilihan - 1]
            
            # Filter catatan sesuai mapel
            catatan_filter = [item for item in catatan if item['mapel'] == mapel_dipilih]
            
            # Hitung total waktu untuk mapel
            total_waktu_mapel = sum(item['durasi'] for item in catatan_filter)
            jam_mapel = total_waktu_mapel // 60
            menit_mapel = total_waktu_mapel % 60
            
            # Tampilkan hasil filter
            print("\n" + "="*60)
            print(f" "*15 + f"CATATAN {mapel_dipilih.upper()}")
            print("="*60)
            
            for nomor, item in enumerate(catatan_filter, 1):
                print(f"\n{nomor}. Tanggal : {item['tanggal']}")
                print(f"   Topik  : {item['topik']}")
                print(f"   Durasi : {item['durasi']} menit")
                print("-" * 60)
            
            print(f"\nTotal catatan: {len(catatan_filter)}")
            print(f"Total waktu belajar: {total_waktu_mapel} menit ({jam_mapel}j {menit_mapel}m)")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("⚠️  Input harus berupa angka!")

def set_target_harian():
    # Meminta input target usaha dari pengguna
    try:
        target = int(input("Masukkan target belajar harian (menit): "))
        
        if target <= 0:
            print("⚠️  Target harus berupa angka positif!")
            return
        
        # Simpan target untuk hari ini
        target_harian["tanggal"] = datetime.now().strftime("%Y-%m-%d")
        target_harian["target"] = target
        
        jam_target = target // 60
        menit_target = target % 60
        
        print(f"✓ Target harian berhasil diatur: {target} menit ({jam_target}j {menit_target}m)")
    except ValueError:
        print("⚠️  Input harus berupa angka!")

def lihat_progress_harian():
    # Cek apakah ada target hari ini
    tanggal_hari_ini = datetime.now().strftime("%Y-%m-%d")
    
    if target_harian["tanggal"] != tanggal_hari_ini or target_harian["target"] == 0:
        print("\n⚠️  Belum ada target harian untuk hari ini. Silahkan atur target terlebih dahulu!")
        return
    
    # Hitung waktu belajar hari ini
    waktu_hari_ini = sum(item['durasi'] for item in catatan if item['tanggal'] == tanggal_hari_ini)
    target = target_harian["target"]
    
    # Hitung persentase progress
    persentase = (waktu_hari_ini / target) * 100 if target > 0 else 0
    kekurangan = max(0, target - waktu_hari_ini)
    
    # Tampilkan progress harian
    print("\n" + "="*60)
    print(" "*18 + "PROGRESS HARIAN")
    print("="*60)
    print(f"Tanggal: {tanggal_hari_ini}")
    
    # Target
    jam_target = target // 60
    menit_target = target % 60
    print(f"\nTarget belajar: {target} menit ({jam_target}j {menit_target}m)")
    
    # Waktu actual
    jam_aktual = waktu_hari_ini // 60
    menit_aktual = waktu_hari_ini % 60
    print(f"Sudah belajar : {waktu_hari_ini} menit ({jam_aktual}j {menit_aktual}m)")
    
    # Progress bar
    panjang_bar = 40
    filled = int(panjang_bar * min(persentase / 100, 1))
    bar = "█" * filled + "░" * (panjang_bar - filled)
    print(f"\nProgress     : [{bar}] {persentase:.1f}%")
    
    # Status
    print("\n" + "-"*60)
    if waktu_hari_ini >= target:
        jam_lebih = (waktu_hari_ini - target) // 60
        menit_lebih = (waktu_hari_ini - target) % 60
        print(f"🎉 SELAMAT! Anda sudah mencapai target!")
        print(f"Bonus: {waktu_hari_ini - target} menit ({jam_lebih}j {menit_lebih}m) lebih dari target")
    else:
        jam_kurang = kekurangan // 60
        menit_kurang = kekurangan % 60
        print(f"📝 Masih kurang: {kekurangan} menit ({jam_kurang}j {menit_kurang}m)")
        print(f"Tetap semangat! Lanjutkan belajar untuk mencapai target hari ini.")

def simpan_file():
    # Menyimpan semua data ke file JSON
    try:
        data = {
            "catatan": catatan,
            "mapel_favorit": mapel_favorit,
            "target_harian": target_harian
        }
        
        with open(NAMA_FILE, "w") as file:
            json.dump(data, file, indent=4)
        
        print(f"✓ Data berhasil disimpan ke file '{NAMA_FILE}'!")
    except Exception as e:
        print(f"⚠️  Gagal menyimpan data: {str(e)}")

def muat_file():
    # Memuat data dari file JSON
    global catatan, mapel_favorit, target_harian
    
    try:
        if os.path.exists(NAMA_FILE):
            with open(NAMA_FILE, "r") as file:
                data = json.load(file)
                catatan = data.get("catatan", [])
                mapel_favorit = data.get("mapel_favorit", [])
                target_harian = data.get("target_harian", {"tanggal": "", "target": 0})
            
            print(f"✓ Data berhasil dimuat dari file '{NAMA_FILE}'!")
            print(f"  - Catatan: {len(catatan)} data")
            print(f"  - Mapel favorit: {len(mapel_favorit)} mapel")
        else:
            print(f"ℹ️  File '{NAMA_FILE}' tidak ditemukan. Mulai dengan data baru.")
    except Exception as e:
        print(f"⚠️  Gagal memuat data: {str(e)}")
        print("ℹ️  Program akan dimulai dengan data kosong.")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("5. Kelola mapel favorit")
    print("6. Lihat mapel favorit")
    print("7. Ringkasan mingguan")
    print("8. Filter catatan per mapel")
    print("9. Atur target harian")
    print("10. Lihat progress harian")
    print("11. Simpan data ke file")
    print("4. Keluar")

# Auto-load data saat program dimulai
print("="*60)
print(" "*15 + "Selamat datang di Study Log App")
print("="*60)
muat_file()
print()

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
    elif pilihan == "7":
        ringkasan_mingguan()
    elif pilihan == "8":
        filter_per_mapel()
    elif pilihan == "9":
        set_target_harian()
    elif pilihan == "10":
        lihat_progress_harian()
    elif pilihan == "11":
        simpan_file()
    elif pilihan == "4":
        print("\nℹ️  Menyimpan data sebelum keluar...")
        simpan_file()
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")

