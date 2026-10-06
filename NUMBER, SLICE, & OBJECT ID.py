# ==========================================
# BAGIAN 4: NUMBER, SLICE, & OBJECT ID
# ==========================================
print("\n--- BAGIAN 4: NUMBER, SLICE, & OBJECT ID ---")
# Number & Pembulatan
import math
angka_float = 4.7
print("Floor:", math.floor(angka_float))
print("Ceil:", math.ceil(angka_float))
print("Round:", round(angka_float))

# Python Slice
data = [10, 20, 30, 40, 50, 60]
print("Slice [1:4]:", data[1:4])
print("Slice dari belakang [-2:]:", data[-2:])

# Object ID & Reference
a = [1, 2, 3]
b = a  # Menyalin referensi
c = a[:]  # Menyalin nilai (memori baru)
print("Apakah a adalah b?", a is b)
print("Apakah a adalah c?", a is c)