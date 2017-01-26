import pandas as pd
from StringIO import StringIO as SIO

class Data:
    """
    Object that parses the data of a given file, organizes each column into a pandas DF
    """
    
    def __init__(self, file_string):
        self.file_string = file_string
        self.data = pd.read_csv(SIO(self.file_string))
        self.columns = list(self.data.columns.values)

    def getData(self):
        return self.data

    def getColumns(self):
        return self.columns

