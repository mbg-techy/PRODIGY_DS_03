# -*- coding: utf-8 -*-
"""Prodigy_InfoTech-Intern-Task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S8eLE9US13CN8PbTzeII25jGwLWLCms2

#Task-03

Build a decision tree classifier to predict whether a customer will purchase a product or service based on their demographic and behavioral data. Use a dataset such as the Bank Marketing dataset from the UCI Machine Learning Repository.



Sample Dateset :- https://archive.ics.uci.edu/ml/datasets/Bank+Marketing

# Importing libraries required
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import LabelEncoder

"""#Importing the data and visualizing some distributions"""

df=pd.read_csv("/content/bank.csv",delimiter=';')
df

"""#Exploratory Data Analysis"""

df.shape

df.info()

df.columns

df.describe()

df.isnull().sum()

col = list(df.columns)
categorical_features = []
numerical_features = []
for i in col:
    if len(df[i].unique()) > 6:
        numerical_features.append(i)
    else:
        categorical_features.append(i)

print('Categorical Features :',*categorical_features)
print('Numerical Features :',*numerical_features)

plt.figure(figsize=(10,8))
sns.heatmap(df.corr(),annot=True,cmap='coolwarm')
plt.title('Correlation Map')
plt.show()

label_encoder=LabelEncoder()
cat_cols=['job','marital','education','default','housing','loan','contact','month','poutcome','y']
for col in cat_cols:
  df[col]=label_encoder.fit_transform(df[col])

plt.figure(figsize=(10,8))
sns.countplot(x='y',data=df)
plt.title('Distribution of Outcome')
plt.show()

plt.figure(figsize=(10,8))
sns.histplot(df['age'],bins=20,kde=True)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Age Distribution')
plt.show()

sns.countplot(x='education',data=df,hue='y')
plt.show()

sns.countplot(x='marital',data=df,hue='y')
plt.show()

"""#Test Train Split"""

X=df.drop('y',axis=1)
y=df['y']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=42)

"""#Decision Tree Classifier"""

des=DecisionTreeClassifier(random_state=42)
des.fit(X_train,y_train)

"""#Parameters for evaluation"""

y_pred=des.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
conf_mat=confusion_matrix(y_test,y_pred)
cls_rep=classification_report(y_test,y_pred)
print('Accuracy:',accuracy)
print('Conf_Mat',conf_mat)
print('Class_Report',cls_rep)