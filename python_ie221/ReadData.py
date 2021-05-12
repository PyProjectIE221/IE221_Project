#!/usr/bin/python
#-*- coding: utf-8 -*-

import pandas as pd
from pandas.io.parsers import read_csv


class ReadData:
    def __init__(self):
        #leave this line below
        super().__init__()
    
    def __init__(self,filepath):
        self.data = read_csv(filepath=filepath)
        save_data = self.data.to_csv('/IE221_Project/data')