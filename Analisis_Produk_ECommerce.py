from datetime import date, datetime
from tabulate import tabulate
class Produk:
    def __init__(self, nama_produk, kategori, harga, stok, rating, jumlah_terjual):
        self.nama_produk = nama_produk
        self.kategori = kategori
        self.harga = harga
        self.stok = stok
        self.rating = rating
        self.jumlah_terjual = jumlah_terjual

    def pendapatan(self):
        pendapatan = self.harga * self.jumlah_terjual
        return pendapatan

    def sisa_stok(self):
        return self.stok - self.jumlah_terjual
    
    def rating_produk(self):
        if isinstance(self.rating, str):
            rtg = int(self.rating)

        else:
            rtg = self.rating

        if rtg < 3:
            return "Perlu Perbaikan"

        elif rtg>=3 and rtg <=4:
            return "Baik"

        else:
            return "Sangat Baik"

class Electronic(Produk):
    stok_total = 0
    def __init__(self, nama_produk, harga, stok, rating, jumlah_terjual=0):
        super().__init__(nama_produk, "Electronics", harga, stok, rating, jumlah_terjual)
            
        Electronic.stok_total += stok

        if Electronic.stok_total > 50:
            self.harga *= 0.85

        Electronic.stok_total -= self.jumlah_terjual

class Fashion(Produk):
    def __init__(self, nama_produk, harga, stok, rating, jumlah_terjual=0, promo=False):
        super().__init__(nama_produk, "Fashion", harga, stok, rating, jumlah_terjual)
        self.promo = promo

    def sisa_stok(self):
        if self.promo:
            return self.stok - self.jumlah_terjual * 2
        else:
            return self.stok - self.jumlah_terjual

    def pendapatan(self):
        return self.harga * self.jumlah_terjual

class Food(Produk):
    def __init__(self, nama_produk, harga, stok, rating, jumlah_terjual, tanggal_kadaluarsa):
        super().__init__(nama_produk, "Food", harga, stok, rating, jumlah_terjual)
        if isinstance(tanggal_kadaluarsa, str):
            self.tanggal_kadaluarsa = datetime.strptime(tanggal_kadaluarsa, "%d/%m/%Y").date()
        else:
            self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def cek_kadaluarsa(self):
        if date.today() > self.tanggal_kadaluarsa:
            return f"{self.cek_kadaluarsa} sudah kadaluarsa!"
        else: 
            return f"{self.tanggal_kadaluarsa} aman dikonsumsi."

#=============================================
produk_list = [
    Electronic("Laptop Gaming", 15000000, 30, 4.5, 10),
    Electronic("Headphone", 1200000, 25, 4.2, 5),
    Fashion("Rok Mini", 350000, 20, 4.0, 5, promo=True),
    Fashion("Kemeja Pria", 250000, 50, 3.8, 8, promo=False),
    Food("Nasi Kotak", 25000, 100, 4.2, 40, "01/11/2025")
]

header= ['Nama Produk', 'Kategori', 'Harga', 'Stok Tersisa', 'Rating', 'Pendapatan', 'Expired (Food)']
data = []

for item in produk_list:
    if isinstance(item, Food):
        expired_info = item.cek_kadaluarsa()
    else:
        expired_info = "-"

    data.append([
        item.nama_produk,
        item.kategori,
        f"Rp{item.harga:,}",
        item.sisa_stok(),
        item.rating,
        f"Rp{item.pendapatan():,}",
        expired_info
    ])

print(tabulate(data, header, tablefmt = "fancy_grid", numalign="left"))