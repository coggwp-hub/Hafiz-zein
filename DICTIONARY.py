# ==========================================
# BAGIAN 2: DICTIONARY
# ==========================================
print("\n--- BAGIAN 2: DICTIONARY ---")
mahasiswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}

# Mengakses data
print("Nama:", mahasiswa["nama"])
print("Umur:", mahasiswa.get("umur"))

# Menambah/Mengubah data
mahasiswa["ipk"] = 3.75
mahasiswa.update({"umur": 21})
print("Dictionary baru:", mahasiswa)