# ==========================================
# 3. STRING: Mengakses & Eliminasi/Potong Elemen
# ==========================================
print("\n--- 3. STRING ---")
teks = "Halo Python"

# Cara Mengakses Elemen (berdasarkan Index)
print("Karakter pertama:", teks[0])
print("Karakter terakhir:", teks[-1])

# Mengeliminasi/Membuang bagian tertentu (Trimming / Replace)
kotor = "   Data Bersih   "
print("Hapus spasi (strip):", kotor.strip())  # Mengeliminasi spasi di awal & akhir
print("Ganti teks (replace):", teks.replace("Python", "Dunia")) # Mengeliminasi kata lama dengan baru