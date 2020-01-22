import math
import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def TitanicLogistic():
  #Step 1: Load data
  titanic_data = pd.read_csv('TitanicDataset.csv')
  
  print("First 5 entries from loaded dataset")
  print(titanic_data.head())
  
  print("Number of passangers are "+ str(len(titanic_data)))
  
  #Step 2: Analyze data
  print("Visualisation: Survived and nonsurvived passangers")
  figure()
  target = "Survived"
  
  countplot(data=titanic_data, x=target).set_title("Survived and non survived passangers")
  show()
  
  print("Visualisation: Survived and nonsurvived passangers based on Gender")
  figure()
  target = "Survived"
  
  countplot(data=titanic_data, x=target,hue="Sex").set_title("Survived and non survived passangers based on Gender")
  show()
   
  print("Visualisation: Survived and nonsurvived passangers based on Passanger Class")
  figure()
  target = "Survived"

  countplot(data=titanic_data, x=target,hue="PClass").set_title("Survived and non survived passangers based on Passanger Class")
  show()
  
  print("Visualisation: Survived and nonsurvived passangers based on Age")
  figure()
  titanic_data["Age"].plot.hist().set_title("Survived and nonsurvived passangers based on Age")
  show()
  
  print("Visualisation: Survived and nonsurvived passangers based on Fare")
  figure()
  titanic_data["Fare"].plot.hist().set_title("Survived and nonsurvived passangers based on Fare")
  show()
  
  #Step 3: Data Cleaning
  titanic_data.drop("zero", axis=1,inplace=True)
  
  print("First five entries from dataset after removing zero column")
  print(titanic_data.head(5))
  
  print("Values of Sex Column")
  print(pd.get_dummies(titanic_data["sex"]))
  
  print("Values of Sex Column after removing one field")
  Sex = pd.get_dummies(titanic_data["sex"],drop_first = 1)
  print(Sex.head(5))
  
  print("First five entries from dataset after removing zero column")
  print(titanic_data.head(5))
  
  print("First five entries from dataset after removing zero column")
  print(titanic_data.head(5))
  

def main():










if __name__ == "__main__":
  main()
