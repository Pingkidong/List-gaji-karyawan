from tabulate import tabulate
import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

class Karyawan:
    def __init__(self, nama, jabatan, usia, tanggal_masuk, gaji_pokok, jam, proyek):
        self.nama = nama
        self.jabatan = jabatan
        self.usia = usia
        self.jam = jam
        self.proyek = proyek
        if isinstance(tanggal_masuk,str):
            self.tanggal_masuk = datetime.strptime(tanggal_masuk, "%d/%m/%Y").date()
        else:
            self.tanggal_masuk = tanggal_masuk

        self.gaji_pokok = gaji_pokok
        self.tunjangan = {}
        self.bonus_usia()
        self.bonus_tenure()
        self.lembur()
        self.bonus_proyek()


    def tenure(self):
        hari_ini = date.today()
        #print("DEBUG tanggal masuk:", self.tanggal_masuk)
        selisih = relativedelta(hari_ini, self.tanggal_masuk)
        return selisih.years

    def bonus_usia(self):
        if self.usia >= 30:
            self.tunjangan['Bonus usia'] = 500000

    def bonus_tenure(self):
        return 0

    def lembur(self):
        upah_per_jam = self.gaji_pokok / 173
        if self.jam <= 0:
            return
        
        total_lembur = 1.5 * upah_per_jam if self.jam >= 1 else 0
        if self.jam > 1:
            total_lembur += (self.jam - 1) * 2 * upah_per_jam

        self.tunjangan[f'Lembur {self.jam} jam'] =  int(total_lembur)

    def bonus_proyek(self):
        #self.tunjangan['Bonus proyek'] = self.tunjangan.get('Bonus proyek', 0) + int(self.proyek)
        return 0

    def total_tunjangan(self):
        total_tunjangan = sum(self.tunjangan.values())
        return total_tunjangan

    def total_gaji(self):
        return self.total_tunjangan() + self.gaji_pokok


#======================================================================================================
class DataAnalist(Karyawan):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bonus_tenure()
        self.bonus_proyek()

    def bonus_tenure(self):
        bonus_tenure = (self.tenure() // 2) * 1500000
        self.tunjangan[f'Bonus Tenure {self.tenure()} Tahun'] = bonus_tenure

    def bonus_proyek(self):
        bonus_proyek = (self.proyek * 0.05)
        self.tunjangan['Bonus Proyek'] = self.tunjangan.get('bonus_proyek', 0) + int(bonus_proyek)

class DataScientist(Karyawan):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bonus_tenure()

    def bonus_tenure(self):
        bonus_tenure = (self.tenure() // 2) * 2000000
        self.tunjangan[f'Bonus Tenure {self.tenure()} Tahun'] = bonus_tenure

    def bonus_proyek(self):
        bonus_proyek = (self.proyek * 0.07)
        self.tunjangan['Bonus Proyek'] = self.tunjangan.get('bonus_proyek', 0) + int(bonus_proyek)

class Admin(Karyawan):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bonus_tenure()

    def bonus_tenure(self):
        bonus_tenure = (self.tenure() // 2) * 750000
        self.tunjangan[f'Bonus Tenure {self.tenure()} Tahun'] = bonus_tenure

    def bonus_proyek(self):
        bonus_proyek = (self.proyek * 0.01)
        self.tunjangan['Bonus Proyek'] = self.tunjangan.get('bonus_proyek', 0) + int(bonus_proyek)

class DataEng(Karyawan):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bonus_tenure()

    def bonus_tenure(self):
        bonus_tenure = (self.tenure() // 2) * 1000000
        self.tunjangan[f'Bonus Tenure {self.tenure()} Tahun'] = bonus_tenure

    def bonus_proyek(self):
        bonus_proyek = (self.proyek * 0.035)
        self.tunjangan['Bonus Proyek'] = self.tunjangan.get('bonus_proyek', 0) + int(bonus_proyek)

data = []
df = pd.read_excel("list_karyawan.xlsx")
for i, row in df.iterrows():
    jabatan = row['Jabatan']
    if "Data Analist" in jabatan:
        k = DataAnalist(
            row['Nama'],
            row['Jabatan'],
            row['Usia'],
            row['Tanggal Masuk'],
            row['Gaji Pokok'],
            row['Lembur'],
            row['Proyek']
            )
        

    elif "Data Scientist" in jabatan:
        k = DataScientist(
            row['Nama'],
            row['Jabatan'],
            row['Usia'],
            row['Tanggal Masuk'],
            row['Gaji Pokok'],
            row['Lembur'],
            row['Proyek']
            )

    elif "Data Cleanser" in jabatan:
        k = DataEng(
            row['Nama'],
            row['Jabatan'],
            row['Usia'],
            row['Tanggal Masuk'],
            row['Gaji Pokok'],
            row['Lembur'],
            row['Proyek']
            ) 

    elif "Admin" in jabatan:
        k = Admin(
            row['Nama'],
            row['Jabatan'],
            row['Usia'],
            row['Tanggal Masuk'],
            row['Gaji Pokok'],
            row['Lembur'],
            row['Proyek']
            )

    else:
        continue

    rincian_tunjangan = "\n".join([f"{key}: Rp{val:,}" for key, val in k.tunjangan.items()])
    data.append(
        [k.nama,
        k.usia,
        k.jabatan,
        k.tenure(),
        f"Rp{k.gaji_pokok: ,}",
        rincian_tunjangan,
        f"Rp{k.total_tunjangan(): ,}",
        f"Rp{k.total_gaji(): ,}"
        ])
    
header = ['Nama', 'Usia', 'Jabatan', 'Tenure', 'Gaji Pokok', 'Rincian Tunjangan', 'Total Tunjangan', 'Total Gaji']
print(tabulate(data, header, tablefmt="grid", showindex=range(1, len(data)+1)))



    
    #print(f"{k.nama} | {k.jabatan} | Masa kerja: {k.tenure()} tahun | Total tunjangan: Rp{k.total_tunjangan():,} | Total gaji: Rp{k.total_gaji():,}")