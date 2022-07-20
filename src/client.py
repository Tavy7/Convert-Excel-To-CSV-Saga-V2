class Client:
    Nume = ""
    CIF = ""
    REG_COM = ""

    def __init__(self, nume, cif, reg_com=""):
        self.Nume = nume
        self.CIF = cif

        if reg_com != "":
            self.REG_COM = reg_com

def main():
    pass

if __name__ == "__main__":
    main()