# 1. List (Akses dan manipulasi)
# Membuat List
List_Mie = ["Mie Gacoan", "Mie Seruit", "Level 0", "Level 3", "Level 5", "Level 7"]
print("=== LIST AWAL ===")
print(List_Mie)
print("-" * 30)
# Mengakses List
print("=== AKSES & SLICING ===")
print("Elemen Pertama   :", List_Mie[0])
print("Elemen Terakhir  :", List_Mie[-1])
# Slicing: [start:stop:step] -> mengambil indeks 0 sampai 5 dengan lompatan 2
print("Slicing [0:6:2]  :", List_Mie[0:6:2]) 
print("-" * 30)
# 3. Manipulasi List
print("=== MANIPULASI LIST ===")
# APPEND: Menambah ke akhir list
print(List_Mie)
List_Mie.append("Level 9")
print("Sesudah Append : ",List_Mie)
# INSERT : Menambah di posisi tertentu
List_Mie.insert(2,"Mie Aceh")
print("Sesudah Insert : ",List_Mie)
# EXTEND: Menggabungkan list lain
List_Mie.extend(["Bihun"])
print("Sesudah Extend : ",List_Mie)
# POP: Menghapus berdasarkan indeks
List_dibuang = List_Mie.pop(3) # Menghapus elemen di indeks 3
print("Sesudah pop : ", List_Mie, " (List yang dibuang:", List_dibuang, ")")
# REMOVE: Menghapus berdasarkan nilai
List_Mie.remove("Bihun")
print("Sesudah remove :", List_Mie)
print("-" * 30)

# 2. Membuat Tuple (immutability & unpacking)
data_pesanan = ("Mie Gacoan", "Level 3", "Es Gobak Sodor", 25000, "Meja 12")
print("=== TUPLE: DATA PESANAN ===")
print("Isi tuple : ", data_pesanan)
print("-" * 40)
# Menampilkan Panjang (len) & Akses Indeks
print("=== AKSES & PANJANG ===")
print("Panjang Tuple (len) :", len(data_pesanan))
print("Elemen Indeks ke-0  :", data_pesanan[0])
print("Elemen Indeks ke-2  :", data_pesanan[2])
print("-" * 40)
# Unpacking (Membongkar isi Tuple ke variabel)
print("=== UNPACKING ===")
menu, level, minuman, *biaya_dan_meja = data_pesanan
print("Variabel 1 (menu)    :", menu)
print("Variabel 2 (level)   :", level)
print("Variabel 3 (minuman) :", minuman)
print("Variabel *rest       :", biaya_dan_meja)
print("-" * 40)

# 3. Set (keunikan dan operasi himpunan)
set_mie = {"Mie Gacoan", "Mie Seruit", "Mie Gacoan", "Level 3", "Level 5", "Level 3"}
print("=== BUKTI DUPLIKAT OTOMATIS HILANG ===")
print("Data yang diinput: {'Mie Gacoan', 'Mie Seruit', 'Mie Gacoan', 'Level 3', 'Level 5', 'Level 3'}")
print("Hasil di Set    :", set_mie) 
# Perhatikan: Nama yang sama otomatis disaring jadi satu
print("-" * 50)
# Membuat dua set yang saling tumpang tindih (overlap)
set_A = {"Mie Gacoan", "Mie Seruit", "Mie Gacoan", "Level 3"}
set_B = {"Mie Gacoan", "Level 3", "Level 5", "Level 3"}
print("Set A:", set_A)
print("Set B:", set_B)
print("-" * 45)
# Operasi Himpunan
print("=== OPERASI HIMPUNAN ===")
# UNION (|): Menggabungkan semua
print("Union (|) :", set_A | set_B)
# # INTERSECTION (&): Hanya mengambil yang sama-sama ada
print("Intersection (&) :", set_A & set_B)
# DIFFERENCE (-): Isi A yang TIDAK ADA di B
print("Difference (A - B)      :", set_A - set_B)
# SYMMETRIC DIFFERENCE (^): Semua elemen KECUALI yang tumpang tindih
print("Symmetric Difference (^):", set_A ^ set_B)
print("-" * 45)

# 4. Dictionary – key/value dasar
# Membuat Dictionary data mahasiswa
data_mhs = {
    "nama": "Ali Ramadhan",
    "nim": "0622403422",
    "angkatan": 2022,
    "kota": "Palembang"
}
print("=== DICTIONARY AWAL ===")
print(data_mhs)
print("-" * 45)
# Operasi Dictionary
# TAMBAH key baru (misal: Jurusan)
data_mhs["jurusan"] = "Teknik Elektro"
#UBAH nilai key (misal: ubah kota)
data_mhs["kota"] = "Shenzen"
# HAPUS key (misal: hapus NIM)
del data_mhs["nim"]
print("=== SETELAH MANIPULASI ===")
print(data_mhs)
print("-" * 45)
# Menampilkan Keys, Values, dan Items
print("Daftar Label (keys) :", data_mhs.keys())
print("Daftar Isi (values) :", data_mhs.values())
print("Daftar Pasangan     :", data_mhs.items())
print("-" * 45)
# Iterasi menampilkan key: value
print("=== HASIL ITERASI ===")
for key, value in data_mhs.items():
    print(f"{key}: {value}")

# 5. Nested Structures (Struktur Bersarang)
# Buat list berisi 4 dictionary
daftar_buku = [
    {"judul": "Laut Bercerita", "penulis": "Leila S. Chudori", "Penerbit": "Gramedia Pustaka Utama", "tahun": 2017},
    {"judul": "11.11", "penulis": "Fiersa Besari", "Penerbit": "Media Kita", "tahun": 2018},
    {"judul": "Dikta dan Hukum", "penulis": "Dhia'an Farah", "Penerbit": "Asoka Aksara x Loveable", "tahun": 2021},
    {"judul": "Dia Angkasa", "penulis": "Nurul Dwi Astuti", "Penerbit": "Loveable", "tahun": 2021}
]
print("=== DAFTAR SEMUA JUDUL BUKU (LOOP) ===")
# menampilkan semua judul saja menggunakan loop
for buku in daftar_buku:
    print(f"Judul: {buku['judul']}")
print("-" * 40)
# Filter buku terbit >= tahun tertentu (misal: 2015)
# Menggunakan List Comprehension
tahun_minimal = 2020
buku_terbaru = [buku["judul"] for buku in daftar_buku if buku["tahun"] >= tahun_minimal]
print(f"=== BUKU TERBIT >= {tahun_minimal} (FILTERED) ===")
print(buku_terbaru)

# 6. Comprehension & utilitas
# LIST COMPREHENSION
angka = range(1, 21)
# List Genap
list_genap = [x for x in angka if x % 2 == 0]
# List Kuadrat
list_kuadrat = [x**2 for x in angka]
print("=== LIST COMPREHENSION ===")
print("List Genap : ", list_genap)
print("List Kuadrat : ", list_kuadrat)
print("-" * 50)
# DICT COMPREHENSION
# Mapping angka 1-20 menjadi "genap" atau "ganjil"
mapping_angka = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 21)}
print("=== DICT COMPREHENSION ===")
print("Mapping 1-20:", mapping_angka)
print("-" * 50)
# SET COMPREHENSION
kalimat = "Saya Sangat Suka Kamu Karna Cantik"
# Huruf unik (lowercase) dari kalimat, abaikan spasi
# .lower() untuk memastikan semua jadi huruf kecil, .isalpha() untuk mengambil huruf saja
huruf_unik = {char.lower() for char in kalimat if char.isalpha()}
print("=== SET COMPREHENSION ===")
print("Kalimat     :", kalimat)
print("Huruf Unik  :", huruf_unik)
print("-" * 50)

# Keanggotaan & pencarian sederhana
list_mie = ["Mie Gacoan", "Mie Seruit", "Mie Aceh", "Mie Ramen"]
set_mie = {"Mie Gacoan", "Mie Seruit", "Mie Aceh", "Mie Ramen"}
print("=== CEK KEANGGOTAAN (in) ===")
# Cek di List
cari = "Mie Aceh"
ada_di_list = cari in list_mie
print(f"Apakah '{cari}' ada di List? {ada_di_list}")
# Cek di Set
ada_di_set = "Mie Sedap" in set_mie
print(f"Apakah 'Mie Sedap' ada di Set? {ada_di_set}")
print("-" * 40)
print("=== MENCARI POSISI (index) ===")
# Hanya bisa di List
if "Mie Seruit" in list_mie:
    posisi = list_mie.index("Mie Seruit")
    print(f"'Mie Seruit' ditemukan pada indeks ke: {posisi}")
else:
    print("Item tidak ditemukan, tidak bisa cek index.")
if "Mie Bihun" in list_mie:
    posisi_1 = list_mie.index("Mie Bihun")
    print(f"'Mie Bihun' ditemukan pada indeks ke: {posisi_1}")
else:
    print("Item tidak ditemukan, tidak bisa cek index.")