class Kitob:
    def __init__(self, nomi, narxi):
        self.nomi = nomi
        self.__narxi = narxi

    def chegirma(self, qiymat):
        self.__narxi -= qiymat

    def info(self):
        print(f"Nomi: {self.nomi}")
        print(f"Hozirgi narxi: {self.__narxi}")


k1 = Kitob("O'tkan kunlar", 50000)
k1.info()

k1.chegirma(30000)
k1.info()
