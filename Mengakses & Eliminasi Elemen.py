# ==========================================
# 1. SET: Mengakses & Eliminasi Elemen
# ==========================================
print("--- 1. SET ---")
my_set = {10, 20, 30, 40}

# Cara Mengakses (karena tidak ada index, harus pakai perulangan/loop atau keyword 'in')
for item in my_set:
    print("Akses elemen set:", item)
print("Apakah 20 ada di set?", 20 in my_set)

# Cara Eliminasi/Hapus Elemen
my_set.remove(10)      # Menghapus elemen (error jika tidak ditemukan)
my_set.discard(99)     # Menghapus elemen (TIDAK error jika tidak ditemukan)
val = my_set.pop()     # Menghapus elemen secara acak dan mengambil nilainya
print("Set setelah eliminasi:", my_set)