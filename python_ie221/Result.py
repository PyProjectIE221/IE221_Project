#!/usr/bin/python
#-*- coding: utf-8 -*-
from sklearn.metrics import accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from Processing import Processing
class Result(Processing):
    def __init__(self,ProCessing):
        #leave this line below
        super().__init__()
        self.y_true = object.y_test
        self.RF_y_pred = object.RF.y_pred
        self.KNN_y_pred = object.KNN.y_pred
        self.SVM_y_pred = object.SVM.y_pred
        self.NV_y_pred = object.NV.y_pred
    def confusionmatrix(self,type='RF'):
        """ Compute confusion matrix to evaluate the accuracy of a classification.
        
        Args:
            y_true(array-like of shape (n_samples,)): Ground truth (correct) target values.
            y_pred(array-like of shape (n_samples,)): Estimated targets as returned by a classifier.
            
        Results:
            C(ndarray of shape (n_classes, n_classes)):Confusion matrix whose i-th row and j-th column entry indicates the number of samples with true label being i-th class and predicted label being j-th class.

        """

        if type == 'RF':
            self.Cm = confusion_matrix(self.y_true,self.RF_y_pred)
        elif type == 'KNN':
            self.Cm = confusion_matrix(self.y_true,self.KNN_y_pred)
        elif type == 'SVM':
            self.Cm = confusion_matrix(self.y_true,self.SVM_y_pred)
        elif type == 'NV':
            self.Cm = confusion_matrix(self.y_true,self.NV_y_pred)
        return self.Cm
  
    def accuracyscore(self, type = 'RF'):
        """ Accuracy classification score.
        
        Args:
            
            y_true(array-like of shape (n_samples,)): Ground truth (correct) target values.
            y_pred(array-like of shape (n_samples,)): Estimated targets as returned by a classifier.
        Results:
            
            Score(float):Predict score
        """

        if type == 'RF':
            self.As = accuracy_score(self.y_true,self.RF_y_pred)
        elif type == 'KNN':
            self.As = accuracy_score(self.y_true,self.KNN_y_pred)
        elif type == 'SVM':
            self.As = accuracy_score(self.y_true,self.SVM_y_pred)
        elif type == 'NV':
            self.As = accuracy_score(self.y_true,self.NV_y_pred)
        return self.As

    def averageprecisionscore(self, type = 'RF'):
        """ Compute average precision (AP) from prediction scores.
        
        Args:
            
            y_true(array-like of shape (n_samples,)): Ground truth (correct) target values.
            y_pred(array-like of shape (n_samples,)): Estimated targets as returned by a classifier.
        Results:
            
            average_precision(float) : AP accuracy
        """

        if type == 'RF':
            self.Ap = average_precision_score(self.y_true,self.RF_y_pred)
        elif type == 'KNN':
            self.Ap = average_precision_score(self.y_true,self.KNN_y_pred)
        elif type == 'SVM':
            self.Ap = average_precision_score(self.y_true,self.SVM_y_pred)
        elif type == 'NV':
            self.Ap = average_precision_score(self.y_true,self.NV_y_pred)
        return self.Ap

    def f1score(self, type = "RF"):
        """ Compute the F1 score, also known as balanced F-score or F-measure.
        
        Args:
            
            y_true(array-like of shape (n_samples,)): Ground truth (correct) target values.
            y_pred(array-like of shape (n_samples,)): Estimated targets as returned by a classifier.
        
        Results:
            f1_score(float or array of float)
        """
        
        if type == 'RF':
            self.F1 = f1_score(self.y_true,self.RF_y_pred)
        elif type == 'KNN':
            self.F1 = f1_score(self.y_true,self.KNN_y_pred)
        elif type == 'SVM':
            self.F1 = f1_score(self.y_true,self.SVM_y_pred)
        elif type == 'NV':
            self.F1 = f1_score(self.y_true,self.NV_y_pred)
        return self.F1

    def full_score(self):
        """ Compute full score for algorithm

        """

        y_pred_list = [self.RF_y_pred,self.KNN_y_pred,self.SVM_y_pred,self.NV_y_pred ]
        List_score = []
        for i in y_pred_list:
            Cm = confusion_matrix(self.y_true,i)
            As = accuracy_score(self.y_true,i)
            Ap = average_precision_score(self.y_true,i)
            F1 = f1_score(self.y_true , i)
            List_score.append([Cm,As,Ap,F1])
        self.List_score = pd.DataFrame(List_score,columns = ['Cm','As','Ap','F1'],index = ['RF','KNN','SVM','NV'])
        return self.List_score
        

