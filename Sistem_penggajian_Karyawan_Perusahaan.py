from tabulate import tabulate
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

class Karyawan:
    def __init__(self, nama, jabatan, usia, tanggal_masuk, gaji_pokok):
        self.nama = nama
        self.usia = usia
        self.gaji_pokok = gaji_pokok
        self.jabatan = jabatan
        self.tanggal_masuk = datetime.strptime(tanggal_masuk, "%d/%m/%Y").date()
        #dict untuk rincian tunjangan
        self.tunjangan_detail = {}

        self.hitung_bonus_usia_lama_kerja()

    def lama_kerja(self):
        hari_ini = date.today()
        selisih = relativedelta(hari_ini, self.tanggal_masuk)
        return selisih.years

    def hitung_bonus_usia_lama_kerja(self):
        #Bonus berdasarkan usia
        if self.usia > 30:
            self.tunjangan_detail['Bonus usia'] = 200000

        #Bonus berdasarkan lama kerja
        bonus_lama_kerja = self.bonus_masa_kerja()
        if bonus_lama_kerja > 0:
            self.tunjangan_detail['Bonus lama kerja'] = bonus_lama_kerja

    def bonus_masa_kerja(self):
        return 0

    def lembur(self, jam):
        upah_per_jam = self.gaji_pokok / 173
        if jam <= 0:
            return
        total = 1.5 * upah_per_jam if jam >= 1 else 0
        if jam > 1:
            total += (jam - 1) * 2 * upah_per_jam
        self.tunjangan_detail[f'Lembur {jam} jam'] = int(total)
    
    def bonus_proyek(self, proyek):
        self.tunjangan_detail['Bonus proyek'] = self.tunjangan_detail.get('Bonus proyek', 0) + int(proyek)

    def total_tunjangan(self):
        return sum(self.tunjangan_detail.values())
    
    def total_pendapatan(self):
        return self.gaji_pokok + self.total_tunjangan()

#===================================================
class AnalisData(Karyawan):
    def __init__(self, nama, jabatan, usia, tanggal_masuk):
        super().__init__(nama, jabatan, usia, tanggal_masuk, gaji_pokok= 7000000)
    
    def bonus_masa_kerja(self):
        tahun = self.lama_kerja()
        kelipatan = tahun // 2
        return kelipatan * 1000000

class IlmuanData(Karyawan):
    def __init__(self, nama, jabatan, usia, tanggal_masuk):
        super().__init__(nama, jabatan, usia, tanggal_masuk, gaji_pokok= 12000000)

    def bonus_masa_kerja(self):
        tahun = self.lama_kerja()
        kelipatan = tahun // 2
        return kelipatan * 1500000

    def bonus_proyek(self, proyek):
        self.tunjangan_detail['Bonus proyek'] = self.tunjangan_detail.get('Bonus proyek', 0)+ int(proyek * 0.1)

class TenagaLepas(Karyawan):
    def __init__(self, nama, jabatan, usia, tanggal_masuk, gaji_pokok):
        super().__init__(nama, jabatan, usia, tanggal_masuk, gaji_pokok)

    def bonus_masa_kerja(self):
        tahun = self.lama_kerja()
        kelipatan = tahun // 2
        return kelipatan * 250000

    def bonus_proyek(self, proyek):
        self.tunjangan_detail['Bonus proyek'] = self.tunjangan_detail.get('Bonus proyek', 0)+ int(proyek * 0.01)        

    def lembur(self, jam):
        return

class DataCleansing(TenagaLepas):
    def __init__(self, nama, jabatan, usia, tanggal_masuk):
        super().__init__(nama, jabatan, usia, tanggal_masuk, gaji_pokok= 5000000)

    def bonus_masa_kerja(self):
        tahun = self.lama_kerja()
        kelipatan = tahun // 2
        return kelipatan * 300000

#==============================================
k1 = AnalisData('Dina', 'Analis Data', 32, '16/06/2020')
k2 = IlmuanData('Bayu', 'Ilmuwan Data', 28, '10/01/2018')
#k2 = AnalisData('Dina', 'Data Analis', 29, '23-06-2020', 7000000, 400000)
k3 = IlmuanData('Udin', 'Data Scientist', 35, '24/04/2018')
k4 = AnalisData('Sita', 'Analis Data', 36, '24/04/2018')
k5 = DataCleansing('Agus', 'Data Cleanser', 35, '23/06/2020')

k1.lembur(3)
k1.bonus_proyek(5000000)
k2.lembur(2)
k2.bonus_proyek(2000000)
#k2.bonus_proyek(1000000)
k3.bonus_proyek(5000000)
k4.bonus_proyek(3000000)
k5.bonus_proyek(2000000)

karyawan_list = [k1, k2, k3, k4, k5]

header = ['Nama', 'Jabatan', 'Lama Kerja', 'Usia', 'Gaji Pokok', 'Tunjangan', 'Total Gaji']
data = []

for k in karyawan_list:
    tunjangan_rinci = "\n".join([f"{k}: Rp{v:,}" for k, v in k.tunjangan_detail.items()])
    data.append([
        k.nama, 
        k.jabatan, 
        f"{k.lama_kerja()} Tahun", 
        k.usia,
        f"Rp{k.gaji_pokok:,}",
        tunjangan_rinci,
        f"Rp{k.total_pendapatan():,}"
        ])

print(tabulate(data, header, tablefmt="fancy_grid", numalign="right", showindex=range(1, len(data)+1)))






    