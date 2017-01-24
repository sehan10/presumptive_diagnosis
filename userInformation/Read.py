import csv

import ID3Method


class File:

   def FileRead(self):
        file = 'csv/DataForDT.csv'
        #Getting reccords from CSV file
        lines = csv.reader(open(file))
        #Making a list of reccords
        lisst = list(lines)
        Instance = ID3Method.MethodRepository()
        TraininD, TestD, Heading = Instance.MadeChunks(lisst)

        return [TraininD,TestD,Heading]