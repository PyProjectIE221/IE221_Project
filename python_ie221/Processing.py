#!/usr/bin/python
#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer

class Processing:
    def __init__(self):
      #Leave this line below
      super().__init__()
class TFIDFVectorizer(TfidfVectorizer):
  def __init__(self,*args,**kwargs):
    super(TFIDFVectorizer,self).__init__(*args,**kwargs)
               
  def fit_transform(self,data):
    """ Change to tf-idf vector
    Args: 
    data (list) : path to your data 
    
    Returns:
    sparse matrix of (n_samples, n_features)
    """
    vectorized = super().fit_transform(data)
    return vectorized
class Countvectorizer(CountVectorizer):
  def __init__(self,*args,**kwargs):
    super(Countvectorizer,self).__init__(*args,**kwargs)
  def fit_transform(self,data):
    """ Change to tf-idf vector
    Args: 
    data (list) : path to your data 
    
    Returns:
    sparse matrix of (n_samples, n_features)
    """
    vectorized = super().fit_transform(data)
    return vectorized
class RandomForest(RandomForestClassifier):
  def __init__(self):
    super(RandomForest,self).__init__()
  def fit(self,X_train,y_train):
    """ Build a forest of trees from the training set (X, y).
    Args:
    X_train : array-like, sparse matrix of shape (n_samples, n_features)
    y_train : array-like of shape (n_samples,) or (n_samples, n_outputs)

    Returns:
    self: object
    """
    object = super().fit(X_train,y_train)
    return object
  def score(self,X_test,y_test):
    """ Return the mean accuracy on the given test data and labels.
    Args:
    X_test : array-like of shape (n_samples, n_features)
    y_test : array-like of shape (n_samples,) or (n_samples, n_outputs)

    Return:
    Score : float
    """
    predict_score = super().score(X_test,y_test)
    return predict_score
        
