# 1. Variabel dan Tipe Data 
Nama = "M. Ali Ramadhan"  
Umur = "21 Tahun"           # String
A = 55
B = 100                     # Integer
C = 35.15
D = 60.5                    # Float
Cowok = True
Cewek = False            # Boolean
Hobi = ["Joging", "Menonton Dracin", "Main ML", "Belajar", "Membantu Orang Tua"] # List (5 item)

# 2. Manipulasi String
intro = "halo perkenalkan saya " + Nama ,"Saya berumur " + Umur
print(intro)
print("Nama (UPPER):", Nama.upper())
print("Nama (lower):", Nama.lower())
print("Jumlah Karakter Nama dan Umur:", len(Nama + Umur))
print("-" * 25)

# 3. Operasi Matematika (+ - * / // %)
print("--- Operasi Matematika ---")
print("A = ",A)
print("B = ",B)
print("C = ",C)
print("D = ",D)
# Penjumlahan
print("--- Penjumlahan (+) ---")
print("Penjumlahan A + B :" ,A + B)
print("Penjumlahan C + D :" ,C + D)
print("Penjumlahan A + B + C + D :" ,A + B + C + D)
# Penngurangan
print("--- Pengurangan (-) ---")
print("Pengurangan A - B :" , A - B)
print("Pengurangan C - D :" , C - D)
print("Pengurangan A - B - C:" , A - B - C)
print("Pengurangan A - B -- C - D:" , A - B - C - D)
# Perkalian
print("--- Perkalian (*) ---")
print("Perkalian A * B :" , A * B)
print("Perkalian C * D :" , C * D)
print("Perkalian A * B * C:" , A * B * C)
print("Perkalian A * B * C * D:" , A * B * C * D)
# Pembagian
print("--- Pembagian (/) dan Pembagian bulat (//) ---")
print("Pembagian A / B :" , A / B)
print("Pembagian A / B :" , A / D)
print("Pembagian Bulat A // C :" , A // C)
print("Pembagian Bulat C // D :" , C // D)
# Sisa Bagi
print("--- Sisa Bagi (%) ---")
print("Pembagian A % B :" , A % B)
print("Pembagian C % D :" , C % D)
print("Pembagian A % B % D :" , A % B % D)
print("-" * 25)

# 4. List Hobi 
print("--- List Hobi ---")
print("Hobi :", Hobi)
print("Yang sering dilakukan:", Hobi[1], "dan", Hobi[3])
# Menambahkan Hobi Baru
Hobi.append("Berenang")
print("Setelah Hobi Ditambahkan :", Hobi)
# Menghapus Hobi Lama
Hobi.remove("Main ML")
print("Setelah Hobi Dihapus :", Hobi)

# 5.Penggunaan Input Dari User
print("--- Input User ---")
nama_user = input("Masukkan nama Anda: ")
umur_user = input("Masukkan umur Anda: ")
hobi_user = input("Masukkan hobi Anda: ")
print(f"Halo, nama saya {nama_user} umur saya {umur_user} tahun dan hobi saya {hobi_user}")