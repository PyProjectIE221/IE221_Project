import python_ie221 as p1
from python_ie221.Processing import *

dt = p1.ReadData('data\Combined_News_DJIA.csv')

pre = p1.PreProcessing()

pre.fully_preprocess(dt.data)

x_train = TFIDFVectorizer(max_features=10000).fit_transform(pre.x_train)
x_test = TFIDFVectorizer(max_features=10000).fit_transform(pre.x_test)

a = KNNClassifier(x_train,pre.y_train, x_test, pre.y_test, n_neighbors=10)

b = KNNClassifier(x_train,pre.y_train, x_test, pre.y_test, n_neighbors=3)

a.knn_process()

b.knn_process()

print(a.score)

print(b.score)