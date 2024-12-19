import matplotlib.pyplot as plt

# Data penjualan tahunan
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
penjualan = [15000, 18000, 17000, 20000, 22000, 24000, 23000, 25000, 21000, 22000, 24000, 30000]

# Membuat diagram batang
plt.figure(figsize=(10, 6))
plt.bar(bulan, penjualan, color="skyblue")

# Menambahkan judul dan label
plt.title("Diagram Penjualan Tahunan", fontsize=16)
plt.xlabel("Bulan", fontsize=12)
plt.ylabel("Penjualan (dalam ribuan)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Menampilkan diagram
plt.tight_layout()
plt.show()
