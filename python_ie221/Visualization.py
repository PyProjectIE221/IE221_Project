#!/usr/bin/python
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
from collections import Counter
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

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
        plt.title('Top 20 common word')
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
        sb.barplot(x='label', y='frequency', data=describe, ax=ax)
        plt.title('Label Distribution')
        plt.xticks(rotation='vertical')



    def chart_score(self,data):
        """Visualize the different assessment method between models: AP, Accuracy, F1
        
        Args: 
            data(dataFrame): include name of model and score for each assessment 
        
        Returns:
            Returns: This method does not return any value
        """
        
        df_score = pd.DataFrame(data = array,columns=['name_model','frequency'])

        fig,ax = plt.subplots(figsize=(10, 6))
        sb.barplot(x='name_model', y='frequency', data = df_score, ax = ax)
        plt.title('The different acurrayscore between models')
        plt.xticks(rotation='vertical')


        
    def confusion_matrix(self,data):
    """Visualize confusion matrix to easily evaluate model
        
        Args: 
            data(list): 
        
        Returns:
            Returns: This method does not return any value
    """
        df_cm = pd.DataFrame(array, index = [i for i in '01'],
                  columns = [i for i in '01'])
        plt.figure(figsize = (10,7))
        sb.heatmap(df_cm, annot=True)

    
