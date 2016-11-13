# coding: utf-8

import csv as csv
import numpy as np
csv_file_object = csv.reader(open('c:/Users/JeremieBoudreau/Git/Kaggle/Titanic/Data/train.csv'))
header = csv_file_object.next()
csv_file_object
header = csv_file_object.next()
header = csv_file_object.next
header = csv_file_object.next()
csv_file_object = csv.reader(open('c:/Users/JeremieBoudreau/Git/Kaggle/Titanic/Data/train.csv', 'rb'))
header = csv_file_object.next()
header = csv_file_object.next()
csv_file_object = csv.reader(open('c:/Users/JeremieBoudreau/Git/Kaggle/Titanic/Data/train.csv', 'rb'))
header = csv_file_object.next()
header = csv_file_object.__next__()
header = next(csv_file_object)
csv_file_object = csv.reader(open('c:/Users/JeremieBoudreau/Git/Kaggle/Titanic/Data/train.csv', 'rb'))
header = next(csv_file_object)
csv_file_object = csv.reader(open('c:/Users/JeremieBoudreau/Git/Kaggle/Titanic/Data/train.csv'))
header = next(csv_file_object)
data = []
for row in csv_file_object:
    data.append(row)
    
data = np.array(data)
da
data
data[0:15,5]
data[0:,5]
data[0::,5]
ages_onboard = data[0::, 5].astype(np.float)
import panadas as pd
import pandas as pd
df = pd.read_csv('c:/users/JeremieBoudreau/Git/Kaggle/Titanic/train.csv', header = 0)
df = pd.read_csv('c:/users/JeremieBoudreau/Git/Kaggle/Titanic/data/train.csv', header = 0)
df
df.head(3)
type(df)
df.dtypes
df.info()
df.describe()
df['Age'][0:10]
df.age[0:10]
df.Age[0:10]
df.Age.mean
df.Age.mean()
df.Age.median()
age_mean = df.Age.mean()
age_median = df.Age.median()
get_ipython().magic('save titanic_kaggle_1')
get_ipython().magic('save titanic_kaggle_1 20')
get_ipython().magic('save titanic_kaggle_1 0-30')
get_ipython().magic('save titanic_kaggle_2 28-40')
get_ipython().magic('save titanic_kaggle_2 28-60')
df[['Sex', 'Pclass', 'Age']]
df[df['Age'] > 60]
df[df['Age'] > 60][['Sex', 'Pclass', 'Age', 'Survived']]
df[df['Age'].isnull()][['Sex', 'Pclass', 'Age']]
for i in range(1,4):
    print i, len(df[ (df['Sex'] == 'male') & (df['Pclass'] == 1)])
    
print(i, len(df[ (df['Sex'] == 'male') & (df['Pclass'] == 1)]))
for i in range(1,4):
    print(i, len(df[ (df['Sex'] == 'male') & (df['Pclass'] == 1)]))
    
for i in range(1,4):
    print(i, len(df[ (df['Sex'] == 'male') & (df['Pclass'] == i)]))
    
import pylab as p
df['Age'].hist()
P.show()
p.show()
df['Age'].dropna().hist()(bins = 16, range(0,80), alpha = .5)
df['Age'].dropna().hist()(bins=16, range(0,80), alpha=.5)
df['Age'].dropna().hist()(bins=16, range=(0,80), alpha=.5)
df['Age'].dropna().hist(bins=16, range=(0,80), alpha=.5)
p.show()
df['Age'].dropna().hist(bins=16, range=(0,80), alpha=.5)
p.show()
df['Gender'] = 4
df['Gender'] = df['Sex'].map(lambda x: x[0].upper())
df['Gender']
df['Gender'] = df['Sex'].map({'female' : 0, 'map':1}).astype(int)
df['Gender'] = df['Sex'].map({'female' : 0, 'male':1}).astype(int)
df.Gender
median_ages = np.zeroes((2,3))
median_ages = np.zeros((2,3))
median_ages
for i in range(0, 2):
    for j in range(0, 3):
        median_ages[i, j] = df[(df['Gender'] == i) & (df['Pclass'] == j+1)]['Age'].dropna().median()
        
median_ages
df['AgeFill' = df['Age']





fas


]
df['AgeFill'] = df['Age']
df.head()
df[df['Age'].isnull()][['Gender','Pclass','Age','AgeFill\]].head(10)
df[df['Age'].isnull()][['Gender','Pclass','Age','AgeFill']].head(10)
get_ipython().magic('save kaggle_titanic_3 0-200')
