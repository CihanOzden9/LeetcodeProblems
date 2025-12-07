import numpy as np

def levenshtein_distance(w1, w2): # w1: Sütun (inovation), w2: Satır (execution)
    # Tablo boyutları (+1 ekliyoruz çünkü ilk satır/sütun boşluktur)
    cols = len(w1) + 1
    rows = len(w2) + 1

    # 1. NumPy ile sıfır matrisi oluştur (Syntax hatasını çözer)
    lev_table = np.zeros((rows, cols), dtype=int)

    # 2. İlk satır ve sütunu doldur (0, 1, 2, 3...)
    lev_table[:, 0] = np.arange(rows) # Sütun 0
    lev_table[0, :] = np.arange(cols) # Satır 0

    # 3. Tabloyu doldur
    for i in range(1, rows):         # Satırlar (execution)
        for j in range(1, cols):     # Sütunlar (inovation)
            
            # Harfler eşleşiyor mu? 
            if w2[i-1] == w1[j-1]:
                cost = 0
            else:
                cost = 1

            # Algoritma: Min(Üst+1, Sol+1, Çapraz+Cost)
            lev_table[i, j] = min(
                lev_table[i-1, j] + 1,      # Silme (Deletion)
                lev_table[i, j-1] + 1,      # Ekleme (Insertion)
                lev_table[i-1, j-1] + cost  # Değiştirme (Substitution)
            )

    print(lev_table) 
    return lev_table[rows-1, cols-1]

# Test
mesafe = levenshtein_distance("inovation", "execution")
print(f"Mesafe: {mesafe}")