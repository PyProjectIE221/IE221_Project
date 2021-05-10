import pytest
from python_ie221.PreProcessing import fill_null
import pandas as pd
class TestFillNull(object):
   
    def test_fill_max(self):
        data = pd.DataFrame({'col1': [1, None, 4 ,6], 'col2': [1,2, 3, 4], 
                         'col3': ['a','b','c',None]})
        expected = pd.DataFrame({'col1': [1, 4, 4 ], 'col2': [1,2, 3], 
                         'col3': ['a','b','c']})
        assert fill_null(data,'max') == expected
        