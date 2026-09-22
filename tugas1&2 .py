
# JAWABAN LATIHAN PERTEMUAN 3: OPERATOR & TIPE DATA PYTHON


print("--- 1. Precedence Operator (Perkalian didahulukan) ---")
print(5 + 3 * 4)  # Output: 17

print("\n--- 2. Penggunaan Tanda Kurung ---")
print((5 + 3) * 4)  # Output: 32

print("\n--- 3. Pembagian Biasa (Float Division) ---")
print(18 / 4)  # Output: 4.5

print("\n--- 4. Pembagian Bulat (Floor Division) ---")
print(18 // 4)  # Output: 4

print("\n--- 5. Sisa Bagi (Modulus) ---")
print(18 % 4)  # Output: 2

print("\n--- 6. Perpangkatan (Exponentiation) ---")
print(3 ** 4)  # Output: 81

print("\n--- 7. Kombinasi Operator Aritmatika ---")
print(10 + 2 * 3 - 4 / 2)  # Output: 14.0

print("\n--- 8. Operasi Variabel dengan Floor Division & Modulus ---")
a = 15
b = 4
print(a // b + a % b * 2)  # Output: 9

print("\n--- 9. Konversi Tipe Data (Type Casting) ---")
print(int("20") + float("3.5") * 2)  # Output: 27.0

print("\n--- 10. Perhitungan Luas (Integer x Float) ---")
panjang = 12
lebar = 5.5
print(panjang * lebar)  # Output: 66.0

print("\n--- 11. Perhitungan Diskon Harga ---")
harga = 200000
diskon = 0.1
print(harga - (harga * diskon))  # Output: 180000.0

print("\n--- 12. Pencarian Rata-rata dari List ---")
nilai = [85, 90, 78]
print(sum(nilai) / len(nilai))  # Output: 84.33333333333333