#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python37-32\python.exe

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler

warnings.filterwarnings("ignore")

df = pd.read_csv("Banking Fraud.csv")  # here dataset new

x = df[['income', 'customer_age', 'credit_risk_score']]
y = df[['fraud_bool']]
x = x.astype(int);
y = y.astype(int);

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
rus = RandomUnderSampler(sampling_strategy='majority')
X_train_rus, y_train_rus = rus.fit_resample(X_train, y_train)

log_reg = LogisticRegression()

log_reg.fit(X_train_rus, y_train_rus)

pickle.dump(log_reg, open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl', 'rb'))
