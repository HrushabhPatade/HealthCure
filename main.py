#import lib
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pickle

#load the data
data=pd.read_csv("survey lung cancer.csv")
data.drop(["AGE","GENDER","PEER_PRESSURE","FATIGUE ","WHEEZING"],axis="columns",inplace=True)
print(data.head())

#understand the data
res = data.isnull().sum()
print(res)



#features and target
feature = data.drop("LUNG_CANCER",axis="columns")
target = data["LUNG_CANCER"]
print(feature.head())
print(target.head())



#train and test
x_train, x_test, y_train, y_test = train_test_split(feature,target,random_state=130)

#model 
model = GaussianNB()
model.fit(feature,target)

#classification report
cr = classification_report(y_test, model.predict(x_test))
print(cr)

#predict
data=[[1,2,2,1,1,2,2,2,2,2]]
res = model.predict(data)
print("res = ",res)



#save the model
with open("lungc.model","wb") as f:
	pickle.dump(model,f)