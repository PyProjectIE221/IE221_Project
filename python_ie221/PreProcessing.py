import pandas as pd
import numpy as np
import string
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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
        print("\nNumber of NaN in your data: ",data.isnull().sum().sum(),'\n')
        return data.isnull().sum()
    
    def fill_null(self, data, method = 'median'):
        """Find any null data and replace it with meadian value in column or drop it if its columns is string
        
        Args:
            data(dataFrame): your data with missing value
            method(string): mean, median, max, min
        Returns:
            dataFrame: data with no missing value
        """
        dict_func = {'max': pd.Series.max, 'min': pd.Series.min, 'median': pd.Series.median,
                     'mean': pd.Series.mean }
        
        for col in data.columns:
            if(pd.api.types.is_numeric_dtype(data[col]) == True):
                data[col].fillna(value = dict_func[method](data[col]))
        data = data.dropna()
                    
        print("\nNow, your number of nan data is ",data.isnull().sum().sum())
        
        return data
    
    def remove_punc_and_lower(self, data):
        """Remove all punctuation and change letter to lower case (except Date and Label columns)
        
        Args:
            data(dataFrame): 
        
        Returns:
            dataFrame: data after change
        """
        
        for col in data.columns:
            if col == 'Date':
                continue
            if col == "Label":
                continue
            data[col] = data[col].str.lower()
            data[col].replace(["b"+"[^a-zA-Z]","[^a-zA-Z]"]," ",True,None,True)
        return data
    
    def combine_title(self,data):
        """Combine all title to a column  
        
        Args: 
            data(dataFrame): 
        
        Returns:
            dataFrame: combined title data
        """
        head_line = []
        for i in range(0,len(data.index)):
            head_line.append(''.join(str(x) for x in data.iloc[i,2:-1]))
        
        new_data = data.copy()
        new_data = new_data.drop(new_data.iloc[:,2:], axis=1)
        new_data['title'] = head_line
        
        return new_data
    
    def tokeninze_and_remove_stopword(self,data):
        """Split every word and remove common word cause it has no value for our processing
        
        Args:
            data(dataFrame)
        
        Returns:
            dataFrame
        
        For ex:  "A and B is friend" -> ['A','B','friend']
        """
        
        stop_words = set(stopwords.words('English'))
        list_filter = []
        for row in data:
            word_tokens = word_tokenize(row[2])
            filter_sentence = [w for w in word_tokens if w not  in stop_words]
            list_filter.append(filter_sentence)
        print(list_filter)
        
    
a = PreProcessing()
data = pd.read_csv('data\Combined_News_DJIA.csv')
a.count_null(data)
data = a.fill_null(data,'mean')
data = a.remove_punc_and_lower(data)
data = a.combine_title(data)
a.tokeninze_and_remove_stopword(data)
