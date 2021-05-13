import pandas as pd
from nltk.corpus import stopwords
from collections import Counter
pd.options.mode.chained_assignment = None
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
                    
        print("\nAfter fill, your number of nan data is ",data.isnull().sum().sum())
        
        self.pre_data = data
        return self.pre_data
    
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
            temp = data.loc[:,col].copy()
            data.loc[:,col] = temp.str.lower()
            data.loc[:,col].replace(["b"+"[^a-zA-Z]","[^a-zA-Z]"]," ",True,None,True)
        
        self.pre_data = data
        return self.pre_data
    
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
        
        data = data.drop(data.iloc[:,2:], axis=1)
        data['title'] = head_line
        
        self.pre_data = data
        return self.pre_data
    
    def remove_stopword(self,data):
        """Remove common word cause it has no value for our processing
        
        Args:
            data(dataFrame)
        
        Returns:
            dataFrame
        
        For ex:  "A and B is friend" -> ['A','B','friend']
        """
        
        stop_words = stopwords.words('english')
        stopwords_dict = Counter(stop_words)
        list_filter = []
        for row in range(0,data.shape[0]):
             fil = ' '.join([word for word in data.iloc[row,2].split() if word not in stopwords_dict])
             list_filter.append(fil)
        data['filter'] = list_filter
        
        data = data.drop(columns = 'title')
        
        self.pre_data = data
        return self.pre_data
    
    def fully_preprocess(self,data, method ='median'):
        """ PreProcess data with all step : fill null, remove stop word, combine, ...
        
        Args:
            data(dataFrame): original data
            method(string): mean, median, max, min
        
        Returns:
            dataFrame: preprocessed data and file csv in 'data\preprocessed_data.csv'
        """
        self.count_null(data)
        fill_data = self.fill_null(data)
        remove_data = self.remove_punc_and_lower(fill_data)
        comb_remove_data = self.combine_title(remove_data)
        final = self.remove_stopword(comb_remove_data)
        
        final_csv = final.set_index('Date')
        final_csv.to_csv('data\preprocessed_data.csv')
        
        self.pre_data = final
        return self.pre_data
    
    
