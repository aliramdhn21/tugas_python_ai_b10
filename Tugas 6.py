import numpy as np
import pandas as pd
import os  # opsional

# Set seed untuk hasil random yang konsisten
np.random.seed(42)

# =======================
# NUMPY - DATA & STATISTIK
# =======================

# Buat array nilai ujian (10 data, random antara 50–100)
nilai = np.random.randint(50, 101, 10)

# Hitung statistik
rata_rata = np.mean(nilai)
median = np.median(nilai)
std_dev = np.std(nilai)
nilai_min = np.min(nilai)
nilai_max = np.max(nilai)

# Tampilkan hasil
print("=== NUMPY ===")
print("Data nilai:", nilai)
print("Rata-rata:", rata_rata)
print("Median:", median)
print("Standar Deviasi:", std_dev)
print("Nilai Minimum:", nilai_min)
print("Nilai Maksimum:", nilai_max)

# =======================
# PANDAS - DATAFRAME
# =======================

# Data mahasiswa (10 orang)
nama = [
    "Ali", "Valdi", "Citra", "Dewi", "Eka",
    "Fajar", "Gina", "Hadi", "Intan", "Baruna"
]

nim = [
    "1190782101", "1190782102", "1190782103", "1190782104", "1190782105",
    "1190782106", "1190782107", "1190782108", "1190782109", "1190782110"
]

# Gunakan semua nilai dari NumPy (10 data)
nilai_df = nilai

# Buat DataFrame
df = pd.DataFrame({
    "nama": nama,
    "nim": nim,
    "nilai": nilai_df
})

# Tambahkan kolom status
df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

# Tampilkan data
print("\n=== PANDAS ===")
print(df.head())

# =======================
# FILE I/O - SIMPAN KE TXT
# =======================

# Hitung ringkasan DataFrame
jumlah_data = len(df)
jumlah_lulus = (df["status"] == "LULUS").sum()
jumlah_tidak_lulus = (df["status"] == "TIDAK LULUS").sum()

# Tulis ke file
with open("ringkasan_tugas6.txt", "w") as file:
    file.write("=== RINGKASAN TUGAS ===\n\n")
    
    # Statistik NumPy
    file.write("Statistik Nilai (NumPy):\n")
    file.write(f"Rata-rata: {rata_rata}\n")
    file.write(f"Median: {median}\n")
    file.write(f"Standar Deviasi: {std_dev}\n")
    file.write(f"Nilai Minimum: {nilai_min}\n")
    file.write(f"Nilai Maksimum: {nilai_max}\n\n")
    
    # Ringkasan DataFrame
    file.write("Ringkasan Mahasiswa:\n")
    file.write(f"Jumlah Data: {jumlah_data}\n")
    file.write(f"Jumlah LULUS: {jumlah_lulus}\n")
    file.write(f"Jumlah TIDAK LULUS: {jumlah_tidak_lulus}\n")

print("\nFile 'ringkasan_tugas6.txt' berhasil dibuat!")

# =======================
# OOP - CLASS GRADEBOOK
# =======================

class GradeBook:
    def __init__(self, df):
        self.df = df

    def average(self):
        return self.df["nilai"].mean()

    def pass_rate(self, threshold=70.0):
        total = len(self.df)
        lulus = (self.df["nilai"] >= threshold).sum()
        return (lulus / total) * 100

    def save_summary(self, path):
        with open(path, "w") as file:
            file.write("=== SUMMARY DARI GRADEBOOK ===\n\n")
            file.write(f"Jumlah Data: {len(self.df)}\n")
            file.write(f"Rata-rata Nilai: {self.average()}\n")
            file.write(f"Persentase Lulus: {self.pass_rate()}%\n")

    def __str__(self):
        return f"GradeBook dengan {len(self.df)} data, rata-rata nilai = {self.average():.2f}"
    
    # =======================
# MAIN PROGRAM
# =======================

if __name__ == "__main__":
    print("\n=== OOP: GRADEBOOK ===")
    
    # Buat object
    gb = GradeBook(df)
    
    # Print object
    print(gb)
    
    # Panggil method
    print("Rata-rata nilai:", gb.average())
    print("Persentase lulus:", gb.pass_rate(), "%")
    
    # Simpan ke file
    gb.save_summary("summary_gradebook.txt")
    
    print("File 'summary_gradebook.txt' berhasil dibuat!")
