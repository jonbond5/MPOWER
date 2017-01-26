import pandas as pd
from StringIO import StringIO as SIO

class Data:
    """
    Object that parses the data of a given file, organizes each column into a pandas DF
    """
    
    def __init__(self, file_string):
        self.file_string = file_string
        self.data = pd.read_csv(self.file_string)
        self.columns = list(self.data.columns.values)

    def getData(self):
        return self.data

    def getColumns(self):
        return self.columns

    def getSubdata(self, column):
        return self.data[column]

def test():
    print """
    Methods:
    getData - returns DataFrame 
    getColums - returns column names of the DataFrame
    getSubdata(column) - requires column, returns data of a certain column

    Files:
    Filenames are from 2006-2016

    To quit:
    Enter quit
    """

    while 1:
        option = raw_input('What would you like to view: ')
        filename = raw_input('What file are we dealing with: ')
        d = Data(filename)
        if option == 'getData':
            d.getData()
        elif option == 'getColumns':
            d.getColumns()
        elif option == 'getSubdata':
            column = raw_input('Column name: ')
            d.getSubdata(column)
        elif option == 'quit':
            break
