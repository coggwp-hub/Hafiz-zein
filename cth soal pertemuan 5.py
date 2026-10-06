# --- CONTOH KODE SET & FROZENSET ---
# Membuat Set (duplikat otomatis dihapus)
buah = {"apel", "mangga", "jeruk", "apel"} 
print("Set Buah:", buah)

# Menambah & Menghapus Elemen
buah.add("pisang")
buah.discard("jeruk") # Aman dari error jika item tidak ada
print("Setelah modifikasi:", buah)

# Operasi Himpunan
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union (Gabungan):", A | B)
print("Intersection (Irisan):", A & B)
print("Difference (Selisih A - B):", A - B)

# Frozenset
kota = frozenset(["Jakarta", "Bandung", "Surabaya"])
print("Frozenset:", kota)

# --- CONTOH KODE DICTIONARY ---
mahasiswa = {
    "nama": "Budi",
    "nim": "12345678",
    "jurusan": "Teknik Informatika"
}

# Mengakses data
print("Nama:", mahasiswa["nama"])
print("Gender:", mahasiswa.get("gender", "Tidak ditemukan")) # Mencegah KeyError

# Menambah & Mengubah data
mahasiswa["nama"] = "Budi Santoso"

# Iterasi Keys & Values
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

# --- CONTOH KODE STRING, UNICODE, & NUMBER ---
# String Formatting (F-string)
nama = "Ani"
umur = 20
print(f"Halo, nama saya {nama} dan umur saya {umur} tahun.")

# Unicode & Emoji
print("Unicode Emoji:", "\U0001F600")
print("Kode ASCII/Unicode dari 'A':", ord('A'))
print("Karakter dari kode 65:", chr(65))

# Bilangan dengan Berbagai Basis
print("Hex 0xFF:", 0xFF)       # 255
print("Oktal 0o17:", 0o17)     # 15
print("Biner 0b1010:", 0b1010) # 10

# --- CONTOH KODE SLICING & REFERENCE ---
# Slicing List
angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Indeks 2 s.d 6:", angka[2:7])
print("Step 2:", angka[0:10:2])
print("Reverse List:", angka[::-1])

# Object ID & Reference
a = [1, 2, 3]
b = a           # Mereferensikan objek yang sama
c = a[:]        # Membuat salinan objek baru via slicing

print("ID a:", id(a))
print("ID b:", id(b)) # Sama persis
print("ID c:", id(c)) # Berbeda
print("Apakah a is b?", a is b) # True
print("Apakah a is c?", a is c) # False

# --- CONTOH KODE FUNCTION ---
def hitung_luas_persegi_panjang(panjang: int, lebar: int = 5) -> int:
    """Menghitung luas persegi panjang dengan lebar default 5"""
    return panjang * lebar

# 1. Positional Argument
print("Luas 1:", hitung_luas_persegi_panjang(10, 4))

# 2. Optional Argument (memakai default lebar=5)
print("Luas 2:", hitung_luas_persegi_panjang(10))

# 3. Keyword Argument (posisi dibalik)
print("Luas 3:", hitung_luas_persegi_panjang(lebar=6, panjang=8))

