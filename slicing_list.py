# --- 1. Mengakses Elemen via Index & Cek Keberadaan ---
list_1 = [10, 70, 20]
elem_1st = list_1[0]
elem_2nd = list_1[1]
elem_3rd = list_1[2]
print("Elemen:", elem_1st, elem_2nd, elem_3rd)

n = 70
if n in list_1:
  print(n, "is exists")
else:
  print(n, "is NOT exists")

# --- 2. Slicing & Mengubah Nilai Elemen ---
list_2 = ["ab", "cd", "hi", "ca"]
print("list_2 original:", list_2)

slice_1 = list_2[1:3]
print("slice_1 (index 1 sampai sebelum 3):", slice_1)

# Mengubah nilai elemen
list_2[1] = "zk"
list_2[2] = "sa"
print("list_2 after update:", list_2)

# --- 3. Append & Extend Element ---
# Append via method & slicing
list_1.append(88)
list_1[len(list_1) :] = [87]
print("list_1 after append:", list_1)

# Extend / Concat / Union
list_a = [10, 70, 20]
list_b = [88, 77]
# Cara 1: method extend()
# list_a.extend(list_b)
# Cara 2: slicing
# list_a[len(list_a):] = list_b
# Cara 3: operator +
list_c = list_a + list_b
print("Hasil extend/concat:", list_c)

# --- 4. Menyisipkan & Menghapus Elemen ---
list_3 = [10, 70, 20, 70]
list_3.insert(0, 15)  # Sisip di index 0
list_3.insert(2, 25)  # Sisip di index 2
print("list_3 after insert:", list_3)

list_3.remove(70)  # Menghapus nilai 70 pertama yang ditemukan
print("list_3 after remove(70):", list_3)

removed_item = list_3.pop(2)  # Menghapus & mengambil elemen index 2
print("list_3 after pop(2):", list_3)
print("Removed element:", removed_item)

# Menghapus dengan del dan slicing
del list_3[1]  # Hapus index 1
print("list_3 after del index 1:", list_3)

list_3 = [10, 70, 20, 70]
del list_3[1:3]  # Hapus range index 1 sampai sebelum 3
print("list_3 after del range [1:3]:", list_3)

# --- 5. Fungsi Lain: Len, Count, Index, Reverse, Sort, Copy ---
sample_list = [10, 70, 20, 70]
print("Total elemen (len):", len(sample_list))
print("Jumlah kemunculan 70 (count):", sample_list.count(70))

# Mencari index
idx = ["ab", "cd", "hi"].index("cd")
print("Index 'cd':", idx)

# Reverse & Sort
data_sort = [10, 70, 20]
data_sort.reverse()
print("Reversed:", data_sort)
data_sort.sort()
print("Sorted:", data_sort)

# Copy list (Shallow Copy)
copied_list = data_sort.copy()
# atau: copied_list = data_sort[:]
print("Copied list:", copied_list)

# Mengosongkan list
# data_sort.clear()
# data_sort[:] = []
# data_sort = []