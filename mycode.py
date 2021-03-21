import openpyxl


class Serial:
    def __init__(self, number, order, article, customer, date, comment):
        self.number = number
        self.order = order
        self.article = article
        self.customer = customer
        self.date = date
        self.comment = comment


a = Serial('115605','2105','801877','petya','28.11.90','test')

print( a.__dict__)

class Readxls:
    """ Класс берет эксель таблицу по образцу через openpyxl
    парсит ее и выдает на выходе список с серийными номерами
    """
    def __init__(self, filename):
        self.filename = filename
        self.excelfile = openpyxl.load_workbook(filename, read_only=True)
        self.sheet = self.excelfile.active

    def givemelist(self):
        print(self.sheet.max_row)
        for i in range(1,self.sheet.max_row+1):
            print(self.sheet.cell(row=i,column=1).value)


b = Readxls('test.xlsx')
b.givemelist()
