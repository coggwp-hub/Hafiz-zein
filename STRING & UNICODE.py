# ==========================================
# BAGIAN 3: STRING & UNICODE
# ==========================================
print("\n--- BAGIAN 3: STRING & UNICODE ---")
nama_depan = "Belajar"
nama_belakang = "Python"

# String Formatting (f-string)
pesan = f"Halo, {nama_depan} {nama_belakang}!"
print(pesan)

# Method String
teks = "  pemrograman python  "
print("Strip:", teks.strip())
print("Upper:", teks.strip().upper())
print("Split:", teks.strip().split(" "))

# Unicode & ASCII
print("Kode ASCII 'A':", ord('A'))
print("Karakter dari kode 65:", chr(65))