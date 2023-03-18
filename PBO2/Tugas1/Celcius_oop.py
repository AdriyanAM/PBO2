# NAMA  : ADRIYAN ARI MUKTIAWAN
# NIM   : 210511177
# KELAS : R4/ D

class Suhu:
    @staticmethod
    def celcius_to_kelvin(c):
        k = c + 273
        return k
    
#Contoh penggunaan
C = 10
K = Suhu.celcius_to_kelvin(C)

print("Konversi", C, "derajat Celcius adalah:", K, "derajat Kelvin")
