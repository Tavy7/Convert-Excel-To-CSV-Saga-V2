class Incasare:
    CIF = ""
    FacturaID = ""
    Data = ""
    Suma = ""
    Explicatie = ""
    Cont = ""
    ContClient = ""

    def __init__(self, cif, facturaID, data, suma, cont, contClient):
        self.CIF = cif.replace("\n", "")
        self.FacturaID = int(facturaID)
        self.Data = data.replace("/", ".")
        self.Suma = suma
        self.Cont = cont
        self.ContClient = contClient
        
    def __repr__(self):
        return f"[CIF = {self.CIF}, Data = {self.Data}, Suma {self.Suma}, {self.FacturaID}]"