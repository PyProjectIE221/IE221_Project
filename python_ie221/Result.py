#!/usr/bin/python
#-*- coding: utf-8 -*-
from sklearn.metrics import accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
class Result:
    def __init__(self):
        #leave this line below
        super().__init__()
        self.Cm = None
        self.Ap = None
        self.As = None
        self.F1 = None
    def confusionmatrix(self, y_true,y_pred):
      """ Compute confusion matrix to evaluate the accuracy of a classification.
      
      Args:
        y_true(array-like of shape (n_samples,)): Ground truth (correct) target values.
        y_pred(array-like of shape (n_samples,)): Estimated targets as returned by a classifier.
        
      Results:
        C(ndarray of shape (n_classes, n_classes)):Confusion matrix whose i-th row and j-th column entry indicates the number of samples with true label being i-th class and predicted label being j-th class.

      """
      self.Cm = confusion_matrix(y_true,y_pred)
      return self.Cm
    def accuracyscore(self, y_true,y_pred):
      """ Accuracy classification score.
      
      Args:
          
        y_true(array-like of shape (n_samples,)): Ground truth (correct) target values.
        y_pred(array-like of shape (n_samples,)): Estimated targets as returned by a classifier.
      Results:
          
        Score(float):Predict score
      """
      self.As = accuracy_score(y_true,y_pred)
      return self.As
    def averageprecisionscore(self, y_true,y_pred):
      """ Compute average precision (AP) from prediction scores.
      
      Args:
          
        y_true(array-like of shape (n_samples,)): Ground truth (correct) target values.
        y_pred(array-like of shape (n_samples,)): Estimated targets as returned by a classifier.
      Results:
          
        average_precision(float) : AP accuracy
      """
      self.Ap = average_precision_score(y_true,y_pred)
      return self.Ap
    def f1score(self, y_true,y_pred):
      """ Compute the F1 score, also known as balanced F-score or F-measure.
      
      Args:
          
        y_true(array-like of shape (n_samples,)): Ground truth (correct) target values.
        y_pred(array-like of shape (n_samples,)): Estimated targets as returned by a classifier.
      
    Results:
        f1_score(float or array of float)
      """
      self.F1 = f1_score(y_true , y_pred)
      return self.F1
