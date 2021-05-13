#!/usr/bin/python
#-*- coding: utf-8 -*-

import pandas as pd
from pandas.io.parsers import read_csv

class ReadData:

    def __init__(self):

        #leave this line below
        super().__init__()
    
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)

    #def __init__(self,filename):
     #   self._data = []
      #  self.localdir = '/IE221_Project/data'
       # self.filename = filename
        #self.filepath = os.path.join(self.localdir,self.filename)
        #self.read_data()
    def read_data(self, filepath):
        """Read data from file csv

        Args: 
            Filepath(string) : file data kiểu csv

        Returns: 
            dataFrame
        """
        self.data = pd.read_csv(filepath)
        return self.data
    
