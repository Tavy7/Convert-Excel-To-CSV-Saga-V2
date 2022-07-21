import xml.etree.ElementTree as gfg 
from xml.dom import minidom
from datetime import date
import re
import var

def getTodayDate():
    return date.today().strftime("%d-%m-%Y")

def getFacturaXMLName(cif):
    return f"F_{cif}_multiple_{getTodayDate()}.xml"

def createFactura(root, factura, tags):
    tagFactura = gfg.SubElement(root, tags['Factura'])
    tagAntet = gfg.SubElement(tagFactura, tags['Antet'])

    # Furnizor
    gfg.SubElement(tagAntet, tags['FurnizorNume']).text = factura.FFurnizor.Nume
    gfg.SubElement(tagAntet, tags['FurnizorCIF']).text = factura.FFurnizor.CIF
    gfg.SubElement(tagAntet, tags['ClientNume']).text = str(factura.numeClient)
    gfg.SubElement(tagAntet, tags['ClientInformatiiSuplimentare'])
    gfg.SubElement(tagAntet, tags['ClientCIF']).text = str(factura.CIF)
    gfg.SubElement(tagAntet, tags['ClientNrRegCom']).text
    gfg.SubElement(tagAntet, tags['ClientTara']).text = "Romania"
    gfg.SubElement(tagAntet, tags['ClientJudet']).text
    gfg.SubElement(tagAntet, tags['FacturaNumar']).text = str(factura.Numar)
    gfg.SubElement(tagAntet, tags['FacturaData']).text = str(factura.Data)
    gfg.SubElement(tagAntet, tags['FacturaScadenta']).text = str(factura.DataScadenta)
    gfg.SubElement(tagAntet, tags['FacturaTaxareInversa']).text = "Nu"
    gfg.SubElement(tagAntet, tags['FacturaTVAIncasare']).text = "Nu"
    gfg.SubElement(tagAntet, tags['FacturaTip'])
    gfg.SubElement(tagAntet, tags['FacturaInformatiiSuplimentare'])
    gfg.SubElement(tagAntet, tags['FacturaMoneda']).text = str(factura.valuta)
    gfg.SubElement(tagAntet, tags['FacturaCotaTVA']).text = factura.FFurinzor.TVA
    gfg.SubElement(tagAntet, tags['FacturaID'])
    gfg.SubElement(tagAntet, tags['FacturaGreutate']).text = "0.000"
    
    tagDetalii = gfg.SubElement(tagFactura, tags['Detalii'])
    tagContinut = gfg.SubElement(tagDetalii, tags['Continut'])
    tagLinie = gfg.SubElement(tagContinut, tags['Linie'])
    
    gfg.SubElement(tagLinie, tags['LinieNrCrt']).text = "1"
    gfg.SubElement(tagLinie, tags['InformatiiSuplimentare'])
    gfg.SubElement(tagLinie, tags['UM']).text = "buc"
    gfg.SubElement(tagLinie, tags['Cantitate']).text = "1.0000"
    gfg.SubElement(tagLinie, tags['Pret']).text = str(factura.Suma)
    factura.Suma = format(float(factura.Suma), '.2f')
    gfg.SubElement(tagLinie, tags['Valoare']).text = str(factura.Suma)
    gfg.SubElement(tagLinie, tags['CotaTVA']).text = factura.FFurnizor.TVA
    gfg.SubElement(tagLinie, tags['ProcTVA']).text = factura.FFurnizor.TVA
    gfg.SubElement(tagLinie, tags['TVA']).text = factura.TVA
    gfg.SubElement(tagLinie, tags["Cont"]).text = factura.FFurnizor.Cont
     
    tagSumar = gfg.SubElement(tagFactura, tags['Sumar'])
    gfg.SubElement(tagSumar, tags['Total']).text = str(factura.Total)
    gfg.SubElement(tagSumar, tags['TotalTVA']).text = str(factura.TVA)
    gfg.SubElement(tagSumar, tags['TotalValoare']).text = str(factura.Suma)
    
    tagObservatii = gfg.SubElement(tagFactura, tags['Observatii'])
    gfg.SubElement(tagObservatii, tags['SoldClient'])
    gfg.SubElement(tagObservatii, tags['txtObservatii'])

def createFacturiXML(facturi):
    tags = var.taguriFacturi

    rootElement = gfg.Element(tags['Facturi'])
    for factura in facturi:
        createFactura(rootElement, factura, tags)
  
    tree = minidom.parseString(gfg.tostring(rootElement)).toprettyxml(indent="    ")
    x = tree
    x = re.sub(r'<([^\/]+)\/\>', r'<\1></\1>', tree)
    furnizor = facturi[0].FFurnizor
    file = open(getFacturaXMLName(furnizor.CIF), "w")
    file.write(x)

    file.close()

def createIncasare(root, incasare, tags):
    tagLinie = gfg.SubElement(root, tags["Linie"])
    
    gfg.SubElement(tagLinie, tags["Data"]).text = str(incasare.Data)
    gfg.SubElement(tagLinie, tags["Numar"]).text = str(incasare.FacturaID)
    gfg.SubElement(tagLinie, tags["Suma"]).text = str(incasare.Suma)
    gfg.SubElement(tagLinie, tags["Explicatie"]).text = str(incasare.Explicatie)
    gfg.SubElement(tagLinie, tags["Cont"]).text = str(incasare.Cont)
    gfg.SubElement(tagLinie, tags["ContClient"]).text = str(incasare.ContClient)
    gfg.SubElement(tagLinie, tags["CodFiscal"]).text = str(incasare.CIF)

def createIncasareXML(incasari):
    tags = var.taguriIncasari

    rootElement = gfg.Element(tags['Incasari'])
    for incasare in incasari:
        createIncasare(rootElement, incasare, tags)
        
    tree = minidom.parseString(gfg.tostring(rootElement)).toprettyxml(indent="    ")
    x = tree
    x = re.sub(r'<([^\/]+)\/\>', r'<\1></\1>', tree)
    
    fileName = f"I_{getTodayDate()}.xml"
    writeFile = open(fileName, "w")
    writeFile.write(x)
    writeFile.close()

if __name__ == "__main__":
    pass