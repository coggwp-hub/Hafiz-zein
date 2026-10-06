# ==========================================
# BAGIAN 5: FUNCTION & ARGUMENT
# ==========================================
print("\n--- BAGIAN 5: FUNCTION ---")
# Definisi fungsi dengan type hinting dan default return
def hitung_luas_persegi_panjang(panjang: int, lebar: int) -> int:
    return panjang * lebar

# Positional Argument
hasil_pos = hitung_luas_persegi_panjang(5, 10)
print("Hasil Positional:", hasil_pos)

# Keyword Argument
hasil_kw = hitung_luas_persegi_panjang(lebar=4, panjang=5)
print("Hasil Keyword Argument:", hasil_kw)