import xlrd
from factura import Factura

def convert_xldate_to_date(xldate):
    xlrd.xldate_as_datetime(xldate, 0)

def checkXLDate(date):
    if (date.ctype == xlrd.XL_CELL_DATE):
            dateObj = convert_xldate_to_date(date.value)
            date = dateObj.date().strftime("%d.%m.%Y")
            return date

    return date.value

def getExcelRows(numeExcel):
    sheets = xlrd.open_workbook(numeExcel)
    sheetsCount = sheets.nsheets

    rows = []

    for sheet_num in range(0, sheetsCount):
        sheet = sheets.sheet_by_index(sheet_num)

        for rowIndex in range(0, sheet.nrows):
            row = sheet.row(rowIndex)

            emptyCnt = 0
            noValueCnt = 0
            headerRow = {'CLIENT', 'CIF', 'ADRESA', 'OBSERVATII'}
            for item in row:
                text = str(item.value).upper()
                if (text in headerRow):
                    emptyCnt = 10
                    break

                if (str(xlrd.empty_cell) == str(item)):
                    emptyCnt += 1
                    continue

                if (item.value == ''):
                    noValueCnt += 1

            if (emptyCnt < 7 and noValueCnt < 5):
                rows.append(row)
            else:
                print(f"Ignored following row {row}")
    
    print(f"Scanned {len(rows)} rows.")
    return rows

def parseRows_Videointerfoane(rows):
    facturi = []
    for row in rows:
        # VIDEOINTERFOANE 
        # numeClient = row[1]
        # cif = row[2]
        # adresa = row[3]
        # serieFactura = row[4]
        # data = row[5]
        # dataScadenta = row[6]
        # tipFactura = row[7]
        # valoareTotala = row[8] 
        factura = Factura()
        factura.setNumeClient(row[1].value)
        factura.setCIF(row[2].value)
        factura.setAdresaJudet(row[3].value)
        factura.setSerie(row[4].value)
        factura.setData(row[5].value)
        factura.setDataScadenta(row[6].value)
        factura.setTip(row[7].value)
        factura.setTotal(row[8].value)

        facturi.append(factura)
    return facturi

def parseRows_Beauty(rows):
    facturi = []
    for row in rows:
        # BEAUTY
        # valuta = row[0]
        # numeClient = row[1]
        # cif = row[2]
        # localitate = row[3]
        # judet = row[4]
        # data = row[5]
        # dataScadenta = row[17]
        # serie = row[6]
        # numar = row[7]
        # tip = row[8]
        # suma = row[9]
        # tva = row[10]
        # total = row[11]
        factura = Factura()
        factura.setValuta(row[0])
        factura.setNumeClient(row[1].value)
        factura.setCIF(row[2].value)
        factura.setAdresaJudet(row[3].value, row[4].value)
        data = checkXLDate(row[5])
        factura.setData(data)
        dataScadenta = checkXLDate(row[17])
        factura.setDataScadenta(dataScadenta)
        factura.setSerie(row[6])
        factura.setNumar(row[7])
        factura.setTip(row[8])
        factura.setSuma(row[9])
        factura.setTVA(row[10])
        factura.setTotal(row[11])

        facturi.append(factura)
    return facturi

def main():
    pass

if __name__ == "__main__":
    main()