
# A.11. PERULANGAN PYTHON -> BREAK, CONTINUE

print("=== A.11.1. Keyword break ==")
# Contoh simulasi break (dihentikan paksa saat kondisi tertentu)
angka_list = [9, 24, 11]  # simulasi input
for n in angka_list:
    if n % 3 != 0:
        break
    print("%d is divisible by 3" % (n))

print("\n=== A.11.2. Keyword continue ==")
# Contoh continue untuk skip iterasi
for i in range(10):
    if i < 3 or i > 7:
        continue
    print(i)

print("\n=== A.11.3. Label perulangan (Simulasi di Python) ==")
max_bintang = 5
outer_loop = True
for i in range(max_bintang):
    if not outer_loop:
        break
    for j in range(i + 1):
        print("*", end="")
        if j >= 7:
            outer_loop = False
            break
    print()