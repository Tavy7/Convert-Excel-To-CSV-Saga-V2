import xlrd

# TO DO Refractor

def read_firms_txt():
    file = open("firme.txt")
    
    firme = []
    for line in file:
        nume, cod = line.split(",")
        firma = (nume, cod)
        firme.append(firma)

    return firme

def format_firm_name(firm_name):
    firm_name = firm_name.upper()
    firm_name = firm_name.replace(".", "")
    firm_name = firm_name.replace("INTREPRINDERE INDIVIDUALA", "II")
    firm_name = firm_name.replace("PERSOANA FIZICA AUTORIZATA", "PFA")
    firm_name = firm_name.replace("PFA", "")
    firm_name = firm_name.replace("SRL", "")
    firm_name = firm_name.replace("II", "")

    # Removes all spaces at the end of string
    while (firm_name[-1] == ' '):
        firm_name = firm_name[:-1]
    
    return firm_name

def search_firm(firm_name):    
    firms = read_firms_txt()
    
    firm_name = format_firm_name(firm_name)
    #print(f"searching for{firm_name}x")
    
    c = 0
    for firm in firms:
        formattedName = format_firm_name(firm[0])
        #if (firm_name.split(" ")[0] == "HASU" and formattedName[0] == 'H'):
         #   print(f"{firm_name}, {formattedName}, {formattedName == firm_name}")
        if (formattedName == firm_name):
            c = 1

            return firm[1]

    if c == 0:
        print("Not found", firm_name)
    return -1


if __name__ == "__main__":
    search_firm("")