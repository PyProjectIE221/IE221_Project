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

    # 
    def top30_wordup(self,data_input):
        fig, ax = plt.subplots(figsize=(10, 6))
        sb.barplot(x='word', y='count', data=data_input, ax=ax)
        plt.title('Top 30 words when DJIA goes up')
        plt.xticks(rotation='vertical')
    
    #
    def top30_worddown(self,data_input):
        fig, ax = plt.subplots(figsize=(10, 6))
        sb.barplot(x='word', y='count', data=data_input, ax=ax)
        plt.title('Top 30 words when DJIA goes down')
        plt.xticks(rotation='vertical')
    
    
    def top20_common(self,dataframe):
        counter = Counter()
        for row in range(dataframe.shape[0]):
            counter += Counter(dataframe.iloc[row,2].split(' '))

        most_common_20 = counter.most_common(20)
        data = pd.DataFrame(data = most_common_20, columns=['word','feq'])

        fig,ax = plt.subplots(figsize=(10, 6))
        sb.barplot(x='word', y='feq', data=data, ax=ax)
        plt.title('Top 20 common word')
        plt.xticks(rotation='vertical')
        
    def top20_common_label_1(self,dataframe):
        counter = Counter()
        for row in range(dataframe.shape[0]):
            if(dataframe.iloc[row,1] == 1):
                counter += Counter(dataframe.iloc[row,2].split(' '))
        most_common_20 = counter.most_common(20)
        data = pd.DataFrame(data = most_common_20, columns=['word','feq'])
        
        fig,ax = plt.subplots(figsize=(10, 6))
        sb.barplot(x='word', y='feq', data=data, ax=ax)
        plt.title('Top 20 common word in label 1')
        plt.xticks(rotation='vertical')  
        
        
    def top20_common_label_0(self,dataframe):
        counter = Counter()
        for row in range(dataframe.shape[0]):
            if(dataframe.iloc[row,1] == 1):
                counter += Counter(dataframe.iloc[row,2].split(' '))
        most_common_20 = counter.most_common(20)
        data = pd.DataFrame(data = most_common_20, columns=['word','feq'])
        
        fig,ax = plt.subplots(figsize=(10, 6))
        sb.barplot(x='word', y='feq', data=data, ax=ax)
        plt.title('Top 20 common word  in label 0')
        plt.xticks(rotation='vertical') 
        
    
    def label_distribution(self,dataframe):
        describe = dataframe['Label'].value_counts().reset_index()
        describe.rename(columns = {'index':'label','Label':'feq'},inplace=True)
        
        fig,ax = plt.subplots(figsize=(10, 6))
        sb.barplot(x='label', y='feq', data=describe, ax=ax)
        plt.title('Label Distribution')
        plt.xticks(rotation='vertical')
    
    
    #
    # def result(self,data):
    #     logit_roc_auc = roc_auc_score(data.test_labels, lr_clf.predict(data.test_features))
    #     fpr, tpr, thresholds = roc_curve(data.test_labels, lr_clf.predict_proba(data.test_features)[:,1])
    #     plt.figure()
    #     plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
    #     plt.plot([0, 1], [0, 1],'r--')
    #     plt.xlim([0.0, 1.0])
    #     plt.ylim([0.0, 1.05])
    #     plt.xlabel('False Positive Rate')
    #     plt.ylabel('True Positive Rate')
    #     plt.title('Receiver operating characteristic')
    #     plt.legend(loc="lower right")
    #     plt.savefig('Log_ROC')
    #     plt.show()
