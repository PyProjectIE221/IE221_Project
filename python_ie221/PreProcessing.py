import pandas as pd
import numpy as np
class PreProcessing:
    def __init__(self):
        
        #Leave this line below
        super().__init__()
    
    def count_null(self, data):
        """Count how many null in your data
        
        Args:
            data(dataFrame): your data after convert from csv, json, ...
        
        Returns:
            Series: Object with missing values
        
        """
        print("\nNumber of NaN in your data: ",data.isnull().sum().sum())
        return data.isnull().sum()
    
    def fill_null(self, data):
        """Find any null data and replace it with meadian value in column or drop it if its columns is string
        
        Args:
            data(dataFrame): your data with missing value
            method(string): median, mean, avg, max , min
            
        Returns:
            dataFrame: data with no missing value
        """
        for col in data.columns:
            if(pd.api.types.is_numeric_dtype(data[col]) == False):
                pd.DataFrame(data[col]).dropna(axis=1)
            else:
                if(data[col].isnull().any() == True):
                    pd.DataFrame(data[col]).fillna(data[col].median, inplace = True)
                    
        print("Now, your number of nan data is ",data.isnull().sum().sum())
        
        return data

# import pandas as pd  
studentData = {
    'name' : ['jack', 'Riti', 'dd'],
    'age' : [34, 30, None],
    'city' : ['Sydney', 'Delhi', None]
}
a = pd.DataFrame(studentData)

if(pd.api.types.is_numeric_dtype(studentData['city']) == False):
    a.dropna(axis = 0)
# a.apply((lambda x: x.fillna(x.mean()) if pd.api.types.is_dtype(x) == True))