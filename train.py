import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#Now we have to load the dataset
file_path = 'Car Sales.xlsx - car_data.csv'
data = pd.read_csv(file_path)

#prints out the data set
data.head()






