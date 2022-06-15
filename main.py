#import lib
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
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

#replacing cat data
#data["SMOKING"] = np.where(data["LUNG_CANCER"] == 1, "NO", "YES")
#data["YELLOW_FINGERS"] = np.where(data["LUNG_CANCER"] == 1, "NO", "YES")
#data["ANXIETY"] = np.where(data["LUNG_CANCER"] == 1, "NO", "YES")
#data["CHRONIC DISEASE"] = np.where(data["LUNG_CANCER"] == 1, "NO", "YES")
#data["ALLERGY"] = np.where(data["LUNG_CANCER"] == 1, "NO", "YES")
#data["ALCOHOL CONSUMING"] = np.where(data["LUNG_CANCER"] == 1, "NO", "YES")
#data["COUGHING"] = np.where(data["LUNG_CANCER"] == 1, "NO", "YES")
#data["SHORTNESS OF BREATH"] = np.where(data["LUNG_CANCER"] == 1, "NO", "YES")
#data["SWALLOWING DIFFICULTY"] = np.where(data["LUNG_CANCER"] == 1, "NO", "YES")
#data["CHEST PAIN"] = np.where(data["LUNG_CANCER"] == 1, "NO", "YES")
#data["LUNG_CANCER"] = np.where(data["LUNG_CANCER"] == 1, "NO", "YES")
#print(data.head())

#features and target
feature = data.drop("LUNG_CANCER",axis="columns")
target = data["LUNG_CANCER"]
print(feature.head())
print(target.head())

#feature scaling
#nfeatures = pd.get_dummies(feature, drop_first=True)
#print(nfeatures.head())

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

#features importance
#x = feature.columns
#y = model.feature_importances_
#plt.figure(figsize=(12,4))
#plt.bar(x, y)
#plt.show()
#print(y)

#save the model
with open("lungc.model","wb") as f:
	pickle.dump(model,f)