
# A.12. PYTHON LIST


print("=== A.12.1. Pengenalan list ==")
list_1 = [10, 70, 20]
list_2 = [
    'ab',
    'cd',
    'hi',
]
list_3 = [3.14, 'hello python', True, False]
list_4 = []

print("Element index ke-0 list_1:", list_1[0])
print("Element index ke-1 list_1:", list_1[1])
print("Element index ke-2 list_1:", list_1[2])

print("\n=== A.12.2. Perulangan list ==")
# Perulangan langsung
for e in list_1:
    print("elem:", e)

# Perulangan menggunakan index dan len()
for i in range(0, len(list_1)):
    print("index:", i, "elem:", list_1[i])

# Perulangan menggunakan enumerate()
for i, v in enumerate(list_1):
    print("index:", i, "elem:", v)

print("\n=== A.12.3. Nested list ==")
matrix = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0]
]
for row in matrix:
    for cell in row:
        print(cell, end="")
    print()

print("\n=== A.12.4. Fungsi list() ==")
# Konversi range ke list
range_1 = range(0, 10)
print(list(range_1))

range_2 = range(0, 22, 3)
print(list(range_2))

range_3 = range(100, 0, -10)
print(list(range_3))

# Konversi string ke list
alphabets = list('abcdefgh')
print(alphabets)

# Konversi tuple ke list
tuple_1 = (1, 2, 3, 4)
numbers_list = list(tuple_1)
print(numbers_list)