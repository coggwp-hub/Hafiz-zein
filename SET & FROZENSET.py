print("--- BAGIAN 1: SET & FROZENSET ---")
# Set kosong
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(2)  # Duplikat akan diabaikan
print("Set:", my_set)

# Operasi Himpunan
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)

# Frozenset (Immutable set)
my_frozen = frozenset([1, 2, 3])
print("Frozenset:", my_frozen)