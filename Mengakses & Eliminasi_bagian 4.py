# ==========================================
# 4. LIST/SEQUENCE (SLICE & INDEX): Mengakses & Eliminasi
# ==========================================
print("\n--- 4. LIST / SLICE ---")
angka = [100, 200, 300, 400, 500]

# Cara Mengakses Elemen & Slice
print("Akses index ke-2:", angka[2])
print("Akses slice [1:4]:", angka[1:4])  # Mengakses sekumpulan elemen

# Cara Eliminasi/Hapus Elemen pada List
angka.remove(300)      # Menghapus berdasarkan nilai elemennya
item_terakhir = angka.pop()  # Menghapus elemen terakhir dan mengambil nilainya
del angka[0]           # Menghapus berdasarkan index
print("List setelah eliminasi:", angka)