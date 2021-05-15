from .PreProcessing import PreProcessing
from .Processing import Processing
from .ReadData import ReadData
from .Visualization import Visualization
from .Result import Result

class Project(ReadData, PreProcessing, Processing, Visualization, Result):
    
    def __init__(self):
        print("PROJECT")
        super().__init__()
        super(ReadData, self).__init__()
        
