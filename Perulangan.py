
# A.9. PERULANGAN PYTHON -> FOR & RANGE

print("=== A.9.1. Keyword for dan fungsi range() ==")
for i in range(5):
    print("index:", i)

# Konversi range ke list menggunakan fungsi list()
r = range(5)
print("r:", list(r))

print("\n=== A.9.2. Penerapan fungsi range() ==")
# Ke-3 perulangan ini ekuivalen:
for i in range(3):
    print("index:", i)

for i in range(0, 3):
    print("index:", i)

# Contoh dengan start, stop, step
for i in range(2, 10, 2):
    print("index:", i)

# Contoh dengan decrement (step negatif)
for i in range(5, -5, -1):
    print("index:", i)

print("\n=== A.9.3. Iterasi element data kolektif ==")
# Iterasi list
messages = ["morning", "afternoon", "evening"]
for m in messages:
    print(m)

# Iterasi tuple
numbers = ("twenty four", 24)
for n in numbers:
    print(n)

# Iterasi string
for char in "hello python":
    print(char)

# Iterasi dictionary
bio = {
    "name": "toyota camry",
    "year": 1993,
}
for key in bio:
    print("key:", key, "value:", bio[key])

# Iterasi set
numbers_set = {"twenty four", 24}
for n in numbers_set:
    print(n)

print("\n=== A.9.4. Perulangan bercabang / nested for ==")
max_bintang = 3  # contoh langsung diset 3
for i in range(max_bintang):
    for j in range(0, max_bintang - i):
        print("*", end=" ")
    print()