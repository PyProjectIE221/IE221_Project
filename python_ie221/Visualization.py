#!/usr/bin/python
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
from collections import Counter
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

class Visualization:
    def __init__(self):
        #leave this line below
        super().__init__()

    
    """Top 20 common word  
        
        Args: 
            data(dataframe): 
        
        Returns:
            Returns: This method does not return any value
    """
    def top20_common(self,dataframe):
        counter = Counter()
        for row in range(dataframe.shape[0]):
            counter += Counter(dataframe.iloc[row,2].split(' '))

        most_common_20 = counter.most_common(20)
        data = pd.DataFrame(data = most_common_20, columns=['word','frequency'])

        fig,ax = plt.subplots(figsize=(10, 6))
        sb.barplot(x='word', y='frequency', data=data, ax=ax)
        plt.title('Top 20 common word')
        plt.xticks(rotation='vertical')
    

    """Top 20 common word in label 1  
        
        Args: 
            data(dataframe): 
        
        Returns:
            Returns: This method does not return any value
    """
    def top20_common_label_1(self,dataframe):
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
        
    
    """Top 20 common word in label 0  
        
        Args: 
            data(dataframe): 
        
        Returns:
            Returns: This method does not return any value
    """
    def top20_common_label_0(self,dataframe):
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
        
    
    """Label Distribution  
        
        Args: 
            data(dataframe): 
        
        Returns:
            Returns: This method does not return any value
    """
    def label_distribution(self,dataframe):
        describe = dataframe['Label'].value_counts().reset_index()
        describe.rename(columns = {'index':'label','Label':'frequency'},inplace=True)
        
        fig,ax = plt.subplots(figsize=(10, 6))
        sb.barplot(x='label', y='frequency', data=describe, ax=ax)
        plt.title('Label Distribution')
        plt.xticks(rotation='vertical')



    """Chart score 
        
        Args: 
            data(list): 
        
        Returns:
            Returns: This method does not return any value
    """
    def chart_score(self,data):
        df_score = pd.DataFrame(data = array,columns=['name_model','frequency'])

        fig,ax = plt.subplots(figsize=(10, 6))
        sb.barplot(x='name_model', y='frequency', data = df_score, ax = ax)
        plt.title('The difference acurrayscore between models')
        plt.xticks(rotation='vertical')


        
    """Confusion maxtrix  
        
        Args: 
            data(list): 
        
        Returns:
            Returns: This method does not return any value
    """
    def confusion_matrix(self,data):
        df_cm = pd.DataFrame(array, index = [i for i in '01'],
                  columns = [i for i in '01'])
        plt.figure(figsize = (10,7))
        sb.heatmap(df_cm, annot=True)

    
