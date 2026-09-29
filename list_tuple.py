# --- 1. Deklarasi & Akses Tuple ---
tuple_1 = (2, 3, 4, "hello python", False)
print("Data tuple_1:", tuple_1)
print("Total elemen:", len(tuple_1))
print("Elemen index 0:", tuple_1[0])

# --- 2. Perulangan Tuple & Enumerate ---
tuple_2 = ("ultra instinc shaggy", "nightwing", "noob saibot")

print("\n--- Perulangan Standar ---")
for t in tuple_2:
  print(t)

print("\n--- Perulangan dengan Enumerate ---")
for i, v in enumerate(tuple_2):
  print(f"index: {i}, elem: {v}")

# Cek keberadaan elemen dengan 'in'
if 70 in (10, 70, 20):
  print("\n70 ada di dalam tuple")

# --- 3. Nested Tuple ---
tuple_nested = ((0, 2), (0, 3), (2, 2), (2, 4))
print("\n--- Nested Tuple ---")
for row in tuple_nested:
  for cell in row:
    print(cell, end=" ")
  print()

# --- 4. Konversi Tipe Data dengan fungsi tuple() ---
alphabets = tuple("abcdefgh")
numbers = tuple([2, 3, 4, 5])
rtuple = tuple(range(0, 3))
print("\nKonversi string ke tuple:", alphabets)
print("Konversi list ke tuple:", numbers)
print("Konversi range ke tuple:", rtuple)

# --- 5. Tuple Packing & Unpacking ---
# Packing
first_name = "aerith gainsborough"
rank = 11
win = False
row_data = first_name, rank, win  # Bisa tanpa tanda kurung ()
print("\nHasil Packing:", row_data)

# Unpacking
f_name, rnk, wn = row_data
print(f"Hasil Unpacking -> Nama: {f_name}, Rank: {rnk}, Win: {wn}")

# --- 6. Kombinasi List & Tuple (Data Kompleks / Kosong) ---
data = [
    ("ultra instinc shaggy", 1, True, ("detective", "saiyan")),
    ("nightwing", 3, True, ("teen titans", "bat family")),
    ("kucing meong", 7, False, ()),  # Menggunakan tuple kosong ()
]

# Append tuple baru ke list
data.append(("tifa lockhart", 2, True, ("avalanche",)))

print("\n--- Kombinasi List & Tuple ---")
print(f"{'name':<22} | {'rank'} | {'win'} | {'affiliation'}")
print("-" * 55)
for row in data:
  print(
      f"{row[0]:<22} | {row[1]:<4} | {str(row[2]):<5} |"
      f" {', '.join(row[3]) if row[3] else '-'}"
  )