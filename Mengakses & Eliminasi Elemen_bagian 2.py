# ==========================================
# 2. DICTIONARY: Mengakses & Eliminasi Elemen
# ==========================================
print("\n--- 2. DICTIONARY ---")
mhs = {"nama": "Ani", "umur": 20, "jurusan": "TI"}

# Cara Mengakses Elemen
print("Akses pakai key:", mhs["nama"])
print("Akses pakai get():", mhs.get("umur"))
print("Akses semua keys:", mhs.keys())
print("Akses semua values:", mhs.values())

# Cara Eliminasi/Hapus Elemen
mhs.pop("jurusan")     # Menghapus key-value berdasarkan key tertentu
del mhs["umur"]        # Menghapus key-value menggunakan keyword 'del'
print("Dictionary setelah eliminasi:", mhs)