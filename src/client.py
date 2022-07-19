from factura import Factura

class Client:
    Nume = ""
    CIF = ""
    REG_COM = ""
    Facturi = []
    TVA = ""

    def __init__(self, nume, cif, tva, reg_com="", facturi=[]):
        self.Nume = nume
        self.CIF = cif
        self.TVA = tva

        if reg_com != "":
            self.REG_COM = reg_com

        if facturi != []:
            self.Facturi = facturi