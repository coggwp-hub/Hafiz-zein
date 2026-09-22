
# A.10. PERULANGAN PYTHON -> WHILE


print("=== A.10.1. Keyword while ==")
# Contoh while dengan operasi logika / boolean
should_continue = True
# Simulasi input otomatis untuk contoh script (atau gunakan input interaktif)
# n = int(input("enter an even number greater than 0: "))

# Contoh while dengan counter dan increment
n_data = 6
i = 0
while i < n_data:
    print("number", i)
    i += 1

print("\n=== A.10.2. Perulangan while vs for ==")
# Perbandingan while vs for untuk kontrol angka
n_limit = 4
i = 0
print("Menggunakan while:")
while i < n_limit:
    print("number", i)
    i += 1

print("Menggunakan for:")
for i in range(n_limit):
    print("number", i)

print("\n=== A.10.3. Perulangan bercabang / nested while ==")
n_max = 4
i = 0
while i < n_max:
    j = 0
    while j < n_max - i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

print("\n=== A.10.4. Kombinasi while dan for ==")
n_combo = 3
for i in range(n_combo):
    j = 0
    while j < n_combo - i:
        print("*", end="")
        j += 1
    print()