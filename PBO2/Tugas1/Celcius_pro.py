# NAMA  : ADRIYAN ARI MUKTIAWAN
# NIM   : 210511177
# KELAS : R4/ D

class Suhu:
    def __init__(self, celcius):
        self.celcius = celcius
    def suhu(self):
        return self.celcius + 273.15
SuhuA = Suhu(5)
print(f"Suhu kelvin: {SuhuA.suhu()}")