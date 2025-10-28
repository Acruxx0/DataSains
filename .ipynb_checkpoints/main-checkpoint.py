import pandas as pd
import numpy as np

def main():
    # Data awal calon TNI
    print("Data Calon TNI ===")
    data = {
        'nama': ['Andi', 'Budi', 'Citra', 'Dewi', 'Eka', 'Fajar', 'Gina', 'Hadi', 'Indah', 'Jilan'],
        'alamat': ['Jl. Merdeka No. 10', 'Jl. Sudirman No. 5', 'Jl. Thamrin No. 20', 
                  'Jl. Gatot Subroto No. 15', 'Jl. Rasuna Said No. 8', 'Jl. Kuningan No. 12',
                  'Jl. Cikini No. 3', 'Jl. Palmerah No. 7', 'Jl. Senayan No. 9', 'Jl. Kuningan No. 2'],
        'tinggi': [175, 178, 180, 180, 183, 185, 170, 168, 178, 160]
    }
    
    df = pd.DataFrame(data)
    print(df.to_string(index=False))
    print()
    
    # Statistik dasar tinggi badan
    print("=== Statistik Dasar Tinggi Badan ===")
    stats = df['tinggi'].describe()
    
    # Format stats sesuai output yang diinginkan
    stats_data = {
        'count': f"{stats['count']:.2f}",
        'mean': f"{stats['mean']:.2f}",
        'std': f"{stats['std']:.2f}",
        'min': f"{stats['min']:.2f}",
        '25%': f"{stats['25%']:.2f}",
        '50%': f"{stats['50%']:.2f}",
        '75%': f"{stats['75%']:.2f}",
        'max': f"{stats['max']:.2f}"
    }
    
    stats_series = pd.Series(stats_data)
    print(stats_series.to_string())
    print("Name: tinggi, dtype: float64")
    print()
    
    # Informasi tambahan
    print(f"Rata-rata tinggi : {stats['mean']:.2f} cm")
    print(f"Tertinggi    : {int(stats['max'])} cm")
    print(f"Terendah    : {int(stats['min'])} cm")
    print(f"Median    : {stats['50%']:.1f} cm")
    print("\n")

    # Calon di atas rata-rata tinggi
    print("=== Calon di atas rata-rata tinggi ===")
    rata_rata = stats['mean']
    di_atas_rata = df[df['tinggi'] > rata_rata].copy()
    # Reset index untuk menampilkan index seperti pada contoh
    di_atas_rata = di_atas_rata.reset_index(drop=True)
    print(di_atas_rata.to_string(index=False))
    print()
    
    # Urutan dari tertinggi ke terendah
    print("=== Urutan dari Tertinggi ke Terendah ===")
    df_sorted = df.sort_values('tinggi', ascending=False).copy()
    # Reset index untuk menampilkan index seperti pada contoh
    df_sorted = df_sorted.reset_index(drop=True)
    print(df_sorted.to_string(index=False))
    print("\n")

    # Data dengan kategori
    print("=== Data dengan Kategori ===")
    df_kategori = df.copy()
    
    # Menambahkan kolom kategori
    def kategori_tinggi(tinggi):
        if tinggi >= 180:
            return 'Tinggi'
        elif tinggi >= 170:
            return 'Sedang'
        else:
            return 'Pendek'
    
    df_kategori['kategori'] = df_kategori['tinggi'].apply(kategori_tinggi)
    print(df_kategori.to_string(index=False))
    print()
    
    # Jumlah per kategori
    print("=== Jumlah Calon per Kategori ===")
    count_kategori = df_kategori['kategori'].value_counts()
    print(count_kategori.to_string())
    print("Name: count, dtype: int64")
    print()
    
    # Statistik lanjutan
    print("=== Statistik Lanjutan ===")
    std_dev = df['tinggi'].std()
    variance = df['tinggi'].var()
    print(f"Standar Deviasi : {std_dev:.2f}")
    print(f"Variansi    : {variance:.2f}")
    print()
    
    # Calon dengan tinggi badan tertinggi
    print("=== Calon dengan Tinggi Badan Tertinggi ===")
    tertinggi = df.loc[df['tinggi'].idxmax()]
    print(f"Nama    : {tertinggi['nama']}")
    print(f"Alamat  : {tertinggi['alamat']}")
    print(f"Tinggi  : {int(tertinggi['tinggi'])} cm")

if __name__ == "__main__":
    main()