class Factura:
    Valuta = ""
    NumeClient = ""
    CIF = ""
    Adresa, Judet = ""
    Data, DataScadenta = ""
    Serie, Numar, Tip = ""
    Suma = format(float(0), '.4f')
    TVA, Total, RestPlata = ""
    
    def __reper__(self):
        return "Client " + str(self.numeClient) + " " + str(self.CIF)

    def setValuta(self, valuta):
        self.Valuta = valuta
    
    def setNumeClient(self, numeClient):
        self.NumeClient = numeClient
    
    def setCIF(self, cif):
        self.CIF = cif
    
    def setData(self, data):
        self.Data = data
    
    def setDataScadenta(self, dataScadenta):
        self.DataScadenta = dataScadenta
    
    def setAdresaJudet(self, adresa, judet):
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
    