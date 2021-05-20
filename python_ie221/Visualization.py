import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
from collections import Counter


class Visualization:
    """This class receive data from Proprocessing and Result class to visualize.
     The graph make data easily to understand. To understand how to visualize, you should read docstring of function
     to know what args you should put it in
     
    Attribute:
        This class does not produce any attribute.
    
    
    """
    
    def __init__(self):
        #leave this line below
        super().__init__()

    
    def top20_common(self,dataframe):
        """
        Top 20 words that appear the most in our data after remove stopwords  
        
        Args: 
            data(dataframe): Format df should have 3 columns: Date  Label(int)   Sentence(string)
        
        Returns:
            Returns: This method does not return any value
        """
        counter = Counter()
        for row in range(dataframe.shape[0]):
            counter += Counter(dataframe.iloc[row,2].split(' '))
        most_common_20 = counter.most_common(20)
        data = pd.DataFrame(data = most_common_20, columns=['word','frequency'])
        
        fig,ax = plt.subplots(figsize=(10, 6))
        sb.barplot(x='word', y='frequency', data=data, ax=ax)
        plt.title('Top 20 common word when the Dowjones goes up')
        plt.xticks(rotation='vertical')
            
    

  
    def top20_common_go_up(self,dataframe):
        """
        Top 20 words that appear the most when the market goes up in our data after remove stopwords  
        
        Args: 
            data(dataframe): Format df should have 3 columns: Date  Label(int)   Sentence(string)
        
        Returns:
            Returns: This method does not return any value
        """
        counter = Counter()
        for row in range(dataframe.shape[0]):
            if(dataframe.iloc[row,1] == 1):
                counter += Counter(dataframe.iloc[row,2].split(' '))
        most_common_20 = counter.most_common(20)
        data = pd.DataFrame(data = most_common_20, columns=['word','frequency'])
        
        fig,ax = plt.subplots(figsize=(10, 6))
        sb.barplot(x='word', y='frequency', data=data, ax=ax)
        plt.title('Top 20 common word when the Dowjones goes up')
        plt.xticks(rotation='vertical')  
        

    def top20_common_go_down(self,dataframe):
        """
        Top 20 words that appear the most when the market goes down in our data after remove stopwords  
        
        Args: 
            data(dataframe): Format df should have 3 columns: Date  Label(int)   Sentence(string)
        
        Returns:
            Returns: This method does not return any value
        """
        counter = Counter()
        for row in range(dataframe.shape[0]):
            if(dataframe.iloc[row,1] == 0):
                counter += Counter(dataframe.iloc[row,2].split(' '))
        most_common_20 = counter.most_common(20)
        data = pd.DataFrame(data = most_common_20, columns=['word','frequency'])
        
        fig,ax = plt.subplots(figsize=(10, 6))
        sb.barplot(x='word', y='frequency', data=data, ax=ax)
        plt.title('Top 20 common word when the Dowjones goes down')
        plt.xticks(rotation='vertical') 
        
    

    def label_distribution(self,dataframe):
        """To watch label distribution. Is your data balanced or not ?  
        
        Args: 
            data(dataframe): 
        
        Returns:
            Returns: This method does not return any value
        """
        describe = dataframe['Label'].value_counts().reset_index()
        describe.rename(columns = {'index':'label','Label':'frequency'},inplace=True)
        
        fig,ax = plt.subplots(figsize=(10, 6))
        sb.barplot(x='label', y='frequency',palette="blue", data=describe, ax=ax)
        plt.title('Label Distribution')
        plt.xticks(rotation='vertical')





    def chart_score(self,dataframe):
        """Visualize the different assessment method between models: AP, Accuracy, F1
        
        Args: 
            data(dataFrame): include name of model and score for each assessment 
        
        Returns:
            Returns: This method does not return any value
        """
        
        dataframe.rename(columns={'Unnamed: 0':'Model'}, inplace=True)
        dataframe.drop('Cm', axis=1, inplace=True)

        td = dataframe.melt(id_vars='Model').rename(columns=str.title)
        fig,ax = plt.subplots(figsize=(10, 10))
        sb.barplot(x='Model', y='Feq', hue='Variable', data=td, ax=ax)
        sb.despine(fig)


        
    def confusion_matrix(self,data):

        """Visualize confusion matrix to easily evaluate model
        
            Args: 
                data(list): 
        
            Returns:
                Returns: This method does not return any value
        """
        
        df_cm = pd.DataFrame(data = data, index = [i for i in '01'],columns = [i for i in '01'])
        plt.figure(figsize = (10,6))
        sb.heatmap(df_cm, annot=True)


    def result_visualization(self,dataframe,listscore):
        self.top20_common(dataframe)
        self.top20_common_go_up(dataframe)
        self.top20_common_go_down(dataframe)
        self.label_distribution(dataframe)
        self.chart_score(listscore)
        # self.confusion_matrix()
        

    