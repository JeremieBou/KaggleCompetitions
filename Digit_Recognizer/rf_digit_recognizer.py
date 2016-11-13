import csv as csv
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('c:/users/JeremieBoudreau/Git/Kaggle/Digit_Recognizer/train.csv', header = 0)
dftest = pd.read_csv('c:/users/JeremieBoudreau/Git/Kaggle/Digit_Recognizer/test.csv', header = 0)

train_data = df.values
test_data = dftest.values

forest = RandomForestClassifier(n_estimators=100)

forest = forest.fit(train_data[0::, 1::], train_data[0::, 0])

output = forest.predict(test_data)

dftest['label'] = output
dfout = dftest['label']
dfout = dfout.to_frame()
dfout['ImageId'] = dfout.index + 1

dfout.to_csv("C:/Users/JeremieBoudreau/Git/Kaggle/Digit_Recognizer/output.csv")
