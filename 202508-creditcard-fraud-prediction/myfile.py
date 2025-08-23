# import required packages
import pandas as pd

# read in train and test data
fraud_train = pd.read_csv('fraudTrain.csv')
fraud_test = pd.read_csv('fraudTest.csv')

print(fraud_train.head())
