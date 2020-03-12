# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:01:05 2020

@author: Abhishek
"""
import numpy as np
from sklearn import svm

per_t = np.int_(6637*0.8)
per_tv = np.int_(6637*0.2)
x_train = np.zeros((per_t,648),dtype=np.float32())
x_test = np.zeros((per_tv+1,648),dtype=np.float32())
y_train = np.zeros((per_t),dtype=np.str)
y_test = np.zeros((per_tv+1),dtype=np.str)
i,j,k = 0,0,0
feature = np.load('feature.npy')
labels = np.load('labels.npy')
# for i,el in enumerate(feature):
#     if (i<=per_t-1):
#         x_train[i,:]=el
#         y_train[i]=labels[i]
#     else:
#         x_test[j,:]=el
#         y_test[j]=labels[i]
#         j=j+1
#%%
#SVM Training
from sklearn.externals import joblib
clf = svm.SVC(C = 0.1,kernel = 'poly',gamma = 'scale',probability=True)
clf.fit(feature,labels)
# save the model to disk
filename = 'finalized_model.sav'
joblib.dump(clf, filename)
#loaded_model = joblib.load(filename)
#y_res = loaded_model.predict(x_test)
#y_res = clf.predict(x_test)
# i = 0
# j = 0
# count = 0
# from sklearn.metrics import confusion_matrix
# for i,j in enumerate(y_test):
#     if(y_res[i] != j):
#         print('Mismatch at position ',i)
#         count = count+1
# print('Number of errors ',count)
# print(confusion_matrix(y_test,y_res))
    