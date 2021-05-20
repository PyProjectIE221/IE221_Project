import python_ie221 as p1
import pickle

#Read data
dt = p1.ReadData('data/Combined_News_DJIA.csv')

#Preprocessing
pre = p1.PreProcessing()

pre.fully_preprocess(dt.data)

#Processing
process = p1.Processing(pre.x_train, pre.x_test, pre.y_train, pre.y_test)
process.RandomForest()
process.KNNClassifier()
process.Naive()
process.SVMLinearSVC()

#Result
result = p1.Result(process)


##visualize
visual = p1.Visualization()
visual.top20_common(pre.pre_data)
visual.top20_common_go_up(pre.pre_data)
visual.top20_common_go_down(pre.pre_data)
visual.label_distribution(pre.pre_data)

#Save class contains models by pickle
filename = "Model"
outfile = open(filename,'wb')
pickle.dump(process,outfile)
outfile.close()

#Load class contains models by pickle(Optional)
#infile = open(filename,'rb')
#class_model = pickle.load(infile)
#infile.close()