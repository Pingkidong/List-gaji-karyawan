from tabulate import tabulate

class Freelancer:
    def __init__(self, nama, durasi_kerja, upah_per_hari, proyek_selesai, jenis_freelancer):
        self.nama = nama
        self.durasi_kerja = durasi_kerja
        self.upah_per_hari = upah_per_hari
        self.proyek_selesai = proyek_selesai
        self.bonus_proyek = 0
        self.loyal = 0
        self.jenis_freelancer = jenis_freelancer

        self.bonus_per_proyek()
        self.bonus_loyalitas()

    def upah(self):
        kalkulasi_upah = self.upah_per_hari * self.durasi_kerja
        return kalkulasi_upah

    def hitung_pendapatan(self):
        total_pemasukan = self.upah() + self.bonus_proyek + self.loyal
        return total_pemasukan
#=======================================================================
class Designer(Freelancer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def bonus_per_proyek(self):
        self.bonus_proyek += self.proyek_selesai * 150000

    def bonus_loyalitas(self):
        if self.durasi_kerja > 30:
            self.loyal += 500000

class Programmer(Freelancer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def bonus_per_proyek(self):
        self.bonus_proyek += self.proyek_selesai * 200000

    def bonus_loyalitas(self):
        if self.proyek_selesai > 5:
            self.loyal += 1000000

class Writer(Freelancer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def bonus_per_proyek(self):
        self.bonus_proyek += self.proyek_selesai * 300000

    def bonus_loyalitas(self):
        if self.durasi_kerja > 20:
            self.loyal += 300000

#=============================================
d1 = Designer("Nina", 40, 300000, 3, "Designer")
p1 = Programmer("Rizky", 25, 400000, 6, 'Programmer')
w1 = Writer("Budi", 15, 250000, 2, 'Writer')

f = [d1, p1, w1]

header = ['Nama', 'Jenis Freelance', 'Durasi Kerja', 'Banyak Projek', 'Upah/Hari', 'Total Pemasukan']
data= []

for baris in f:
    data.append([
        baris.nama,
        baris.jenis_freelancer,
        f"{baris.durasi_kerja} Hari",
        baris.proyek_selesai,
        f"Rp{baris.upah_per_hari:,}",
        f"Rp{baris.hitung_pendapatan():,}"
    ])

print(tabulate(data, header, tablefmt="fancy_grid", numalign="left"))
