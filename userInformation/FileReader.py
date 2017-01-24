import  csv

import Methods


class File:

   def FileRead(self):
        file = 'csv/DataForDT.csv'
        #Getting reccords from CSV file
        lines = csv.reader(open(file))
        #Making a list of reccords
        lisst = list(lines)
        Instance = Methods.MethodRepository()
        TraininD, TestD = Instance.MadeChunks(lisst)

        return [TraininD,TestD]