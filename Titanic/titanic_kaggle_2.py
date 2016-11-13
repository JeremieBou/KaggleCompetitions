# coding: utf-8
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
