from furnizor import Furnizor

class Factura:
    Valuta = ""
    NumeClient = ""
    CIF = ""
    Adresa, Judet = "", ""
    Data, DataScadenta = "", ""
    Serie, Numar, Tip = "", "", ""
    Suma = format(float(0), '.4f')
    TVA, Total, RestPlata = "", "", ""
    FFurnizor = None
    
    def __init__(self, furnizor):
        self.FFurnizor = furnizor

    def __repr__(self):
        return f"Client {self.NumeClient} {self.CIF}. Suma {self.Total}"

    def setValuta(self, valuta):
        self.Valuta = valuta
    
    def setNumeClient(self, numeClient):
        self.NumeClient = numeClient
    
    def setCIF(self, cif):
        self.CIF = cif
    
    def setData(self, data):
        self.Data = data
        self.Data = self.Data.replace("/", ".")
    
    def setDataScadenta(self, dataScadenta):
        self.DataScadenta = dataScadenta
    
    def setAdresaJudet(self, adresa, judet=""):
        self.Adresa = adresa
        self.Judet = judet

    def setSerie(self, serie):
        self.Serie = serie
    
    def setNumar(self, numar):
        self.Numar = numar
    
    def setTip(self, tip):
        self.Tip = tip

    def setSuma(self, suma):
        self.Suma = suma
    
    def setTotal(self, total):
        self.Total = total
    
    def setTVA(self, dataScadenta):
        self.DataScadenta = dataScadenta

    def setRestDePlata(self, restDePlata):
        self.RestPlata = restDePlata

def main():
    pass

if __name__ == "__main__":
    main()