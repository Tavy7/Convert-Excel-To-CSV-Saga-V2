class Furnizor:
    Nume = ""
    CIF = ""
    REG_COM = ""
    Cont = ""
    TVA = ""

    def __init__(self, nume, cif, cont, tva, reg_com=""):
        self.Nume = nume
        self.CIF = cif
        self.Cont = cont
        self.TVA = tva

        if reg_com != "":
            self.REG_COM = reg_com

def main():
    pass

if __name__ == "__main__":
    main()