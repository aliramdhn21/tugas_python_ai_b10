# 1. Function
def greet(nama: str) -> str:
    return f"Halo, {nama}!"
# Fungsi Tambah (Penjumlahan)
def tambah(a: float, b: float = 0.0) -> float:
    return a + b
# Fungsi Rata-Rata (Menghitung rata-rata dari list)
def rata_rata(angka: list[float]) -> float:
    # Cek jika list kosong
    if not angka:
        return 0.0
        # Hitung rata-rata
    hasil = sum(angka) / len(angka)
        # Return dengan 2 angka di belakang koma (round)
    return round(hasil, 2)
# --- UJI COBA FUNGSI ---
print("=== TEST FUNCTION ===")
print(greet("Ali Rmdhn"))
print("Hasil Tambah (5 + 3.5) :", tambah(5, 3.5))
print("Hasil Tambah :", tambah(10)) # b otomatis jadi 0.0
list_nilai = [85.5, 90.0, 78.8, 92.4]
print("Rata-rata Nilai        :", rata_rata(list_nilai))
print("Rata-rata List Kosong  :", rata_rata([]))

# 2. Class
def rata_rata(angka: list[float]) -> float:
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)
# --- MEMBUAT CLASS STUDENT ---
class Student:
    # Atribut: Inisialisasi data awal
    def __init__(self, nama: str, nim: str, jurusan: str):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai = [89]
    # Method: Menambah satu nilai ke list
    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)
    # Method: Menghitung rata-rata pakai fungsi rata_rata
    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)
    # Method: Cek status kelulusan (Default threshold = 70.0)
    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"
    # Method Spesial: __str__ untuk tampilan ringkas
    def __str__(self):
        rata = self.rata_nilai()
        st = self.status()
        return f"Student(nama='{self.nama}', nim='{self.nim}', jurusan='{self.jurusan}', rata={rata}, status={st})"

# --- UJI COBA CLASS ---
print("=== TESTING CLASS STUDENT ===")
# Membuat objek mahasiswa baru
mhs = Student("M. Ali Ramadhan", "062240342211", "Teknik Elektro")
# Menambah nilai
mhs.tambah_nilai(80.0)
mhs.tambah_nilai(85.0)
mhs.tambah_nilai(79.5)
print(mhs)

# Demo
if __name__ == "__main__":
    # Tampilkan Header Functions
    print(f"{'='*10} FUNCTIONS {'='*10}")
    print(greet("Ali Ramadhan"))
    print(f"tambah(5, 7)    : {tambah(5, 7)}")
    print(f"tambah(10)      : {tambah(10, 25)}")
    print(f"rata_rata([80, 90, 100]) : {rata_rata([80, 90, 100])}")
    print(f"rata_rata([])   : {rata_rata([])}")
    print("\n") # Memberi jarak
# Tampilkan Header Class Student
    print(f"{'='*10} CLASS STUDENT {'='*10}")
    # Buat 2 objek mahasiswa
    mhs1 = Student("Ali Ramadhan", "062240342210", "Teknik Elektro")
    mhs2 = Student("Angkasa", "062240342046", "Teknik Informatika")
    # Menambahkan nilai mhs1
    mhs1.tambah_nilai(80.0)
    mhs1.tambah_nilai(90.0)
    mhs1.tambah_nilai(100.0)
    # Menambahkan nilai mhs2
    mhs2.tambah_nilai(60.0)
    mhs2.tambah_nilai(55.0)
    mhs2.tambah_nilai(65.5)
    print(mhs1)
    print(mhs2)
    # Cetak rata-rata dan status secara spesifik
    print(f"\nDetail {mhs1.nama}: Rata-rata {mhs1.rata_nilai()}, Status: {mhs1.status()}")
    print(f"Detail {mhs2.nama}: Rata-rata {mhs2.rata_nilai()}, Status: {mhs2.status()}")

    
