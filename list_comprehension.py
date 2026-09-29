# Contoh #1: Perkalian elemen dalam range
seq_1 = [i * 2 for i in range(5)]
print("Contoh 1:", seq_1)  # Output: [0, 2, 4, 6, 8]

# Contoh #2: Menggunakan kondisi if
seq_2 = [i for i in range(10) if i % 2 == 1]
print("Contoh 2:", seq_2)  # Output: [1, 3, 5, 7, 9]

# Contoh #3: Menggunakan ternary operator
seq_3 = [(i * (2 if i % 2 == 0 else 3)) for i in range(1, 10)]
print("Contoh 3:", seq_3)  # Output: [3, 4, 9, 8, 15, 12, 21, 16, 27]

# Contoh #4: Nested loops (Perulangan bersarang)
list_x = ["a", "b", "c"]
list_y = ["1", "2", "3"]
seq_4 = [x + y for x in list_x for y in list_y]
print("Contoh 4:", seq_4)

# Contoh #5: Transposed Matrix
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
transposed = [[row[i] for row in matrix] for i in range(4)]
print("Contoh 5 (Transposed Matrix):", transposed)
# Output: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]