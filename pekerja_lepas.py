class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.insentif_lembur = insentif_lembur
        self.pendapatan_tambahan = 0

    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    
    def proyek(self, proyek):
        self.pendapatan_tambahan += proyek
    
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan

#Child class
class pekerja_lepas(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan,0)

    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan += int(nilai_proyek *0.01)