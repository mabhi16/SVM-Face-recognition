# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 17:52:10 2020

@author: CLOAK AND DAGGER
"""
import csv
import random
from os import listdir
path = 'G:/IPPR/face_img/Project_DataSet/'
Image_list = list()
i = 0 
j = 0 


file_name=listdir(path)

for files in file_name:
    #split the jpg and append with the numbers to list
    Image_list.append(files.split('.jpg')[0])
    #Ramdomize the list 
    
random.shuffle(Image_list)
print(Image_list[:10])
#%% 
print(Image_list[0:50]) 
print(len(Image_list))


#%%
f = open('IPPRImage_list.csv', 'w', newline='')
for Img in Image_list:
   csv.writer(f).writerow(Img)
f.close()
            
#%%
encode_labels = {
  "A": 1,
  "D": 2,
  "H": 3,
  "I": 4,
  "K": 5,
  "M": 6,
}
print(encode_labels[0].values())

#%%
f = open('IPPR_labels.csv', 'w', newline='')
for i,filename in enumerate(Image_list):
    if filename[0] =='A':
        csv.writer(f).writerow('1')   
    elif filename[0] =='D':
        csv.writer(f).writerow('2')
    elif filename[0] =='H':
        csv.writer(f).writerow('3')
    elif filename[0] =='I':
        csv.writer(f).writerow('4')
    elif filename[0] =='K':
        csv.writer(f).writerow('5')
    elif filename[0] =='M':
        csv.writer(f).writerow('6') 
        
     
#%%    